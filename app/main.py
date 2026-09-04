from fastapi import FastAPI, Depends , HTTPException
from app.ingestion.seed import seed_index
from app.database.vector_db import vector_db

from app.model.schema import AskRequest, AskResponse , Source

from app.auth.authentication import get_current_user

from app.auth.permission import get_user_permission_scopes

from app.retrieval.search import hybrid_search

from app.re_rank.reranking import re_rank

from app.llm.prompt import built_cited_prompt

from app.llm.llm import call_llm

from app.core.citation_validation import validate_citation

from app.audit.audit import log_rag_trace , audit_log


app = FastAPI(title = "LEARNING RAG STR")

@app.get("/")
def greet():
    return "THIS IS MY LEARNING RAG PROJECT"

@app.post("/ask", response_model= AskResponse)
async def ask(req : AskRequest, user = Depends(get_current_user)):

    #step 1 - get user permission scope

    allowed_scopes = get_user_permission_scopes(user)

    #step 2 - metadata - filtered hybrid search 

    candidates = await hybrid_search(req.question , allowed_scopes, top_k = 30)

    #step 3 : guadrails-filtered - no evidence found at all
    if not candidates :
        return AskResponse(answer = "I could not find relevent policy content",
                           citations= [], sources = [])


    # step 4 - re rank wide candidates down to the best few
    top_chunks = await re_rank(req.question , candidates , keep = 5)


    #step 5 - cited prompt --> llm call
    prompt = built_cited_prompt(req.question, top_chunks)
    answer = await call_llm(prompt, top_chunks)

    #step 6 - citation validation 
    try :
        validate_citation(answer, top_chunks)
    except ValueError as e :
        raise HTTPException(status_code= 500, detials = f"Groundness check failed : {e}")


    #step 7 - audit log for observablity
    log_rag_trace(req.question ,top_chunks, answer)


    #step 8 - map citation labels back to full source info for ui
    label_to_chunks = {c['citations_label']: c for c in top_chunks}
    sources = [
        Source(chunk_id=label_to_chunks[label]["chunk_id"],
               title = label_to_chunks[label]["source_id"],
               section = label_to_chunks[label]["heading"])
        for label in answer.get("citation",[])
    ]
    return AskResponse(**answer, sources = sources)



@app.on_event("startup")
async def startup():
    seed_index()

# We added /debug/rows only for testing,We wanted to check whether seed_index() actually populated it.

@app.get("/debug/rows")
def debug_rows():
    return vector_db.rows


@app.get("/eval/golden-check")
async def golden_check_endpoint():
    from app.eval.evaluate import golden_check

    return await golden_check()


@app.get("/audit-log")
def get_audit_log():
    """
    Returns the in-memory audit trail.
    """
    return audit_log