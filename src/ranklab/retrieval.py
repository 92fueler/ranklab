"""Query embedding and shortlist retrieval from the shared reference pattern.

The query model must match the document embeddings in the configured index.
No ingestion, filters, ranking heuristics, or fabricated IDs are included.
"""

from .settings import required_env
import math


def embed_query(text: str) -> list[float]:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Query text must be a nonempty string")
    import voyageai

    client = voyageai.Client(api_key=required_env("VOYAGE_API_KEY"), timeout=60)
    response = client.embed([text], model=required_env("VOYAGE_MODEL"), input_type="query")
    if len(response.embeddings) != 1:
        raise ValueError("Embedding service must return one query vector")
    embedding = response.embeddings[0]
    _validate_vector(embedding)
    return embedding


def _validate_vector(embedding: list[float]) -> None:
    if not isinstance(embedding, list) or not embedding:
        raise ValueError("Query vector must be a nonempty list of finite numbers")
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x)
           for x in embedding):
        raise ValueError("Query vector must contain finite numbers")
    if not any(embedding):
        raise ValueError("Query vector must not be all zeros")


def ann_query(embedding: list[float], top_k: int = 200):
    _validate_vector(embedding)
    if isinstance(top_k, bool) or not isinstance(top_k, int) or not 1 <= top_k <= 10000:
        raise ValueError("top_k must be an integer between 1 and 10000")
    import turbopuffer

    with turbopuffer.Turbopuffer(
        api_key=required_env("TURBOPUFFER_API_KEY"),
        region=required_env("TPUF_REGION"),
        timeout=60,
    ) as client:
        namespace = client.namespace(required_env("TPUF_NAMESPACE"))
        return namespace.query(
            rank_by=("vector", "ANN", embedding),
            top_k=top_k,
            include_attributes=True,
        )
