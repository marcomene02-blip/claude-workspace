# Wiki Log

Append-only. Entry format: `## [YYYY-MM-DD] <op> | <title>`. Parseable with `grep "^## \[" wiki/log.md`.

## [2026-04-13] schema | wiki initialized
- Created `wiki/CLAUDE.md` schema with three-layer architecture (raw / pages / control).
- Created empty `wiki/index.md` catalog.
- Created `wiki/log.md` (this file).
- Created folder stubs: `raw/{articles,papers,notes,transcripts,images}`, `pages/{entities,concepts,topics,sources,analyses}`.
- Wiki ready for first ingest.

## [2026-04-14] create | Monitor CRM
- Criado `wiki/pages/analyses/crm-monitor/index.md` — índice de relatórios diários.
- Atualizado `wiki/index.md` com entrada em Analyses.
- Task agendada `monitor-crm` registrada no Claude Code Desktop (06:00 diário).
