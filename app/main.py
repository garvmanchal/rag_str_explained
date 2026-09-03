from fastapi import FastAPI
from app.ingestion.seed import seed_index
from app.database.vector_db import vector_db


app = FastAPI(title = "LEARNING RAG STR")

@app.get("/")
def greet():
    return "THIS IS MY LEARNING RAG PROJECT"



@app.on_event("startup")
async def startup():
    seed_index()

# We added /debug/rows only for testing,We wanted to check whether seed_index() actually populated it.

@app.get("/debug/rows")
def debug_rows():
    return vector_db.rows
    