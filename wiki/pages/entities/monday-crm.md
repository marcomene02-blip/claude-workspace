---
title: Monday CRM
type: entity
created: 2026-04-15
updated: 2026-04-15
sources: [menegon-company]
tags: [sistema, crm, monday, integração, fonte-de-verdade]
---

## Summary

Monday.com é o sistema de CRM utilizado pela Menegon Seguros como fonte de verdade para todos os 17 agentes. Todos os dados de clientes, apólices, leads, NPS e renovações vivem no Monday. Nenhuma análise ou recomendação dos agentes é gerada sem antes consultar o CRM, e toda saída relevante é registrada de volta no Monday como update ou notificação.

## Key points

- Sistema de CRM da Menegon Seguros; workspace ID 11267903 [menegon-company]
- 8 boards mapeados: renovacao (9427535861), seguro_novo (9332203907), leads (9332203913), clientes (9332203920), apolices (9749857183), nps (9751082146), sinistro (18026494883), agendamentos (18398959154) [menegon-company]
- 2 documentos internos mapeados: knowledge_map_doc_id (39560051) e daily_log_doc_id (39303015) [menegon-company]
- Princípio "dados primeiro": nenhuma análise ou recomendação dos agentes é gerada sem primeiro ler os dados do CRM [menegon-company]
- Princípio "registro obrigatório": toda ação executada por agente é documentada no Monday [menegon-company]
- Skills `monday-crm-query` e `monday-crm-write` são as interfaces programáticas dos agentes com o CRM [menegon-company]

## Connections

- [[menegon-seguros]] — empresa que usa o sistema
- [[sistema-agentes-menegon]] — todos os 17 agentes dependem do Monday CRM
- [[marco-menegon]] — gestor que aprova ações escritas no CRM

## Open questions

- Quais colunas são usadas em cada board? (Detalhes nos SKILL.md de monday-crm-query e monday-crm-write — pendente ingest)
- O Nucleus Operacional usa algum board adicional além dos 8 mapeados?

## Changelog

- 2026-04-15 — criada a partir de [menegon-company]; IDs de workspace, boards e docs documentados
