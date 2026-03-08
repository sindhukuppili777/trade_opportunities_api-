from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from data_collector import collect_market_data
from ai_analysis import generate_market_report
from rate_limiter import check_rate_limit
from auth import verify_token

app = FastAPI(title="Trade Opportunities API")

security = HTTPBearer()

@app.get("/analyze/{sector}")
async def analyze(sector: str, token: HTTPAuthorizationCredentials = Depends(security)):

    user = verify_token(token.credentials)

    # rate limiting
    check_rate_limit(user)

    # collect market data
    market_data = collect_market_data(sector)

    if not market_data:
        raise HTTPException(status_code=404, detail="No market data found")

    # generate AI report
    report = generate_market_report(sector, market_data)

    return {
        "sector": sector,
        "report_markdown": report
    }


# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# app = FastAPI()

# security = HTTPBearer()

# # sector opportunity data
# data = {
#     "technology": ["AI tools", "Cloud services", "Cybersecurity"],
#     "pharmaceuticals": ["Generic drugs", "Vaccine export"],
#     "agriculture": ["Organic farming", "Food processing"]
# }

# @app.get("/analyze/{sector}")
# async def analyze(sector: str, token: HTTPAuthorizationCredentials = Depends(security)):

#     # token validation
#     if token.credentials != "secret123":
#         raise HTTPException(status_code=401, detail="Invalid token")

#     # return opportunities
#     return {
#         "sector": sector,
#         "opportunities": data.get(sector.lower(), "No data available")
#     }





# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# app = FastAPI()

# security = HTTPBearer()

# @app.get("/analyze/{sector}")
# async def analyze(sector: str, token: HTTPAuthorizationCredentials = Depends(security)):
    
#     if token.credentials != "secret123":
#         raise HTTPException(status_code=401, detail="Invalid token")

#     return {
#         "sector": sector,
#         "message": "Authorized access"
#     }













# # from fastapi import FastAPI, Depends, HTTPException
# # from auth import verify_token
# # from rate_limiter import check_rate_limit
# # from data_collector import collect_market_data
# # from ai_analysis import analyze_sector

# # app = FastAPI(title="Trade Opportunities API")

# # @app.get("/analyze/{sector}")
# # async def analyze(sector: str, session_id: str = Depends(verify_token)):

# #     if not sector.isalpha():
# #         raise HTTPException(status_code=400, detail="Invalid sector name")

# #     check_rate_limit(session_id)

# #     market_data = collect_market_data(sector)

# #     report = analyze_sector(sector, market_data)

# #     return {
# #         "sector": sector,
# #         "report_markdown": report
# #     }