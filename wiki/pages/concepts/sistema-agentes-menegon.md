---
title: Sistema de Agentes — Menegon Seguros
type: concept
created: 2026-04-15
updated: 2026-04-15
sources: [menegon-company, team-comercial, team-crm-fidelizacao, team-marketing]
tags: [agentes, skills, sistema, paperclip, agentcompanies]
---

## Summary

O sistema de agentes da Menegon Seguros é composto por 17 agentes e 14 skills organizados em 4 núcleos operacionais (Comercial, CRM & Fidelização, Marketing, Operacional) mais o Diretor Comercial como agente-raiz. Os agentes cobrem vendas, renovação, retenção, cross-sell, marketing e diagnóstico operacional. As skills são procedimentos reutilizáveis que os agentes invocam para executar tarefas específicas — consultas ao CRM, análises e geração de conteúdo. O sistema é descrito no formato Agent Companies spec v1 e gerenciado via Paperclip.

## Key points

- 4 núcleos: Comercial (5 agentes), CRM & Fidelização (3), Marketing (4), Operacional (3); mais o Diretor Comercial no topo = 16 documentados nos TEAMs [menegon-company]
- O agente `monitor-crm` existe no filesystem (`menegon-seguros/agents/monitor-crm/`) e é citado no backlog como o 17º agente, mas não aparece em nenhum TEAM.md nem na estrutura do COMPANY.md [menegon-company]
- 14 skills registradas no filesystem; README.md lista apenas 10 — as 4 adicionais (analise-nps, nutricao-lead, criacao-conteudo, segmentacao-carteira) foram adicionadas após a documentação do README [menegon-company]
- Todos os agentes usam Monday CRM (workspace 11267903) como fonte de verdade [menegon-company]
- Aprovação humana do Marco é obrigatória para ações críticas (planos de recuperação, registros no CRM, campanhas) [menegon-company]

## Tabela de Agentes

| Agente | Núcleo | Papel principal | Fonte individual |
|---|---|---|---|
| diretor-comercial | Raiz | Aprovador final, coordenação estratégica [menegon-company] | [AGENTS.md](../../../../menegon-seguros/agents/diretor-comercial/AGENTS.md) |
| gerente-comercial | Comercial | Coordenação e distribuição de prioridades [team-comercial] | [AGENTS.md](../../../../menegon-seguros/agents/gerente-comercial/AGENTS.md) |
| especialista-renovacao | Comercial | Renovar carteira ativa (1ª prioridade) [team-comercial] | [AGENTS.md](../../../../menegon-seguros/agents/especialista-renovacao/AGENTS.md) |
| especialista-seguro-novo | Comercial | Fechar novos negócios (2ª prioridade) [team-comercial] | [AGENTS.md](../../../../menegon-seguros/agents/especialista-seguro-novo/AGENTS.md) |
| hunter-cross-sell | Comercial | Expandir produtos por cliente (3ª prioridade) [team-comercial] | [AGENTS.md](../../../../menegon-seguros/agents/hunter-cross-sell/AGENTS.md) |
| qualificador-leads | Comercial | Filtrar e priorizar leads (suporte) [team-comercial] | [AGENTS.md](../../../../menegon-seguros/agents/qualificador-leads/AGENTS.md) |
| analista-churn | CRM & Fidelização | Detecta risco de perda antes que aconteça [team-crm-fidelizacao] | [AGENTS.md](../../../../menegon-seguros/agents/analista-churn/AGENTS.md) |
| executor-retencao | CRM & Fidelização | Constrói e executa planos de recuperação [team-crm-fidelizacao] | [AGENTS.md](../../../../menegon-seguros/agents/executor-retencao/AGENTS.md) |
| analista-nps | CRM & Fidelização | Transforma satisfação em ação [team-crm-fidelizacao] | [AGENTS.md](../../../../menegon-seguros/agents/analista-nps/AGENTS.md) |
| cmo | Marketing | Define estratégia, OKRs e alocação de esforço [team-marketing] | [AGENTS.md](../../../../menegon-seguros/agents/cmo/AGENTS.md) |
| analista-campanhas | Marketing | Executa, monitora e otimiza campanhas ativas [team-marketing] | [AGENTS.md](../../../../menegon-seguros/agents/analista-campanhas/AGENTS.md) |
| criador-conteudo | Marketing | Produz materiais, scripts e posts [team-marketing] | [AGENTS.md](../../../../menegon-seguros/agents/criador-conteudo/AGENTS.md) |
| especialista-inbound | Marketing | Atrai e nutre leads digitais até estarem prontos para vendas [team-marketing] | [AGENTS.md](../../../../menegon-seguros/agents/especialista-inbound/AGENTS.md) |
| analista-pipeline | Operacional | — (pendente ingest de AGENTS.md) | [AGENTS.md](../../../../menegon-seguros/agents/analista-pipeline/AGENTS.md) |
| analista-forecast | Operacional | — (pendente ingest de AGENTS.md) | [AGENTS.md](../../../../menegon-seguros/agents/analista-forecast/AGENTS.md) |
| analista-performance | Operacional | — (pendente ingest de AGENTS.md) | [AGENTS.md](../../../../menegon-seguros/agents/analista-performance/AGENTS.md) |
| monitor-crm | — (não documentado em TEAM) | — (pendente ingest de AGENTS.md) | [AGENTS.md](../../../../menegon-seguros/agents/monitor-crm/AGENTS.md) |

