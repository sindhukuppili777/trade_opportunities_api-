from fastapi import HTTPException

VALID_TOKEN = "secret123"

def verify_token(token: str):

    if token != VALID_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    return "guest_user"





# from fastapi import Header, HTTPException
# import os

# API_TOKEN = os.getenv("API_TOKEN", "secret123")

# def verify_token(authorization: str | None = Header(None)):

#     if authorization is None:
#         raise HTTPException(status_code=401, detail="Authorization header missing")

#     if authorization != f"Bearer {API_TOKEN}":
#         raise HTTPException(status_code=401, detail="Invalid token")

#     return authorization