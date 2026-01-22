from fastapi import Request
from fastapi.responses import RedirectResponse

def require_login(request: Request):
    """
    Checks if a user is logged in.
    If NOT logged in: Returns a RedirectResponse to the login page.
    If Logged in: Returns the user dictionary.
    """
    if "user" not in request.session:
        # Instead of raising an error, we return a RedirectResponse
        return RedirectResponse(url="/login", status_code=303)
    
    return request.session["user"]