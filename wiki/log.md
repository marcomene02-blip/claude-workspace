# Wiki Log

Append-only. Entry format: `## [YYYY-MM-DD] <op> | <title>`. Parseable with `grep "^## \[" wiki/log.md`.

## [2026-04-19] ingest | Inteligência de Renovação — rotina criada
- Criado `menegon-seguros/agents/inteligencia-renovacao/AGENTS.md` — rotina diária 07:00 BRT, 8 passos.
- Criado `menegon-seguros/config/thresholds/inteligencia-renovacao.yaml` — janela 15d, tolerância 1d, LTV VIP R$15k, sinistros alerta ≥2.
- Criado `wiki/pages/analyses/inteligencia-renovacao-menegon/index.md` — índice da rotina.
- Atualizado `hub-state.json` — rotinas_ativas 12→13, nova rotina e agente adicionados.
- Atualizado `wiki/index.md` — entrada em Analyses.

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

## [2026-04-14] refactor | backlog-melhorias — skills grupo CRM e dados
- Populadas 5 linhas de skills (monday-crm-query, monday-crm-write, forecast-ponderado, analise-churn, analise-nps)
- monday-crm-query: formato de saída indefinido + exemplo de paginação GraphQL ausente para board Apólices
- monday-crm-write: retorno de sucesso/erro não padronizado + rollback parcial não documentado + movimentação de grupo ausente da lista de ações críticas
- forecast-ponderado: fonte da meta mensal não especificada + calibração histórica dos multiplicadores ausente + regra para deals mid-period indefinida
- analise-churn: dimensão Engajamento sem fonte de dados mapeada (last_updated_at) + join com Apólices para monoproduto não documentado + caso zero-críticos ausente do template de saída
- analise-nps: tamanho mínimo de amostra não definido (risco de NPS espúrio) + column ID de feedback textual não documentado + cálculo de prêmio anual para escalada a Marco não especificado
- Key points atualizado: 5 de 14 skills com melhorias definidas

## [2026-04-14] refactor | backlog-melhorias — skills grupo comercial/retenção
- Populadas 5 linhas de skills (auditoria-pipeline, cross-sell-hunt, plano-retencao, qualificacao-lead, abordagem-comercial)
- auditoria-pipeline: gatilho ausente + dimensão "distribuição equilibrada" sem critério numérico + fonte da Meta Mensal não especificada
- cross-sell-hunt: gatilho e cadência ausentes + probabilidades sem calibração histórica + lógica de rotação de clientes inexistente
- plano-retencao: gatilho ausente + SLA de aprovação do Marco indefinido para clientes Críticos + output não definido para causa raiz indeterminável
- qualificacao-lead: score não inteiro por critério de contato (0.5) inconsistente com faixas de classificação inteiras + score não gravado no Monday + campo de motivo de descarte não definido
- abordagem-comercial: gatilho ausente em todas as 5 situações de template + template de email prometido nas regras mas inexistente na SKILL.md + limite de caracteres WhatsApp ambíguo
- Key points atualizado: 10 de 14 skills com melhorias definidas; Summary da página atualizado

## [2026-04-14] refactor | backlog-melhorias — skills grupo conteúdo/crescimento
- Populadas 4 linhas de skills (analise-campanhas, nutricao-lead, criacao-conteudo, segmentacao-carteira)
- analise-campanhas: gatilho ausente + custo sem fonte/coluna definida + divisão por zero não tratada em ROI/CPL/taxa
- nutricao-lead: gatilho ausente + limite de ciclos de cadência indefinido (risco de loop infinito) + templates incompletos para 2 personas (dias 7/10/14 faltando)
- criacao-conteudo: gatilho e formato de saída ausentes + processo de aprovação de cases não documentado + faixa de preço no one-pager sem fonte de dados especificada
- segmentacao-carteira: gatilho ausente + sem fallback quando health score não calculado + Marco omitido da distribuição por corretor + "contato direto" sem definição operacional
- Key points atualizado: 14 de 14 skills com melhorias definidas — backlog de skills completo; Summary da página atualizado

