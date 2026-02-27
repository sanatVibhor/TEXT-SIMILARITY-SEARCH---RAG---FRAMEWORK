from app.embedding_model import embed_texts
from app.vector_store import get_collection

def retrieve_similar(query: str, top_k: int = 3, threshold: float = 0.90):
    collection = get_collection()

    query_embedding = embed_texts([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    distances = results["distances"][0]
    print("Distances:", distances)
    # Convert distance to similarity (since using cosine)
    similarities = [1 - d for d in distances]

    # Filter by threshold
    filtered_docs = [
        doc for doc, sim in zip(documents, similarities)
        if sim >= threshold
    ]

    if not filtered_docs:
        return ["No relevant incidents found in the system."]

    return filtered_docs

if __name__ == "__main__":
    test_query = "power failure in transformer unit"
    results = retrieve_similar(test_query, top_k=3)

    print("\nQuery:", test_query)
    print("\nTop Matches:\n")

    for i, doc in enumerate(results, 1):
        print(f"{i}. {doc}")