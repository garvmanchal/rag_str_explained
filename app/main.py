from fastapi import FastAPI
from app.ingestion.seed import seed_index


app = FastAPI(title = "LEARNING RAG STR")

@app.get("/")
def greet():
    return "THIS IS MY LEARNING RAG PROJECT"



@app.on_event("startup")
async def startup():
    seed_index()