## [2026-04-14] refactor | backlog-melhorias — revisão final e prioridades
- Verificado que todos os 33 ativos têm melhorias definidas
- Prioridades revisadas e consistentes

## [2026-04-15] refactor | analise-nps — amostra mínima, campo feedback, prêmio anual
- Adicionada seção de tamanho mínimo de amostra (< 5 respostas = AMOSTRA INSUFICIENTE)
- Campo de feedback textual documentado (text_mkrtez0s, board 9751082146)
- Regra de escalada para Marco com source do prêmio anual (numeric_mks5gh0b)
- Backlog: analise-nps marcado como Concluído

## [2026-04-15] refactor | backlog-melhorias — Fase 2 seções Quando usar
- 7 skills recebem seção ## Quando usar: auditoria-pipeline, cross-sell-hunt, plano-retencao, analise-campanhas, nutricao-lead, criacao-conteudo, segmentacao-carteira
- Todas marcadas como Concluído no backlog

## [2026-04-15] refactor | backlog-melhorias — Fase 3 qualificacao-lead e executor-retencao
- qualificacao-lead: score inteiro, Quando usar, registro obrigatório no Monday, campo de descarte
- executor-retencao: SLA 24h/72h, escalada [Aguardando Aprovação], skill nutricao-lead adicionada
- Ambos marcados como Concluído no backlog

## [2026-04-15] refactor | backlog-melhorias — Fase 4
- analista-churn: tendência de score (deterioração rápida) e exit criteria
- hunter-cross-sell: rubrica de probabilidade de fechamento
- monday-crm-query: formato list/summary e paginação com cursor
- forecast-ponderado: Quando usar, fonte da meta, MAPE, deals mid-period
- Todos marcados como Concluído no backlog

## [2026-04-14] refactor | Fase 5 onda 1 — 5 agentes melhorados

- cmo: skill segmentacao-carteira adicionada ao frontmatter + exit criteria de planejamento
- especialista-renovacao: nutricao-lead + score de urgência para cotações simultâneas
- especialista-seguro-novo: nutricao-lead para leads frios + passo 6a (status_handoff no CRM)
- analista-nps: gatilho mensal (Dia 1) + nutricao-lead para promotores
- analista-pipeline: escalada automática (48h → diretor) + critério de deal duplicado
- Todos marcados como Concluído no backlog

## [2026-04-15] refactor | Fase 5 onda 2 — 5 agentes melhorados

- especialista-inbound: passo 4b (status_nurturing + data_handoff via monday-crm-write) + skill segmentacao-carteira
- analista-performance: tabela de benchmarks por KPI (7 métricas com alerta) + passo 0 de rastreamento de recomendações pendentes
- gerente-comercial: fórmula de prioridade score=(30-dias)×prêmio + few-shot distribuição semanal + exit criteria do resumo ao diretor
- diretor-comercial: 4 exemplos few-shot (aprovação, ajuste, reprovação forecast, reprovação campanha)
- qualificador-leads: tabela BANT com pontuação numérica (máx 10 pts) + regra de registro do score no Monday
- Todos marcados como Concluído no backlog

## [2026-04-15] refactor | Fase 5 onda 3 — 5 ativos melhorados

- analise-churn SKILL: fonte de engajamento (last_updated_at) + join Apólices (9749857183) para monoproduto + template zero-críticos
- abordagem-comercial SKILL: seção Quando usar (5 cenários) + templates email renovação e cross-sell + limite 320 chars WhatsApp
- analista-campanhas AGENT: thresholds numéricos (ROI < 1,0 = pausar; conversão < 60% = alertar CMO) + skill segmentacao-carteira
- criador-conteudo AGENT: 4 exemplos few-shot (WhatsApp e email, certo/errado) + passo de monday-crm-query para conteúdo personalizado
- analista-forecast AGENT: regra de corte dia 15 para deals novos + referência MAPE + fonte da meta (doc_id 39560051)
- Todos marcados como Concluído no backlog — 100% de agentes e skills concluídos; apenas 6 itens de plugins restam (deferred)

