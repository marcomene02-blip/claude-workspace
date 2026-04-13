"""
Chat web app — search Pinecone for context, answer with Claude Sonnet via OpenRouter.

Usage:
    python app.py
    Then open http://localhost:5000
"""
from __future__ import annotations
import sys

sys.stdout.reconfigure(encoding="utf-8")

from flask import Flask, render_template, request, jsonify
from config import openrouter_client
from embedder import embed_text
from pinecone_store import ensure_index, query_similar

app = Flask(__name__)

CHAT_MODEL = "nvidia/nemotron-3-super-120b-a12b:free"
SYSTEM_PROMPT = (
    "You are a helpful assistant with access to a knowledge base. "
    "Use the retrieved context below to answer the user's question. "
    "Cite sources by their filename when relevant. "
    "If the context doesn't contain enough information, say so honestly "
    "and answer from your general knowledge, noting the distinction."
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # 1. Embed the query and search Pinecone
    query_result = embed_text(user_message, task_type="search_query")
    matches = query_similar(query_result.vector, top_k=5)

    # 2. Build context block from results
    context_parts = []
    for i, m in enumerate(matches, 1):
        meta = m["metadata"]
        text = meta.get("text_content", "")
        desc = meta.get("description", "")
        entry = f"[{i}] file={meta['filename']}, type={meta['content_type']}, score={m['score']:.4f}"
        if desc:
            entry += f", description={desc}"
        if text:
            entry += f"\nContent: {text}"
        context_parts.append(entry)

    context_block = "\n\n".join(context_parts) if context_parts else "No relevant context found."

    # 3. Call Claude Sonnet via OpenRouter
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"{user_message}\n\n---\nRetrieved context:\n{context_block}",
        },
    ]

    response = openrouter_client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages,
    )
    answer = response.choices[0].message.content

    # 4. Return answer + sources
    sources = [
        {
            "filename": m["metadata"]["filename"],
            "type": m["metadata"]["content_type"],
            "score": round(m["score"], 4),
        }
        for m in matches
    ]

    return jsonify({"answer": answer, "sources": sources})


if __name__ == "__main__":
    print("Ensuring Pinecone index exists...")
    ensure_index()
    print(f"Chat model: {CHAT_MODEL}")
    print("Starting server at http://localhost:5000")
    app.run(debug=True, port=5000)
