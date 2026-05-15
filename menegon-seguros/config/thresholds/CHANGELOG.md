# Changelog de Thresholds — Menegon Seguros

Histórico de todas as alterações automáticas e manuais nos arquivos de threshold.
Editado pelo `recalibrador-menegon` (automático) ou pelo usuário (manual).

## Formato de entrada

```
### YYYY-MM-DD HH:MM — <rotina> — <campo>
- **Valor anterior:** <valor>
- **Valor novo:** <valor>
- **Justificativa:** <motivo da mudança>
- **Fonte:** recalibrador-menegon | manual
- **Reverter:** `<campo>: <valor_anterior>` em `config/thresholds/<rotina>.yaml`
```

## Entradas

<!-- O recalibrador-menegon adiciona entradas aqui automaticamente -->
<!-- Entradas mais recentes no topo -->

### 2026-05-15 15:00 — ciclo recalibrador-menegon (sexta-feira)
- **Rotinas avaliadas:** forecast-ponderado, qualificacao-lead, cross-sell-hunt, analise-churn, monitor-crm, nutricao-lead
- **Auto-aplicadas:** nenhuma
- **Shadow geradas:** 2
  - `monitor-crm.pipeline.alerta_deals_parados_dias`: 5 → 7 (proposta) — Trava 2 falhou: delta T+7 = −13% (> ±10%). Melhora vs. ciclo anterior (−52,6% → −13%) por batch clearing 05/05-06/05.
  - `monitor-crm.nps.detrator_sem_update_dias`: 7 → 14 (proposta) — Trava 2 falhou: delta = −100% (taxa_ação = 0/9 = 0%).
- **Métricas retroativas preenchidas:** T+7 para 9 execuções monitor-crm (16/04–07/05); T+14 para 6 execuções (16/04–30/04). Consulta board Seguro Novo (9332203907) e Sinistros (18026494883) via Monday MCP.
- **Sinistros confirmados:** 4 itens PENDENTES, updated_at = 2026-04-07 (38d sem atualização).
- **NPS detrator:** #9854144275 sem updates (261 dias).
- **Sem histórico suficiente:** forecast-ponderado, qualificacao-lead, cross-sell-hunt, analise-churn, nutricao-lead (0 execuções com dados).
- **Fonte:** recalibrador-menegon (ciclo automático sexta 15:00)
- **Ver:** wiki/pages/analyses/recalibrador-menegon/2026-05-15.md

### 2026-05-08 15:00 — ciclo recalibrador-menegon (sexta-feira)
- **Rotinas avaliadas:** forecast-ponderado, qualificacao-lead, cross-sell-hunt, analise-churn, monitor-crm, nutricao-lead
- **Auto-aplicadas:** nenhuma
- **Shadow:** monitor-crm — 2 propostas (pipeline.alerta_deals_parados_dias 5→7 e nps.detrator_sem_update_dias 7→14) — trava 2 falhou (delta T+14 = −52,6%, acima de ±10%)
- **Métricas retroativas:** T+14 preenchido para monitor-crm/2026-04-20 e monitor-crm/2026-04-21 (confirmado via board activity Monday)
- **Fonte:** recalibrador-menegon (ciclo automático sexta 15:00)
- **Ver:** wiki/pages/analyses/recalibrador-menegon/2026-05-08.md

### 2026-04-15 — setup inicial
- Todos os arquivos criados com valores hardcoded extraídos das SKILL.md originais
- Fonte: manual (T2 do plano rotinas-autonomas)
- Nenhum histórico de calibração disponível — recalibrador aguarda ≥4 execuções com dados completos
