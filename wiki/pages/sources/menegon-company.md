---
title: Menegon Seguros — COMPANY
type: source
created: 2026-04-15
updated: 2026-04-15
sources: []
tags: [empresa, estrutura, agentes, crm, monday, metas, principios]
---

## Summary

COMPANY.md é o documento raiz da empresa Menegon Seguros no formato Agent Companies spec v1. Define a identidade da empresa, seus objetivos estratégicos, a estrutura organizacional com quatro núcleos e seus respectivos agentes, e os princípios de operação que regem todos os agentes. É também o mapa das integrações com o Monday CRM, listando os IDs de workspace, boards e documentos internos.

## Key points

- Menegon Seguros é uma corretora de seguros multiramo liderada por Marco Menegon (Diretor Comercial) [menegon-company]
- A empresa opera com corretores humanos amplificados por agentes de IA — agentes fazem diagnósticos, planos e registro; corretores focam em relacionamento e fechamento [menegon-company]
- Estrutura com 4 núcleos: Comercial (5 agentes), CRM & Fidelização (3), Marketing (4), Operacional (3) — 15 agentes na árvore estrutural, excluindo o próprio Diretor Comercial [menegon-company]
- 6 metas estratégicas formais: 95% renovação, +30% prêmio líquido/ano, NPS > 70, cross-sell 100% monoproduto, 80% automação operacional, forecast semanal com 3 cenários [menegon-company]
- Monday CRM (workspace 11267903) é a fonte de verdade; 8 boards mapeados: renovacao, seguro_novo, leads, clientes, apolices, nps, sinistro, agendamentos [menegon-company]
- 5 princípios de operação: renovação é prioridade absoluta; dados primeiro; aprovação humana para ações críticas; simplicidade; registro obrigatório no Monday [menegon-company]

## Arquivo raw

[raw/notes/2026-04-15-menegon-company.md](../raw/notes/2026-04-15-menegon-company.md)

## Connections

- [[menegon-seguros]] — entidade principal descrita por esta fonte
- [[marco-menegon]] — autor e Diretor Comercial citado no frontmatter
- [[monday-crm]] — sistema externo com workspace_id e board IDs documentados

## Open questions

- O COMPANY.md lista 15 agentes nos núcleos subordinados; o backlog-melhorias e o filesystem contam 17. A diferença são o `diretor-comercial` (Marco, no topo da árvore) e o `monitor-crm` (ausente do COMPANY.md). Reconciliar com [[sistema-agentes-menegon]].

## Changelog

- 2026-04-15 — criada a partir de menegon-seguros/COMPANY.md
