import time
from fastapi import HTTPException

RATE_LIMIT = 5
TIME_WINDOW = 60

user_requests = {}

def check_rate_limit(user):

    current_time = time.time()

    if user not in user_requests:
        user_requests[user] = []

    user_requests[user] = [
        t for t in user_requests[user] if current_time - t < TIME_WINDOW
    ]

    if len(user_requests[user]) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    user_requests[user].append(current_time)






