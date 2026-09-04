
def get_user_permission_scopes(user_id : str) -> list[dict]:
    """
    Fake permission resolver. In a real system this would look up the
    user's department/role/tenant and return the scopes they're allowed
    to search (e.g. ["hr-all", "finance-managers"]). Here everyone can
    see the single "all-employees" scope so the demo works out of the box.
    """


    return ["all-employees"]