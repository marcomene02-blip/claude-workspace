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
updated: 2026-05-02
---

# Inteligência de Renovação — Índice

Rotina diária (07:00 BRT). Varre o board Renovação (`9427535861`) buscando apólices com vencimento em 15 dias e gera dossiê completo por cliente: apólices ativas e vencidas, LTV, sinistros, ramos, data de antiguidade e texto de WhatsApp para o corretor.

## Última execução

2026-05-02 (07:00 BRT) — 11 clientes na janela 2026-05-16 a 2026-05-18. 4 VIPs: LIVIA MARTIN CARDOZO (R$ 28.013,04) · TIEGHIS MOVEIS PROJETADOS E PLANEJADOS (R$ 28.204,86) · ALCIDES VENDRAMI (R$ 23.568,37) · SHANTAL MENEGON PILLAY (R$ 21.613,98). LTV total da janela: R$ 159.620,46.

## Histórico de recalibrações
<!-- preenchido pelo recalibrador -->

## Execuções

| Data | Clientes | LTV total | Alertas | Observação |
|------|----------|-----------|---------|------------|
| — | — | — | — | Rotina criada em 2026-04-19. Ainda sem execuções. |
| 2026-04-20 | 0 clientes | R$ 0,00 | 0 VIP · 0 RISCO | Janela 2026-05-04–05-06 vazia; pipeline ativo encerra em 2026-04-30. Re-exec 10:17 BRT confirmou resultado. |
| 2026-04-20 (j10) | 6 clientes | R$ 51.373,41 | 0 VIP · 0 RISCO | Teste janela_dias=10; janela 2026-04-29–05-01. 2 apólices prêmio R$ 0 (Atualizar Cadastro). |
| 2026-04-20 (07:23) | 0 clientes | R$ 0,00 | 0 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-04–05-06 vazia; pipeline ativo encerra em 2026-04-30. |
| 2026-04-21 | 0 clientes | R$ 0,00 | 0 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-05–05-07 vazia; pipeline ativo encerra em 2026-04-30. |
| 2026-04-22 | 0 clientes | R$ 0,00 | 0 VIP · 0 RISCO | Execução diária 07:14 BRT. Janela 2026-05-06–05-08 vazia; pipeline ativo encerra em 2026-04-30. |
| 2026-04-23 | 0 clientes | R$ 0,00 | 0 VIP · 0 RISCO | Execução diária 07:10 BRT. Janela 2026-05-07–05-09 vazia; pipeline ativo encerra em 2026-04-30. |
| 2026-04-24 | 9 clientes | R$ 17.613,02 | 2 VIP · 0 RISCO | Execução diária 07:15 BRT. Janela 2026-05-08–05-10. VIPs: Claudete Pinto Pereira (R$ 18.185,90) · Odair João Valário (R$ 40.152,82). |
| 2026-04-25 | 8 clientes | R$ 128.363,93 | 2 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-09–05-11. VIPs: Paula Schmidt Azevedo Gaiolla (R$ 45.781,30) · Posto São Paulo Avenida Ltda (R$ 27.333,47). |
| 2026-04-26 | 9 clientes | R$ 220.293,56 | 4 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-10–05-12. VIPs: Paula Schmidt (R$ 45.781,30) · Posto São Paulo Avenida (R$ 27.333,47) · Armando Delmanto (R$ 69.545,69) · FBRS Gestão (R$ 20.269,63). |
| 2026-04-27 | 12 clientes | R$ 254.726,75 | 5 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-11–05-13. VIPs: Paula Schmidt (R$ 45.781,30) · Paula Maria Leite Maletta (R$ 18.523,99) · Posto São Paulo Avenida (R$ 27.333,47) · Armando Delmanto (R$ 82.419,94) · FBRS Gestão (R$ 20.269,63). |
| 2026-04-28 | 11 clientes | R$ 189.033,30 | 3 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-12–05-14. VIPs: Armando Delmanto (R$ 82.419,94) · FBRS Gestão (R$ 20.269,63) · Paula Maria Leite Maletta (R$ 18.523,99). |
| 2026-04-29 | 10 clientes | R$ 93.114,79 | 1 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-13–05-15. VIP: Paula Maria Leite Maletta (R$ 18.523,99). |
| 2026-04-30 | 7 clientes | R$ 55.042,99 | 0 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-14–05-16. Todos mono-ramo. Pendência: JULIA LAURINDO GIACOMINI — apólice ativa não registrada no CRM. |
| 2026-05-01 | 8 clientes | R$ 77.253,14 | 1 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-15–05-17. VIP: ALCIDES VENDRAMI (R$ 23.568,37). Pendência: JULIA LAURINDO GIACOMINI — apólice ativa ainda não registrada no CRM. |
| 2026-05-02 | 11 clientes | R$ 159.620,46 | 4 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-16–05-18. VIPs: LIVIA MARTIN CARDOZO (R$ 28.013,04) · TIEGHIS MOVEIS PROJETADOS E PLANEJADOS (R$ 28.204,86) · ALCIDES VENDRAMI (R$ 23.568,37) · SHANTAL MENEGON PILLAY (R$ 21.613,98). Pendência: JULIA LAURINDO GIACOMINI — apólice ativa não registrada no CRM (3ª execução consecutiva). |
