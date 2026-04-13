"""
CLI: Search the Pinecone vector DB and optionally get a RAG answer via OpenRouter.

Usage:
    python query.py "a cat sitting on a laptop"
    python query.py "quarterly revenue chart" --type image --top-k 3
    python query.py "summarize the keynote video" --rag --model google/gemini-2.5-flash
"""
from __future__ import annotations
import argparse
import sys

sys.stdout.reconfigure(encoding="utf-8")

from config import openrouter_client
from embedder import embed_text
from pinecone_store import ensure_index, query_similar


DEFAULT_RAG_MODEL = "google/gemini-2.5-flash"


def search(query_text: str, *, top_k: int = 5, content_type_filter: str | None = None) -> list[dict]:
    """Embed the query and return top-k similar results from Pinecone."""
    result = embed_text(query_text, task_type="search_query")
    return query_similar(result.vector, top_k=top_k, content_type_filter=content_type_filter)


def rag_answer(query_text: str, context_results: list[dict], *, model: str = DEFAULT_RAG_MODEL) -> str:
    """Send query + retrieved context to an OpenRouter LLM and return the answer."""
    context_parts = []
    for i, r in enumerate(context_results, 1):
        meta = r["metadata"]
        text = meta.get("text_content", "")
        desc = meta.get("description", "")
        context_parts.append(
            f"[{i}] type={meta['content_type']}, "
            f"file={meta['filename']}, "
            f"score={r['score']:.4f}"
            f"{f', description={desc}' if desc else ''}"
            f"{f', content={text}' if text else ''}"
        )
    context_block = "\n".join(context_parts)

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. Use the retrieved context below to "
                "answer the user's question. Cite sources by their index number. "
                "If the context is insufficient, say so."
            ),
        },
        {
            "role": "user",
            "content": f"Question: {query_text}\n\nRetrieved context:\n{context_block}",
        },
    ]

    response = openrouter_client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the multimodal vector DB")
    parser.add_argument("query", help="Natural language query")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--type", choices=["text", "image", "video"], default=None,
                        help="Filter results by content type")
    parser.add_argument("--rag", action="store_true",
                        help="Get a RAG-style answer from an LLM via OpenRouter")
    parser.add_argument("--model", default=DEFAULT_RAG_MODEL,
                        help=f"OpenRouter model for RAG (default: {DEFAULT_RAG_MODEL})")
    args = parser.parse_args()

    ensure_index()

    print(f"Searching for: {args.query}\n")
    matches = search(args.query, top_k=args.top_k, content_type_filter=args.type)

    if not matches:
        print("No results found.")
        return

    print(f"Top {len(matches)} results:")
    for i, m in enumerate(matches, 1):
        meta = m["metadata"]
        print(f"  {i}. [{meta['content_type']}] {meta['filename']} (score: {m['score']:.4f})")

    if args.rag:
        print("\n--- RAG Answer ---")
        answer = rag_answer(args.query, matches, model=args.model)
        print(answer)


if __name__ == "__main__":
    main()
