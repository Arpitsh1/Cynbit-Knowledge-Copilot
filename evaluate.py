
from knowledge import load_documents, retrieve


TESTS = [
    (
        "What services does Cynbit offer?",
        {"cynbit_services.txt"}
    ),
    (
        "What is Revio AI?",
        {"cynbit_products.txt"}
    ),
    (
        "How can I contact Cynbit?",
        {"cynbit_contact.txt"}
    ),
    (
        "Does Cynbit work on AI agents?",
        {"cynbit_services.txt"}
    ),
    (
        "What is TenantEase?",
        {"cynbit_products.txt"}
    )
]


def main():

    records = load_documents()

    hits = 0
    reciprocal_ranks = []

    for question, relevant_sources in TESTS:

        results = retrieve(
            question,
            records,
            top_k=3
        )

        ranked_sources = [
            result["source"]
            for result in results
        ]

        found = any(
            source in relevant_sources
            for source in ranked_sources
        )

        hits += int(found)

        reciprocal_rank = next(
            (
                1 / (index + 1)
                for index, source in enumerate(ranked_sources)
                if source in relevant_sources
            ),
            0
        )

        reciprocal_ranks.append(reciprocal_rank)

        print("Question:", question)
        print("Retrieved:", ranked_sources)
        print("Relevant document found:", found)
        print("-" * 50)

    recall_at_3 = hits / len(TESTS)

    mrr = sum(reciprocal_ranks) / len(TESTS)

    print("\nEvaluation Results")

    print(f"Recall@3: {recall_at_3:.3f}")

    print(f"MRR: {mrr:.3f}")

    print(
        "\nNote: This is a five-question smoke test, "
        "not a reliable production benchmark."
    )


if __name__ == "__main__":
    main()
