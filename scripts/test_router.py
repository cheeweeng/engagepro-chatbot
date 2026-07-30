from routing.router import classify_question

questions = [
    "What is EngagePro's mission?",
    "Summarise the company vision.",
    "What AI solutions does EngagePro provide?",
    "Explain Retrieval-Augmented Generation.",
    "Who won the FIFA World Cup in 2022?",
]

for question in questions:

    category = classify_question(question)

    print(f"{question}")

    print(f"→ {category}")

    print("-" * 60)