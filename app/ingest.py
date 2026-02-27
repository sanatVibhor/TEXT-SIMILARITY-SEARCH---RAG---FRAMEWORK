import pandas as pd
from app.embedding_model import embed_texts
from app.vector_store import get_collection


CSV_FILE = "data/incidents_semantic.csv"

def run_ingestion():
    print("Loading CSV...")
    df = pd.read_csv(CSV_FILE)

    assert "semantic_text" in df.columns

    texts = df["semantic_text"].tolist()

    print("Generating embeddings...")
    embeddings = embed_texts(texts)

    collection = get_collection()

    print("Inserting into ChromaDB...")

    ids = [str(i) for i in df.index]
    metadatas = [{"row_index": int(i)} for i in df.index]

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print("Ingestion completed.")
    print("Total records:", collection.count())


if __name__ == "__main__":
    run_ingestion()