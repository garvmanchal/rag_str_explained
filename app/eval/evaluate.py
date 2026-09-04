from app.model.schema import AskRequest
from app.main import ask


async def golden_check():
    """
    Minimal recall@k / groundedness-style regression check: re-run a known
    question through the whole pipeline and confirm both that the expected
    fact ("12" sick days) appears AND that the answer is actually cited.
    In production you'd run a whole golden set like this before every
    index or prompt change ships (see the tutorial's "RAG Release Gate").
    """

    result = await ask(AskRequest(user_id= "u1", question= "How many sick days I do get ?",
                                    workspace_id = "acme"  ))
    passed = "12" in result.answer and len(result.citations)> 0
    return{"golden_case_passed": passed, "answer" : result.answer}
