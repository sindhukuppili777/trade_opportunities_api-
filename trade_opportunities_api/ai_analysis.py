def generate_market_report(sector: str, market_data):

    news_points = "\n".join([f"- {item}" for item in market_data])

    report = f"""
# Market Analysis Report

## Sector
{sector.title()} Sector - India

## Current Market Insights
{news_points}

## Trade Opportunities
- Increasing domestic demand
- Export opportunities in emerging markets
- Government incentives and policy support

## Potential Risks
- Global market competition
- Regulatory changes
- Supply chain disruptions

## Conclusion
Based on recent market trends and news, the **{sector} sector**
in India presents promising trade opportunities with growing
demand and investment potential.
"""

    return report



# import os
# import requests

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# def analyze_sector(sector: str, market_data: dict):

#     if not GEMINI_API_KEY:
#         return "Error: GEMINI_API_KEY not set."

#     prompt = f"""
#     Write a detailed financial analysis report for the {sector} sector.

#     Market Data:
#     {market_data}

#     Include:
#     - Market overview
#     - Key companies
#     - Growth drivers
#     - Risks
#     - Future outlook
#     """

#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

#     headers = {
#         "Content-Type": "application/json"
#     }

#     body = {
#         "contents": [
#             {
#                 "parts": [
#                     {"text": prompt}
#                 ]
#             }
#         ]
#     }

#     try:
#         response = requests.post(url, headers=headers, json=body)

#         if response.status_code != 200:
#             return f"Gemini API Error: {response.text}"

#         data = response.json()

#         return data["candidates"][0]["content"]["parts"][0]["text"]

#     except Exception as e:
#         return f"AI analysis failed: {str(e)}"