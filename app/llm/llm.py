

async def call_llm(chunks : list[dict]) -> dict :
    if not chunks:
        return{"answer": "I could not find relevent policy content.",
               "citations": [], "needs_human_review" : True}

    top = chunks[0]  # highest-reranked chunk
    return {
        "answer" : f"{top['text'][:200]}... [{top['citations_label']}]",
        "citations" : [top["citations_label"]],
        "needs_human_review" : False
    }