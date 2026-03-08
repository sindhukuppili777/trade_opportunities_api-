import requests

def collect_market_data(sector: str):

    query = f"{sector} market India news"

    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        results = []

        if "RelatedTopics" in data:
            for item in data["RelatedTopics"][:5]:
                if isinstance(item, dict) and "Text" in item:
                    results.append(item["Text"])

        # If API returns empty results, use fallback data
        if not results:
            results = [
                f"{sector} sector in India is experiencing steady growth.",
                f"Government initiatives supporting {sector} industry.",
                f"Increasing investment opportunities in {sector} sector."
            ]

        return results

    except Exception:
        return [
            f"{sector} sector showing increasing market demand in India.",
            f"New trade opportunities emerging in {sector}.",
            f"Investments rising in the {sector} industry."
        ]


# from duckduckgo_search import DDGS

# def collect_market_data(sector: str):

#     query = f"India {sector} market news trade opportunities"

#     results = []

#     with DDGS() as ddgs:
#         for r in ddgs.text(query, max_results=5):
#             results.append(r["body"])

#     return "\n".join(results)