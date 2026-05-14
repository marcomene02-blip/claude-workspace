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
updated: 2026-05-14
---

# Inteligência de Renovação — Índice

Rotina diária (07:00 BRT). Varre o board Renovação (`9427535861`) buscando apólices com vencimento em 15 dias e gera dossiê completo por cliente: apólices ativas e vencidas, LTV, sinistros, ramos, data de antiguidade e texto de WhatsApp para o corretor.

## Última execução

2026-05-14 (07:00 BRT) — 10 clientes na janela 2026-05-28 a 2026-05-30. 3 VIPs: LAURO FERREIRA GONCALVES (R$ 67.458,58) · ALL CONNECT SERVICOS LTDA ME (R$ 26.115,07) · VALDIR GONZALEZ PAIXAO JUNIOR (R$ 17.755,74). LTV total da janela: R$ 19.213,48. 0 RISCO. 5 com status "Atualizar Cadastro". 3 multi-ramo: LAURO · ERIC · ALL CONNECT.

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
| 2026-05-03 | 13 clientes | R$ 294.225,74 | 7 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-17–05-19. VIPs: JOAO HENRIQUE PUPO NEVES (R$ 85.202,68) · MARA SILVIA MARCELLO (R$ 36.731,00) · TIEGHIS MOVEIS (R$ 28.204,86) · LIVIA MARTIN CARDOZO (R$ 28.013,04) · ALCIDES VENDRAMI (R$ 23.568,37) · SHANTAL MENEGON PILLAY (R$ 21.614,98) · DANIELLA PALUDETTI GAIOTTI BOIANI (R$ 18.839,32). |
| 2026-05-04 | 16 clientes | R$ 36.065,49 | 9 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-18–05-20. VIPs: JOAO HENRIQUE PUPO NEVES (R$ 85.202,68) · GRANDD ATACADO (R$ 50.779,36) · MARA SILVIA MARCELLO (R$ 36.731,00) · TIEGHIS MOVEIS (R$ 28.204,86) · LIVIA MARTIN CARDOZO (R$ 28.013,04) · MARCO AURELIO MENEGON FILHO (R$ 26.444,29) · PILAN ENGENHARIA (R$ 22.797,45) · SHANTAL MENEGON PILLAY (R$ 21.614,98) · DANIELLA PALUDETTI GAIOTTI BOIANI (R$ 18.839,32). |
| 2026-05-05 | 16 clientes | R$ 24.348,62 | 7 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-19–05-21. VIPs: JOAO HENRIQUE PUPO NEVES (R$ 85.202,68) · ANA PAULA SPADOTTO (R$ 27.831,06) · GRANDD ATACADO (R$ 50.779,36) · MARA SILVIA MARCELLO (R$ 36.731,00) · MARCO AURELIO MENEGON FILHO (R$ 26.444,29) · PILAN ENGENHARIA (R$ 22.797,45) · DANIELLA PALUDETTI GAIOTTI BOIANI (R$ 18.839,32). 5 novos: ANA PAULA SPADOTTO, LUIZA CARAMANTE ARRUDA, OTAVIO CARMELLO GOMES, RENATA SILVA VIEIRA, HELENICE BARREIROS ORPHEU. |
| 2026-05-06 | 15 clientes | R$ 30.040,69 | 5 VIP · 0 RISCO | Execução diária 07:00 BRT. Janela 2026-05-20–05-22. VIPs: GRANDD ATACADO (R$ 50.779,36) · ANA PAULA SPADOTTO (R$ 27.831,06) · MARCO AURELIO MENEGON FILHO (R$ 26.444,29) · PILAN ENGENHARIA (R$ 22.797,45) · SHEILA CRISTINA SAYURI ABE MAGALHAES (R$ 22.378,26). Nova janela: SHEILA CRISTINA (VIP, 1ª vez). Pendências: EDUARDO FERNANDO (status CRM inconsistente), HELENICE (duplicata apólice), PILAN (cadastro fragmentado). |
| 2026-05-07 | 13 clientes | R$ 28.066,75 | 3 VIP · 0 RISCO | — |
| 2026-05-08 | 9 clientes | R$ 103.984,83 | 3 VIP · 0 RISCO | VIPs: SHEILA SAYURI (R$ 22.378,26) · RENATA MENEGUELLA CURY (R$ 22.296,08) · ALINE FISCHER ANIZELLI (R$ 20.448,25). Pendência CRM: EDUARDO FERNANDO — apólice 9459620 "Renovada" prematura (3ª ocorrência). |
| 2026-05-09 | 9 clientes | R$ 20.043,41 | 4 VIP · 0 RISCO | VIPs: MARIO PARAISO (R$ 28.493,26) · RENATA MENEGUELLA CURY (R$ 22.296,08) · ALINE FISCHER ANIZELLI (R$ 20.448,25) · RAQUEL GUAZZELLI (R$ 18.063,62). 2 primeiras renovações: JOAO CARLOS BRAGA · MARCELO CHAGURI. 3 multi-ramo. |
| 2026-05-11 | 11 clientes | R$ 225.362,80 | 5 VIP · 0 RISCO | VIPs: LAURO FERREIRA (R$ 67.459,58) · MARA MARCELLO (R$ 36.731,00) · RAQUEL DIAS (R$ 29.072,59) · MARIO PARAISO (R$ 28.493,26) · RAQUEL GUAZZELLI (R$ 18.063,62). 1 primeira renovação: PAULO BORLINA. 4 multi-ramo: LAURO · MARA · MARIO · ISOLINA. |
| 2026-05-12 | 8 clientes | R$ 143.422,13 | 3 VIP · 0 RISCO | VIPs: LAURO FERREIRA (R$ 39.601,27) · MARA MARCELLO (R$ 34.078,06) · RAQUEL FROSSARD (R$ 29.072,59). 1 primeira renovação: PAULO BORLINA. 2 multi-ramo: LAURO · MARA. |
| 2026-05-13 | 7 clientes | R$ 100.165,38 | 1 VIP · 0 RISCO | VIP: LAURO FERREIRA GONCALVES (R$ 39.601,27). 4 "Atualizar Cadastro". 2 multi-ramo: LAURO (AUTO+PATRIMONIAL+RESP) · ERIC GONCALVES DA CUNHA (AUTO+PATRIMONIAL). |
| 2026-05-14 | 10 clientes | R$ 19.213,48 | 3 VIP · 0 RISCO | VIPs: LAURO FERREIRA GONCALVES (R$ 67.458,58) · ALL CONNECT SERVICOS LTDA ME (R$ 26.115,07) · VALDIR GONZALEZ PAIXAO JUNIOR (R$ 17.755,74). 5 "Atualizar Cadastro". 3 multi-ramo: LAURO · ERIC · ALL CONNECT. |
