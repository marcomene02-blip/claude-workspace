---
title: Backlog de Melhorias
type: topic
created: 2026-04-14
updated: 2026-04-14
sources: []
tags: [backlog, melhorias, plugins, agentes, skills, tarefas]
---

## Summary

Rastreamento centralizado de ideias de melhoria para todos os ativos do sistema: plugins, agentes, skills e tarefas agendadas. As melhorias são priorizadas em Alta / Média / Baixa e rastreadas com status Pendente / Em andamento / Concluído. As entradas de plugins com prioridade Alta envolvem habilitar paralelismo no monitor-crm e auditoria adversarial nas skills que escrevem no CRM.

## Key points

- 6 melhorias identificadas para plugins `superpowers` e `codex`, todas com status Pendente
- 17 agentes cadastrados no backlog aguardando levantamento de melhorias específicas
- 14 skills cadastradas, incluindo `monday-crm-write` e `forecast-ponderado` como candidatas a revisão de código
- Nenhuma tarefa agendada ativa no momento do levantamento (2026-04-14)

## Connections

- [Monitor CRM — Índice](../analyses/crm-monitor/index.md) — agente `monitor-crm` é alvo da melhoria de paralelismo (superpowers)
- Workspace n8n em menegon.app.n8n.cloud referenciado na melhoria de skills `n8n-*`

## Open questions

- Quais agentes têm maior prioridade para levantamento de melhorias específicas?
- A skill `forecast-ponderado` tem cobertura de testes antes de receber `codex:review`?
- O limite de 3 cloud triggers afeta a viabilidade de ativar tarefas agendadas no futuro?

## Changelog

- 2026-04-14 — página criada com 6 melhorias de plugins e tabelas-esqueleto para agentes, skills e tarefas

---

## Plugins — 2 instalados

| Nome | Versão | Melhoria | Prioridade | Status |
|------|--------|----------|------------|--------|
| superpowers | 5.0.7 | Habilitar `dispatching-parallel-agents` no agente `monitor-crm` para rodar forecast + pipeline + NPS em paralelo — reduz tempo de diagnóstico matinal de ~3 execuções sequenciais para 1 | Alta | Pendente |
| superpowers | 5.0.7 | Ativar skills `n8n-*` nos agentes que constroem ou debugam automações (especialista-renovacao, executor-retencao) — o workspace n8n em menegon.app.n8n.cloud já existe mas nenhum agente usa essas skills explicitamente | Alta | Pendente |
| superpowers | 5.0.7 | Integrar skill `notebooklm` ao agente `analista-nps` para consultar corpus de feedback de clientes acumulado (NPS board + apolices) sem precisar repassar dados brutos no prompt | Média | Pendente |
| superpowers | 5.0.7 | Usar skill `insights` no fluxo semanal do `diretor-comercial` para gerar relatório de uso de agentes — identifica quais agentes param de ser invocados e quais consomem mais tempo | Média | Pendente |
| codex | 1.0.3 | Rodar `codex:adversarial-review` nas skills `monday-crm-write` e `plano-retencao` — essas skills escrevem no CRM (fonte de verdade); um erro silencioso pode corromper dados de renovação para 95% da carteira | Alta | Pendente |
| codex | 1.0.3 | Rodar `codex:review` na skill `forecast-ponderado` — lógica de três cenários é complexa e ainda não foi auditada; erros afetam diretamente as decisões do Diretor Comercial | Média | Pendente |

---

## Agentes (17)

| Nome | Melhoria | Prioridade | Status |
|------|----------|------------|--------|
| analista-campanhas | — | — | Pendente |
| analista-churn | — | — | Pendente |
| analista-forecast | — | — | Pendente |
| analista-nps | — | — | Pendente |
| analista-performance | — | — | Pendente |
| analista-pipeline | — | — | Pendente |
| cmo | — | — | Pendente |
| criador-conteudo | — | — | Pendente |
| diretor-comercial | — | — | Pendente |
| especialista-inbound | — | — | Pendente |
| especialista-renovacao | — | — | Pendente |
| especialista-seguro-novo | — | — | Pendente |
| executor-retencao | — | — | Pendente |
| gerente-comercial | — | — | Pendente |
| hunter-cross-sell | — | — | Pendente |
| monitor-crm | — | — | Pendente |
| qualificador-leads | — | — | Pendente |

---

## Skills (14)

| Nome | Melhoria | Prioridade | Status |
|------|----------|------------|--------|
| abordagem-comercial | — | — | Pendente |
| analise-campanhas | — | — | Pendente |
| analise-churn | — | — | Pendente |
| analise-nps | — | — | Pendente |
| auditoria-pipeline | — | — | Pendente |
| criacao-conteudo | — | — | Pendente |
| cross-sell-hunt | — | — | Pendente |
| forecast-ponderado | — | — | Pendente |
| monday-crm-query | — | — | Pendente |
| monday-crm-write | — | — | Pendente |
| nutricao-lead | — | — | Pendente |
| plano-retencao | — | — | Pendente |
| qualificacao-lead | — | — | Pendente |
| segmentacao-carteira | — | — | Pendente |

---

## Tarefas Agendadas (0)

| Nome | Melhoria | Prioridade | Status |
|------|----------|------------|--------|
| *nenhuma ativa no momento* | — | — | — |

---

*Última atualização: 2026-04-14*
