# Wiki Schema — LLM Wiki Agent Rules

This file is the operating contract for the LLM agent maintaining this wiki. The agent owns every file under `wiki/` **except** `wiki/raw/`. The human owns `wiki/raw/` and this schema file.

## Three layers

1. **Raw sources** — `wiki/raw/`. Immutable. Read-only for the agent. One subfolder per source type (`articles/`, `papers/`, `notes/`, `transcripts/`, `images/`). Each source keeps its original filename plus a short slug.
2. **Wiki pages** — `wiki/pages/`. Agent-owned. Structured, interlinked markdown. Subdivided into:
   - `pages/entities/` — people, companies, products, places. One page per entity.
   - `pages/concepts/` — ideas, techniques, frameworks, patterns.
   - `pages/topics/` — broad themes that tie entities and concepts together.
   - `pages/sources/` — one summary page per ingested raw source.
   - `pages/analyses/` — agent outputs from queries the human asked to file back (comparisons, deep dives, decks).
3. **Control files** — `wiki/index.md`, `wiki/log.md`, this `CLAUDE.md`. Agent updates index and log; human and agent co-evolve CLAUDE.md.

## Page format

Every page in `pages/` starts with YAML frontmatter:

```yaml
---
title: Canonical Page Title
type: entity | concept | topic | source | analysis
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug-1, source-slug-2]
tags: [tag1, tag2]
---
```

Body uses:
- `## Summary` — 2–5 sentences, the TL;DR.
- `## Key points` — bulleted facts, each with a `[source-slug]` citation.
- `## Connections` — links to related pages using markdown links `[Page](../concepts/page.md)`.
- `## Open questions` — what's unresolved or contradictory.
- `## Changelog` — dated one-liners: `- 2026-04-13 — created from article-xyz`.

Cross-references use relative markdown links. Slugs are `kebab-case`. Filenames match slugs.

## index.md conventions

`wiki/index.md` is a catalog, not a narrative. Sections: `## Entities`, `## Concepts`, `## Topics`, `## Sources`, `## Analyses`. Each line: `- [Title](pages/entities/slug.md) — one-line summary`. Agent rewrites the relevant section on every ingest. Keep under ~500 lines; split into sub-indexes if it grows past that.

## log.md conventions

`wiki/log.md` is append-only. Every entry starts with the prefix:

```
## [YYYY-MM-DD] <op> | <short title>
```

Where `<op>` is one of: `ingest`, `query`, `lint`, `refactor`, `schema`. Body is 1–5 bullet lines describing what changed and which pages were touched. Never rewrite history; only append. Parseable with `grep "^## \[" wiki/log.md`.

## Workflows

### Ingest (human drops a source, asks me to process)
1. Confirm the source path under `wiki/raw/`. If the human pasted text or a URL, save it first as a `.md` file in the right `raw/` subfolder with a kebab-case slug.
2. Read the full source. Summarize the key takeaways back to the human in chat (3–6 bullets).
3. Ask the human what to emphasize or skip before writing pages. Default to proceeding if they already gave direction.
4. Create `pages/sources/<slug>.md` with the frontmatter + summary + key points + a link back to the raw file.
5. For each entity, concept, or topic mentioned: create the page if missing, or update it in place — add facts under `## Key points` with citations, update `## Connections`, bump `updated:`, append a line to `## Changelog`.
6. If new data contradicts an existing claim, do NOT silently overwrite. Keep both under `## Open questions` with both source citations and flag it to the human.
7. Update `wiki/index.md` — add the new source line, add any new entity/concept/topic lines.
8. Append an entry to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>` with a bullet list of pages touched.
9. Report back to the human: source summary link, list of pages created/updated, any contradictions found.

### Query (human asks a question)
1. Read `wiki/index.md` first to identify candidate pages.
2. Read the candidate pages. If the wiki lacks coverage, say so explicitly — don't hallucinate.
3. Answer with citations using the `[source-slug]` format, with links to the wiki pages consulted.
4. Ask the human: "File this answer as an analysis page?" If yes, write it to `pages/analyses/<slug>.md` and update index + log.

### Lint (human asks for a health check, or periodically)
1. Scan `pages/` for: contradictions, stale claims, orphan pages (no inbound links), concepts mentioned but lacking their own page, missing cross-references, data gaps.
2. Report findings as a prioritized list. Do NOT fix silently — propose fixes, wait for human approval, then execute.
3. Append a `lint` entry to `log.md` summarizing what was found and what was fixed.

### Refactor
Moving or renaming pages, splitting one page into several, merging duplicates. Always update inbound links in the same pass. Log it.

## Hard rules

1. **Never modify files under `wiki/raw/`.** Read-only.
2. **Never invent facts.** Every claim in a `## Key points` bullet needs a `[source-slug]` citation pointing to an existing source page.
3. **Never delete a page without asking.** Propose, wait, then delete.
4. **Never batch-ingest silently.** If the human drops 10 sources, process them one by one and check in, unless they explicitly said "batch".
5. **Every write touches the log.** If you edit a page, the log gets an entry. No exceptions.
6. **Contradictions are preserved, not resolved.** The wiki records conflicts; the human decides which source to trust.
7. **Index and log stay current.** After any page write, update `index.md` if structure changed and append to `log.md`.
8. **Citations use slugs, not titles.** `[menegon-website-brief]` not `[Menegon Website Brief]`.

## Obsidian compatibility

This wiki is designed to be opened as an Obsidian vault (point Obsidian at `wiki/`).

- Wikilinks `[[page-slug]]` are allowed in `## Connections` sections as an alternative to markdown links `[Title](../path/page.md)`. Use whichever is clearer.
- **Source citations in `## Key points` stay as `[source-slug]` (bare brackets, single pair)** — this keeps citations visually distinct from wiki cross-references and keeps the parseable citation grep working.
- Recommended Obsidian settings: Files & Links → New link format = "Shortest path when possible"; Use `[[Wikilinks]]` = on; Default location for new attachments = `raw/images`.
- The agent does not commit `.obsidian/` vault config — it is listed in `.gitignore`. Obsidian regenerates it on first open.
- Attachment convention: images pasted or downloaded via Obsidian land in `raw/images/`. They are raw sources under the immutability rule.

## Content language

- **Wiki pages (`pages/**`), `index.md`, and `log.md`**: Portuguese (pt-BR). Matches the Menegon Seguros domain and all canonical sources.
- **This schema (`CLAUDE.md`) and `raw/README.md`**: English. These are control/meta files.
- Raw sources keep their original language.

## Out of scope (for now)

- Embeddings / vector search — the index is enough at this scale.
- Automatic web fetching on ingest — the human curates what enters `raw/`.
- Multiple wikis in one folder — one wiki per `wiki/` directory. Fork the folder if you need a second domain.

## Co-evolution

This schema is not frozen. When the human and agent discover a better convention, update this file and log a `schema` entry. Keep the old rule in `## Changelog` at the bottom of this file so we remember why things changed.

## Changelog

- 2026-04-13 — initial schema created.
- 2026-04-15 — added Obsidian compatibility section, wikilinks allowed in Connections, declared pt-BR as content language.
