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

## [2026-04-14] refactor | backlog-melhorias — agentes grupo análise e monitoramento
- Populadas 7 linhas de agentes (analista-churn, executor-retencao, analista-forecast, monitor-crm, analista-nps, analista-pipeline, analista-performance)
- analista-churn: rastreamento de tendência de health score (queda ≥15 pts em 7 dias) ausente + exit criteria do relatório indefinido
- executor-retencao: SLA de aprovação do Marco indefinido — clientes Críticos ficam sem escalada automática; skill nutricao-lead faltando para clientes Em Risco
- analista-forecast: MAPE nunca calculado, calibração dos multiplicadores sem base histórica; deals mid-week sem regra de inclusão definida
- monitor-crm: skill monday-crm-write ausente impede criar alertas no Monday; health score duplicado com analista-churn, frágil a mudanças de peso
- analista-nps: gatilho reativo sem cadência mínima garantida; skill nutricao-lead faltando para fluxo de referral de promotores
- analista-pipeline: escalada quando threshold violado sem prazo definido; critério de duplicata não especificado
- analista-performance: KPIs sem faixas de referência objetivas; recomendações anteriores nunca verificadas antes de novas
- Summary, Key points e Changelog da página atualizados; todos os 17 agentes têm melhorias documentadas
