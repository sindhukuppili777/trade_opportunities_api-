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



