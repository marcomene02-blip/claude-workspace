---
title: Time CRM & Fidelização (Núcleo CRM & Fidelização)
type: entity
created: 2026-04-15
updated: 2026-04-15
sources: [team-crm-fidelizacao, menegon-company]
tags: [time, crm, fidelizacao, churn, retencao, nps, ltv]
---

## Summary

O Núcleo CRM & Fidelização protege a receita recorrente da Menegon Seguros. Enquanto o Comercial busca novas receitas, este núcleo garante que a base existente não se perca. Opera com um fluxo sequencial obrigatório de detecção → plano → aprovação do Marco → execução → monitoramento.

## Key points

- Composto por 3 agentes: Analista de Churn (detecta risco), Executor de Retenção (constrói e executa planos), Analista de NPS (transforma satisfação em ação) [team-crm-fidelizacao]
- Fluxo integrado com aprovação obrigatória do Marco antes de qualquer registro no Monday ou notificação ao corretor [team-crm-fidelizacao]
- Cadência: varredura de churn toda segunda às 10:00; Relatório consolidado de retenção para o Diretor no Dia 1 de cada mês [team-crm-fidelizacao]
- Integra NPS com histórico de renovação para diagnóstico completo; recebe feedback de sinistros via board 18026494883 [team-crm-fidelizacao]
- Clientes recuperados com oportunidade de cross-sell são encaminhados ao Hunter de Cross-sell (Comercial) [team-crm-fidelizacao]

## Connections

- [[menegon-seguros]] — empresa a que pertence
- [[sistema-agentes-menegon]] — listagem de todos os agentes do núcleo
- [[time-comercial]] — destino de clientes recuperados com oportunidade de cross-sell
- [[monday-crm]] — fonte de dados de sinistros e NPS; destino de planos de retenção aprovados

## Changelog

- 2026-04-15 — criada a partir de [team-crm-fidelizacao] e [menegon-company]
