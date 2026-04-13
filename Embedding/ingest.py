"""
CLI: Ingest files from a local directory into Pinecone.

Usage:
    python ingest.py /path/to/folder
    python ingest.py /path/to/folder --type image
    python ingest.py /path/to/folder --description "Product photos from Q1"
    python ingest.py /path/to/folder --recursive
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

from utils import detect_content_type, segment_video, read_text_file
from embedder import embed_text, embed_image, embed_video_segment, EmbeddingResult
from pinecone_store import ensure_index, upsert_results


def ingest_file(filepath: str, description: str = "") -> list[EmbeddingResult]:
    """Embed a single file. Returns list of EmbeddingResult (>1 for segmented video)."""
    ctype = detect_content_type(filepath)
    if ctype is None:
        print(f"  SKIP unsupported: {filepath}")
        return []

    results = []

    if ctype == "text":
        text = read_text_file(filepath)
        results.append(embed_text(text, source_file=filepath))

    elif ctype == "image":
        results.append(embed_image(filepath, description=description))

    elif ctype == "video":
        segments = segment_video(filepath)
        for seg in segments:
            r = embed_video_segment(
                seg["path"],
                segment_index=seg["index"],
                description=description,
            )
            r.source_file = filepath  # always point to original, not temp segment
            results.append(r)

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest files into Pinecone")
    parser.add_argument("folder", help="Path to folder containing files to ingest")
    parser.add_argument("--type", choices=["text", "image", "video"], default=None,
                        help="Only ingest files of this type")
    parser.add_argument("--description", default="",
                        help="Text description to attach to image/video embeddings")
    parser.add_argument("--recursive", action="store_true",
                        help="Recurse into subdirectories")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Error: {folder} is not a directory", file=sys.stderr)
        sys.exit(1)

    print("Ensuring Pinecone index exists...")
    ensure_index()

    pattern = "**/*" if args.recursive else "*"
    files = sorted(p for p in folder.glob(pattern) if p.is_file())

    all_results: list[EmbeddingResult] = []
    for f in files:
        filepath = str(f)
        ctype = detect_content_type(filepath)

        if args.type and ctype != args.type:
            continue

        print(f"  Embedding: {filepath} ({ctype})")
        try:
            results = ingest_file(filepath, description=args.description)
            all_results.extend(results)
        except Exception as e:
            print(f"  ERROR on {filepath}: {e}", file=sys.stderr)

    if all_results:
        count = upsert_results(all_results)
        print(f"\nDone. Upserted {count} vectors into Pinecone.")
    else:
        print("\nNo files were embedded.")


if __name__ == "__main__":
    main()
