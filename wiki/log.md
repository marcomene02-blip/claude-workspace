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

## [2026-04-14] refactor | backlog-melhorias — agentes grupo comercial
- Populadas 6 linhas de agentes (diretor-comercial, gerente-comercial, especialista-renovacao, especialista-seguro-novo, hunter-cross-sell, qualificador-leads)

## [2026-04-14] refactor | backlog-melhorias — agentes grupo marketing/conteúdo
- Populadas 4 linhas de agentes (cmo, analista-campanhas, criador-conteudo, especialista-inbound)
- cmo: skill segmentacao-carteira ausente + exit criteria de planejamento faltando
- analista-campanhas: threshold numérico de intervenção ausente + skill segmentacao-carteira faltando
- criador-conteudo: exemplos concretos de tom/voz ausentes + consulta CRM antes de criar conteúdo personalizado
- especialista-inbound: passo de registro Monday no handoff ausente + skill segmentacao-carteira faltando
- Summary e Key points atualizados para refletir 10 agentes com melhorias definidas
