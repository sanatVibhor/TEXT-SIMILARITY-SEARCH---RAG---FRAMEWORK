import chromadb
from chromadb.config import Settings

PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "incident_tickets"

_client = None
_collection = None

def get_collection():
    global _client, _collection

    if _client is None:
        _client = chromadb.Client(
            Settings(
                persist_directory=PERSIST_DIR,
                is_persistent=True
            )
        )

    if _collection is None:
        _collection = _client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )

    return _collection
