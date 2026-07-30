"""
Wikipedia search utilities.

Uses the official Wikipedia REST API.
"""
import re
import requests

USER_AGENT = (
    "EngageProChatbot/1.0 (Ngee Ann Polytechnic LLMA Student Project)"
)

def retrieve_wikipedia_summary(query: str) -> str:
    """
    Search Wikipedia using a natural-language query and
    return the summary of the best matching article.
    """
    query = clean_query(query)

    headers = {
        "User-Agent": USER_AGENT
    }

    try:
        # Step 1: Search for the best matching article
        search_url = (
            "https://en.wikipedia.org/w/api.php"
        )

        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
        }

        search_response = requests.get(
            search_url,
            params=search_params,
            headers=headers,
            timeout=10,
        )

        search_response.raise_for_status()

        search_results = search_response.json()

        hits = search_results["query"]["search"]

        if not hits:
            return (
                "No relevant Wikipedia article was found for this topic.\n\n"
                "Do not answer using your own knowledge."
            )

        title = hits[0]["title"]

        # print(f"Search query : {query}")
        # print(f"Matched title: {title}")

        # Step 2: Retrieve the article summary
        summary_url = (
            "https://en.wikipedia.org/api/rest_v1/"
            f"page/summary/{title.replace(' ', '_')}"
        )

        summary_response = requests.get(
            summary_url,
            headers=headers,
            timeout=10,
        )

        summary_response.raise_for_status()

        data = summary_response.json()

        return data.get(
            "extract",
            "No summary available."
        )

    except Exception as error:

        return f"Wikipedia search failed: {error}"


def clean_query(query: str) -> str:
    """
    Convert a natural-language question into a Wikipedia search query.
    """

    query = query.strip()

    prefixes = [
        "what is",
        "what are",
        "who is",
        "who are",
        "explain",
        "define",
        "describe",
        "tell me about",
        "give me an overview of",
        "can you explain",
        "can you describe",]

    lower = query.lower()

    for prefix in prefixes:
        if lower.startswith(prefix):
            query = query[len(prefix):].strip()
            break

    query = re.sub(r"[?.!,]+$", "", query)

    return query