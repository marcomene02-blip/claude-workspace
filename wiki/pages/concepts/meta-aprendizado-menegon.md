---
title: Sistema de Meta-Aprendizado — Menegon Seguros
type: concept
created: 2026-04-15
tags: [meta-aprendizado, telemetria, recalibrador, chassi]
---

# Sistema de Meta-Aprendizado — Menegon Seguros

## Visão geral

Cada rotina registra sua execução num arquivo markdown estruturado. O recalibrador lê esse histórico semanalmente e ajusta os parâmetros das rotinas dentro de travas de segurança. O resultado é um sistema que fica mais preciso à medida que acumula histórico.

## Arquitetura

```
┌─ CHASSI DE META-APRENDIZADO ───────────────────────────────────┐
│                                                                │
│   rotinas (12, expandindo)                                     │
│        │                                                       │
│        │ emit (YAML frontmatter + narrativa)                   │
│        ▼                                                       │
│   wiki/pages/analyses/<rotina>/YYYY-MM-DD.md ◄── canônico      │
│        │                                                       │
│        │ upsert (embedding de corpo + metadata)                │
│        ▼                                                       │
│   Pinecone index "menegon-telemetria" ◄── recall semântico     │
│        ▲                                                       │
│        │                                                       │
│   recalibrador-menegon (novo, semanal Sex 15:00)               │
│        │                                                       │
│        │ lê últimas N semanas + feedback humano                │
│        │ aplica trava dupla → grava changelog                  │
│        ▼                                                       │
│   menegon-seguros/config/thresholds/<rotina>.yaml ◄─ skills    │
│        │                                                       │
│        └─ rotinas leem esse yaml no início da execução         │
└────────────────────────────────────────────────────────────────┘
```

## Famílias de métricas

### Família A — Precisão preditiva
Usada em rotinas que fazem previsões verificáveis: forecast, qualificação de leads, cross-sell, churn.
O recalibrador compara o valor previsto com o valor realizado (lido do Monday 7/14/30 dias depois).

### Família B — Conversão de ação
Usada em rotinas operacionais que geram alertas: monitor-crm, audit-followup, limpeza-pipeline.
O recalibrador mede quantos alertas geraram ação humana dentro do prazo.

### Família D — Feedback humano (override)
O especialista-performance taga execuções com "util" ou "ignorar" na revisão semanal.
Tag "ignorar" em >30% das últimas 4 execuções bloqueia auto-apply.

## Travas de segurança do recalibrador

1. ≥4 execuções com dados completos (sem isso, pula)
2. Delta máximo ±10% por ciclo (além disso, proposta em shadow)
3. Rotina toca cliente externo → sempre shadow, nunca auto-apply
4. Feedback "ignorar" em >30% das últimas 4 execuções → shadow

## Feedback humano

O especialista-performance (agente existente) revisa na sprint-review semanal (sexta 16h) e taga execuções no Log Diário Monday (doc_id 39303015).

Convenção de tags no update do Monday:
- Adicionar texto `[util]` ou `[ignorar]` no update do dia correspondente

## Extensão futura

- Fase 2: email execution via n8n+Resend quando ferramenta for contratada
- Fase 2: publishing automático via Blotato quando conta estiver ativa