## [2026-04-15] refactor | conexões — backlog-melhorias e crm-monitor no grafo
- backlog-melhorias.md: Connections populado com 6 wikilinks para [[sistema-agentes-menegon]], [[menegon-seguros]], [[time-comercial]], [[time-crm-fidelizacao]], [[time-marketing]], [[monday-crm]]; frontmatter updated bumped para 2026-04-15; linha adicionada ao Changelog
- crm-monitor/index.md: adicionada seção ## Connections com wikilinks para [[sistema-agentes-menegon]], [[monday-crm]], [[menegon-seguros]]; estava órfão antes; frontmatter updated bumped

## [2026-04-15] refactor | seeds — hub de agentes + 6 entidades + index atualizado
- Criada concepts/sistema-agentes-menegon.md: hub com tabelas de 17 agentes (papéis por núcleo) e 14 skills (por grupo); contradições de contagem de agents (16 vs 17) e skills (10 vs 14) registradas em Open questions; 4 conceitos sem fonte pendentes listados
- Criadas 6 entity pages: menegon-seguros, marco-menegon, monday-crm, time-comercial, time-crm-fidelizacao, time-marketing
- Atualizado index.md seções ## Entities e ## Concepts
- Dry-run de lint executado em chat antes do commit: nenhum key point sem citação, nenhum órfão novo, contradições preservadas, lacunas de conceitos registradas

## [2026-04-15] ingest | Menegon Seguros — COMPANY e 3 TEAMs
- Copiadas 4 fontes canônicas de menegon-seguros/ para wiki/raw/notes/ com prefixo 2026-04-15 e cabeçalho de origem
- Criadas 4 páginas em pages/sources/: menegon-company, team-comercial, team-crm-fidelizacao, team-marketing
- Atualizada seção ## Sources de wiki/index.md
- Contradição de contagem identificada: COMPANY.md descreve 15 agentes nos núcleos subordinados; backlog e filesystem apontam para 17 — registrada em Open questions de menegon-company.md; será filiada no hub em C3

## [2026-04-15] schema | Obsidian compatibility + content language
- CLAUDE.md: nova seção "Obsidian compatibility" permitindo wikilinks `[[slug]]` em Connections; citações de fontes em Key points permanecem `[slug]` (não `[[slug]]`)
- CLAUDE.md: documentadas settings recomendadas do Obsidian vault; attachment folder = `raw/images/`
- CLAUDE.md: nova seção "Content language" declarando pt-BR para pages/index/log e en para schema/meta
- .gitignore (raiz): adicionado `wiki/.obsidian/` para não versionar config local do vault

## [2026-04-16] query | Diagnóstico Completo de Vendas 2026-04
- Criado `wiki/pages/analyses/diagnostico-vendas-2026-04.md` — análise de 4 focos solicitada por Marco
- Fontes: Monday API (8 boards, snapshot vivo) + Quiver CSV (1.108 apólices) + documentação existente
- Páginas criadas: diagnostico-vendas-2026-04.md
- Dados coletados em: data/monday-snapshots/2026-04-16/, data/quiver-2026-04-16/, data/kpis/2026-04-16.json
- Atualizado wiki/index.md com entrada em Analyses
- 12 análises existentes referenciadas em Connections
- Alertas identificados: funil inbound inoperante, workflow renovação com falhas, concentração crítica Ester
- Quick wins: 8 itens com impacto×esforço | Roadmap: 3 epics por mês (Saneamento, Visibilidade, Escala)

## [2026-05-04] query | Briefing Semanal de Renovações 2026-W19
- Criado `wiki/pages/analyses/renovacao-weekly-briefing/2026-W19.md` — briefing automatizado da semana 19 (04/05 a 10/05/2026)
- Fonte: Monday board 9427535861 (Renovação), dados coletados via MCP às 07:00 BRT por `renovacao-weekly-briefing`
- 15 renovações ativas filtradas (zero fechadas); R$ 31.371,29 em risco; 5 com vencimento ≤ 3 dias sem cotação aberta
- Atualizado `wiki/index.md` com entrada em Analyses
