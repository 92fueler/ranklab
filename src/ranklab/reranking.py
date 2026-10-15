"""Basic model reranking with scores aligned to the input document order.

This is an extracted model adapter, not an eligibility policy or tuned ranker.
"""

from .settings import required_env
import math


def _get_score(item):
    # Newer SDKs expose `relevance_score`; some examples use `score`.
    for attr in ("relevance_score", "score", "relevance"):
        if hasattr(item, attr):
            val = getattr(item, attr)
            try:
                score = float(val)
            except (TypeError, ValueError) as exc:
                raise ValueError("Reranker returned a nonnumeric score") from exc
            if not math.isfinite(score):
                raise ValueError("Reranker returned a nonfinite score")
            return score
    raise ValueError("Reranker result is missing its score")

def rerank_pairs(query_text: str, docs: list[str]) -> list[float]:
    """
    Returns scores aligned with `docs` order using Voyage reranker.
    """
    if not docs:
        return []
    if not isinstance(query_text, str) or not query_text.strip():
        raise ValueError("Reranking query must be a nonempty string")
    if not isinstance(docs, list) or any(not isinstance(doc, str) for doc in docs):
        raise ValueError("Reranking documents must be a list of strings")

    import voyageai

    client = voyageai.Client(api_key=required_env("VOYAGE_API_KEY"), timeout=60)
    rr = client.rerank(
        query=query_text, documents=docs, model=required_env("VOYAGE_RERANK_MODEL")
    )

    # Incomplete responses must not silently turn into zero scores.
    score_by_idx = {}
    for result in rr.results:
        index = result.index
        if (isinstance(index, bool) or not isinstance(index, int)
                or not 0 <= index < len(docs) or index in score_by_idx):
            raise ValueError("Reranker returned invalid or duplicate document indices")
        score_by_idx[index] = _get_score(result)
    if len(score_by_idx) != len(docs):
        raise ValueError("Reranker did not return one score per document")
    return [score_by_idx[i] for i in range(len(docs))]
