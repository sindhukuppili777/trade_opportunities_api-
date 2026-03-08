from fastapi import HTTPException

VALID_TOKEN = "secret123"

def verify_token(token: str):

    if token != VALID_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    return "guest_user"





