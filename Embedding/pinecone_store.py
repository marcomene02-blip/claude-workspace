from __future__ import annotations
import os
import time as _time

from pinecone import ServerlessSpec

from config import pc_client, PINECONE_INDEX_NAME, EMBEDDING_DIMENSION, PINECONE_METRIC
from embedder import EmbeddingResult


def ensure_index() -> None:
    """Create the Pinecone index if it doesn't exist (serverless, free-tier compatible)."""
    existing = [idx.name for idx in pc_client.list_indexes()]
    if PINECONE_INDEX_NAME in existing:
        return

    pc_client.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=EMBEDDING_DIMENSION,
        metric=PINECONE_METRIC,
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    while not pc_client.describe_index(PINECONE_INDEX_NAME).status["ready"]:
        _time.sleep(1)


def get_index():
    """Return a handle to the index."""
    return pc_client.Index(PINECONE_INDEX_NAME)


def upsert_results(results: list[EmbeddingResult], batch_size: int = 100) -> int:
    """
    Upsert embedding results into Pinecone.

    Metadata per vector: content_type, filename, source_path,
    segment_index, description, timestamp.
    Returns the number of vectors upserted.
    """
    index = get_index()
    vectors = []
    for r in results:
        vectors.append({
            "id": r.vector_id,
            "values": r.vector,
            "metadata": {
                "content_type": r.content_type,
                "filename": os.path.basename(r.source_file),
                "source_path": r.source_file,
                "segment_index": r.segment_index,
                "description": r.description,
                "text_content": r.text_content[:2000],
                "timestamp": int(_time.time()),
            },
        })

    total = 0
    for i in range(0, len(vectors), batch_size):
        batch = vectors[i : i + batch_size]
        index.upsert(vectors=batch)
        total += len(batch)

    return total


def query_similar(
    query_vector: list[float],
    *,
    top_k: int = 5,
    content_type_filter: str | None = None,
) -> list[dict]:
    """Query the index for similar vectors. Returns list of {id, score, metadata}."""
    index = get_index()

    filter_dict = {}
    if content_type_filter:
        filter_dict["content_type"] = {"$eq": content_type_filter}

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True,
        filter=filter_dict or None,
    )

    return [
        {"id": m.id, "score": m.score, "metadata": m.metadata}
        for m in results.matches
    ]
