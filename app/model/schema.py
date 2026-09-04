from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    user_id : str 
    question : str = Field(min_length=1, max_length= 2000)
    workspace_id : str

class Source(BaseModel):
    chunk_id : str
    title : str
    section : str | None = None

class AskResponse(BaseModel):
    answer : str
    citations : list[str]
    sources : list[Source]
    needs_human_review : bool = False