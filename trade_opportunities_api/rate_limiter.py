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






# import os
# from fastapi import HTTPException
# from storage import request_counts

# RATE_LIMIT = int(os.getenv("RATE_LIMIT", 5))

# def check_rate_limit(session_id):

#     if session_id not in request_counts:
#         request_counts[session_id] = 0

#     request_counts[session_id] += 1

#     if request_counts[session_id] > RATE_LIMIT:
#         raise HTTPException(
#             status_code=429,
#             detail="Rate limit exceeded. Try again later."
#         )