## Tabela de Skills

| Skill | Grupo | Propósito | Fonte individual |
|---|---|---|---|
| monday-crm-query | CRM e dados | Consultar dados do Monday CRM | [SKILL.md](../../../../menegon-seguros/skills/monday-crm-query/SKILL.md) |
| monday-crm-write | CRM e dados | Registrar updates e notificações no Monday | [SKILL.md](../../../../menegon-seguros/skills/monday-crm-write/SKILL.md) |
| forecast-ponderado | CRM e dados | Calcular forecast com 3 cenários | [SKILL.md](../../../../menegon-seguros/skills/forecast-ponderado/SKILL.md) |
| analise-churn | CRM e dados | Score de risco por cliente | [SKILL.md](../../../../menegon-seguros/skills/analise-churn/SKILL.md) |
| analise-nps | CRM e dados | Calcular e interpretar NPS da carteira | [SKILL.md](../../../../menegon-seguros/skills/analise-nps/SKILL.md) |
| auditoria-pipeline | Comercial/retenção | Health check do pipeline comercial | [SKILL.md](../../../../menegon-seguros/skills/auditoria-pipeline/SKILL.md) |
| cross-sell-hunt | Comercial/retenção | Identificar gaps de produto em clientes ativos | [SKILL.md](../../../../menegon-seguros/skills/cross-sell-hunt/SKILL.md) |
| plano-retencao | Comercial/retenção | Gerar plano de recuperação de cliente em risco | [SKILL.md](../../../../menegon-seguros/skills/plano-retencao/SKILL.md) |
| qualificacao-lead | Comercial/retenção | Pontuar e priorizar leads (0–10) | [SKILL.md](../../../../menegon-seguros/skills/qualificacao-lead/SKILL.md) |
| abordagem-comercial | Comercial/retenção | Gerar script de abordagem por situação | [SKILL.md](../../../../menegon-seguros/skills/abordagem-comercial/SKILL.md) |
| analise-campanhas | Conteúdo/crescimento | Calcular KPIs de campanha (ROI, CPL, conversão) | [SKILL.md](../../../../menegon-seguros/skills/analise-campanhas/SKILL.md) |
| nutricao-lead | Conteúdo/crescimento | Cadência de nutrição de leads por persona | [SKILL.md](../../../../menegon-seguros/skills/nutricao-lead/SKILL.md) |
| criacao-conteudo | Conteúdo/crescimento | Gerar materiais e posts para canais definidos | [SKILL.md](../../../../menegon-seguros/skills/criacao-conteudo/SKILL.md) |
| segmentacao-carteira | Conteúdo/crescimento | Segmentar clientes para ações de marketing e retenção | [SKILL.md](../../../../menegon-seguros/skills/segmentacao-carteira/SKILL.md) |

## Connections

- [[menegon-seguros]] — empresa que opera este sistema
- [[marco-menegon]] — Diretor Comercial; aprovador final de ações críticas
- [[monday-crm]] — fonte de verdade compartilhada por todos os agentes
- [[time-comercial]] — Núcleo Comercial (5 agentes)
- [[time-crm-fidelizacao]] — Núcleo CRM & Fidelização (3 agentes)
- [[time-marketing]] — Núcleo Marketing (4 agentes)

## Open questions

- **Contradição de contagem de agentes**: COMPANY.md lista 15 agentes nos núcleos subordinados; contando o Diretor Comercial na raiz são 16 [menegon-company]. O filesystem tem 17 (inclui `monitor-crm`). O backlog-melhorias afirma "17 de 17 agentes" [backlog-melhorias]. O `monitor-crm` não aparece em nenhum TEAM.md nem na estrutura organizacional do COMPANY.md — foi adicionado depois? Reconciliar.
- **Contradição de contagem de skills**: README.md lista 10 skills; filesystem tem 14; backlog afirma "14 de 14". As 4 não documentadas no README são: analise-nps, nutricao-lead, criacao-conteudo, segmentacao-carteira. Atualizar README ou aceitar que está desatualizado.
- **Núcleo Operacional sem TEAM.md**: Analista de Pipeline, Analista de Forecast e Analista de Performance aparecem em COMPANY.md como "Núcleo Operacional" [menegon-company] mas não existe `teams/operacional/TEAM.md`. Os 3 agentes têm AGENTS.md individuais mas sem team doc de contexto.
- **Conceitos sem página própria**: health score, forecast ponderado, BANT (qualificação de leads), ciclo de renovação — mencionados no backlog e nas skills mas sem page dedicada. Requer ingest das skills correspondentes.

## Changelog

- 2026-04-15 — criada como hub do sistema de agentes; tabelas de 17 agentes e 14 skills; contradições de contagem registradas em Open questions
