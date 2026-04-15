# Wiki Log

Append-only. Entry format: `## [YYYY-MM-DD] <op> | <title>`. Parseable with `grep "^## \[" wiki/log.md`.

## [2026-04-13] schema | wiki initialized
- Created `wiki/CLAUDE.md` schema with three-layer architecture (raw / pages / control).
- Created empty `wiki/index.md` catalog.
- Created `wiki/log.md` (this file).
- Created folder stubs: `raw/{articles,papers,notes,transcripts,images}`, `pages/{entities,concepts,topics,sources,analyses}`.
- Wiki ready for first ingest.

## [2026-04-14] ingest | Monitor CRM
- Criado `wiki/pages/analyses/crm-monitor/index.md` — índice de relatórios diários.
- Atualizado `wiki/index.md` com entrada em Analyses.

## [2026-04-14] refactor | backlog-melhorias criado sem frontmatter
- Adicionado YAML frontmatter ao `pages/topics/backlog-melhorias.md`
- Adicionadas seções obrigatórias (Summary, Key points, Connections, Open questions, Changelog)
- Adicionada entrada no índice `wiki/index.md`
