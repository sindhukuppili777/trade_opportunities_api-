# Trade Opportunities API

FastAPI service that analyzes Indian sector trade opportunities using Gemini AI.

## Features
- Sector market analysis
- Gemini AI integration
- DuckDuckGo web search
- Authentication
- Rate limiting
- In-memory storage

## Run

pip install -r requirements.txt
uvicorn main:app --reload

## Endpoint

GET /analyze/{sector}

Header:
Authorization: Bearer secret123