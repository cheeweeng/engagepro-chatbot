from wiki.wikipedia_search import search_wikipedia


questions = [
    "Retrieval-Augmented Generation",
    "LangGraph",
    "Artificial Intelligence",
]

for question in questions:

    print("=" * 60)

    print(question)

    print("=" * 60)

    result = search_wikipedia(question)

    print(result)

    print()