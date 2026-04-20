---
rotina: inteligencia-renovacao
familia: renovacao
toca_cliente_externo: false
modo_autonomia: auto
board_monday_principal: 9427535861
metricas_chave:
  - metricas_acao.itens_avaliados
  - metricas_acao.alertas_gerados
  - metricas_acao.updates_escritos_no_monday
created: 2026-04-19
updated: 2026-04-20
---

# Inteligência de Renovação — Índice

Rotina diária (07:00 BRT). Varre o board Renovação (`9427535861`) buscando apólices com vencimento em 15 dias e gera dossiê completo por cliente: apólices ativas e vencidas, LTV, sinistros, ramos, data de antiguidade e texto de WhatsApp para o corretor.

## Última execução

2026-04-20 j10 (10:32 BRT) — 6 clientes na janela 2026-04-29 a 2026-05-01. LTV R$ 51.373,41. 2 apólices com prêmio R$ 0 (Atualizar Cadastro urgente).

## Histórico de recalibrações
<!-- preenchido pelo recalibrador -->

## Execuções

| Data | Clientes | LTV total | Alertas | Observação |
|------|----------|-----------|---------|------------|
| — | — | — | — | Rotina criada em 2026-04-19. Ainda sem execuções. |
| 2026-04-20 | 0 clientes | R$ 0,00 | 0 VIP · 0 RISCO | Janela 2026-05-04–05-06 vazia; pipeline ativo encerra em 2026-04-30. Re-exec 10:17 BRT confirmou resultado. |
| 2026-04-20 (j10) | 6 clientes | R$ 51.373,41 | 0 VIP · 0 RISCO | Teste janela_dias=10; janela 2026-04-29–05-01. 2 apólices prêmio R$ 0 (Atualizar Cadastro). |
