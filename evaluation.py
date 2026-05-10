def precision_at_k(relevant, retrieved, k):

    retrieved_k = retrieved[:k]

    relevant_count = len(
        set(retrieved_k) & set(relevant)
    )

    return relevant_count / k

# Example
relevant = [
    "Java Backend Developer Assessment"
]

retrieved = [
    "Java Backend Developer Assessment",
    "Software Engineer Assessment"
]

print(
    "Precision@2:",
    precision_at_k(relevant, retrieved, 2)
)