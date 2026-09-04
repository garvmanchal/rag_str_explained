from fastapi import FastAPI, Depends
from app.ingestion.seed import seed_index
from app.database.vector_db import vector_db

from app.model.schema import AskRequest, AskResponse , Source

from app.auth.authentication import get_current_user

from app.auth.permission import get_user_permission_scopes



app = FastAPI(title = "LEARNING RAG STR")

@app.get("/")
def greet():
    return "THIS IS MY LEARNING RAG PROJECT"

@app.post("/ask", response_model= AskResponse)
async def ask(req : AskRequest, user = Depends(get_current_user)):
    pass



@app.on_event("startup")
async def startup():
    seed_index()

# We added /debug/rows only for testing,We wanted to check whether seed_index() actually populated it.

@app.get("/debug/rows")
def debug_rows():
    return vector_db.rows
    