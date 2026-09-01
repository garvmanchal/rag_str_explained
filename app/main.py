from fastapi import FastAPI


app = FastAPI(title = "LEARNING RAG STR")

@app.get("/")
def greet():
    return "THIS IS MY LEARNING RAG PROJECT"



