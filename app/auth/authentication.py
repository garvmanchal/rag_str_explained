
def get_current_user(user_id : str =  "u1") -> str :
    """
    Stand-in for real authentication (e.g. reading a JWT/session cookie).
    FastAPI's Depends() wires this into the /ask route below.
    """

    return user_id