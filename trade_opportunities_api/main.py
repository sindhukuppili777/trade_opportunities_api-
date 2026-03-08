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


