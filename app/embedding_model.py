from sentence_transformers import SentenceTransformer

MODEL_NAME = "thenlper/gte-small"

_model = None

def get_embedding_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(
            MODEL_NAME,
            device="cpu"  # switch to cuda if available
        )
    return _model


def embed_texts(texts):
    model = get_embedding_model()
    return model.encode(
        texts,
        batch_size=32,
        normalize_embeddings=True
    )