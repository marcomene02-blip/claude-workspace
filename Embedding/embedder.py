from __future__ import annotations
import hashlib
from dataclasses import dataclass
from pathlib import Path

from google.genai import types as genai_types

from config import gemini_client, EMBEDDING_MODEL, EMBEDDING_DIMENSION


@dataclass
class EmbeddingResult:
    vector: list[float]
    source_file: str
    content_type: str          # "text" | "image" | "video"
    segment_index: int = 0     # 0 for non-segmented; 0,1,2... for video segments
    description: str = ""
    text_content: str = ""     # original text (truncated) for RAG retrieval
    vector_id: str = ""


def _make_vector_id(filepath: str, segment: int = 0) -> str:
    """Deterministic ID from filepath + segment index."""
    raw = f"{filepath}::seg{segment}"
    return hashlib.sha256(raw.encode()).hexdigest()[:32]


def embed_text(text: str, *, source_file: str = "", task_type: str = "search_document") -> EmbeddingResult:
    """
    Embed a single text string.
    For ingestion use task_type="search_document"; for queries use "search_query".
    """
    prompt = f"task: {task_type} | content: {text}"

    response = gemini_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=prompt,
        config=genai_types.EmbedContentConfig(output_dimensionality=EMBEDDING_DIMENSION),
    )
    vector = response.embeddings[0].values

    return EmbeddingResult(
        vector=vector,
        source_file=source_file,
        content_type="text",
        segment_index=0,
        text_content=text[:2000],
        vector_id=_make_vector_id(source_file),
    )


def embed_image(image_path: str, *, description: str = "", task_type: str = "search_document") -> EmbeddingResult:
    """Embed a single image file (PNG or JPEG)."""
    path = Path(image_path)
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    image_bytes = path.read_bytes()

    parts = []
    if description:
        parts.append(genai_types.Part.from_text(f"task: {task_type} | description: {description}"))
    parts.append(genai_types.Part.from_bytes(data=image_bytes, mime_type=mime))

    response = gemini_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=genai_types.Content(parts=parts),
        config=genai_types.EmbedContentConfig(output_dimensionality=EMBEDDING_DIMENSION),
    )
    vector = response.embeddings[0].values

    return EmbeddingResult(
        vector=vector,
        source_file=image_path,
        content_type="image",
        segment_index=0,
        description=description,
        vector_id=_make_vector_id(image_path),
    )


def embed_video_segment(
    video_path: str,
    *,
    segment_index: int = 0,
    description: str = "",
    task_type: str = "search_document",
) -> EmbeddingResult:
    """Embed a single video segment (must be <= 120 seconds)."""
    path = Path(video_path)
    mime = "video/mp4" if path.suffix.lower() == ".mp4" else "video/quicktime"
    video_bytes = path.read_bytes()

    parts = []
    if description:
        parts.append(genai_types.Part.from_text(f"task: {task_type} | description: {description}"))
    parts.append(genai_types.Part.from_bytes(data=video_bytes, mime_type=mime))

    response = gemini_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=genai_types.Content(parts=parts),
        config=genai_types.EmbedContentConfig(output_dimensionality=EMBEDDING_DIMENSION),
    )
    vector = response.embeddings[0].values

    return EmbeddingResult(
        vector=vector,
        source_file=video_path,
        content_type="video",
        segment_index=segment_index,
        description=description,
        vector_id=_make_vector_id(video_path, segment_index),
    )
