---
title: Monitor CRM — Índice
type: analysis
created: 2026-04-14
updated: 2026-04-15
sources: []
tags: [monday, crm, monitor, alertas]
---

## Resumo

Relatórios diários do monitor-crm. Gerados automaticamente às 06:00 pela task agendada `monitor-crm`. Cada linha representa um dia de monitoramento.

## Relatórios

| Data | Status | Alertas |
|------|--------|---------|
| [2026-04-14](2026-04-14.md) | critico | Renovações crítico (2 apólices vencendo amanhã, ≥26 nos próximos 7 dias); Pipeline crítico (≥5 deals parados); NPS alerta (1 detrator sem atualização há 238 dias); Churn alerta (4 sinistros PENDENTE); Automações alerta; Forecast alerta (sem meta). |
| _aguardando próxima execução_ | — | — |

## Connections

- [[sistema-agentes-menegon]] — agente `monitor-crm` faz parte do sistema (17º agente, sem TEAM.md associado)
- [[monday-crm]] — fonte de dados de todos os relatórios (boards: renovacao, pipeline, NPS, churn, forecast)
- [[menegon-seguros]] — empresa cujas métricas operacionais são monitoradas aqui

## Changelog

- 2026-04-14 — criado como índice do monitor-crm.
- 2026-04-14 — primeiro relatório diário registrado (status: critico).
- 2026-04-15 — adicionada seção Connections para integrar ao grafo da wiki.
