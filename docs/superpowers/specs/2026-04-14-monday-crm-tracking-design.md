---
title: Monitoramento Sistemático do Monday CRM para Identificação de Melhorias
type: analysis
created: 2026-04-14
updated: 2026-04-14
tags: [monday, crm, monitor, agentes, wiki, alertas]
---

## Objetivo

Monitorar sistematicamente o Monday CRM para identificar oportunidades de melhoria operacional — renovações em risco, churn latente, pipeline estagnado, NPS baixo, automações falhando e desvios de forecast — e acionar automaticamente o agente responsável quando uma anomalia é detectada.

## Escopo

Cobre duas responsabilidades:

1. **Monitoramento proativo** — leitura diária dos 8 boards, avaliação de 6 dimensões com limiares de alerta, geração de relatório na wiki Git
2. **Reatividade automática** — quando anomalia é detectada, o agente responsável pela dimensão é acionado diretamente, sem intervenção manual

Não cobre: execução das ações corretivas (responsabilidade dos agentes especializados), mudanças estruturais no sistema (agentes, skills, boards).

## Arquitetura

Um novo agente **monitor-crm** opera como task agendada local (Desktop), rodando todo dia às 06:00 — antes de todas as tasks operacionais. Fluxo:

```
06:00 → monitor-crm roda
         ├── consulta 8 boards via MCP Monday
         ├── avalia 6 dimensões
         ├── grava relatório em wiki/pages/analyses/crm-monitor/YYYY-MM-DD.md
         ├── atualiza wiki/pages/analyses/crm-monitor/index.md
         └── para cada anomalia → aciona task do agente responsável
```

## Estrutura de Arquivos

```
wiki/pages/analyses/crm-monitor/
  index.md              ← índice de todos os relatórios (uma linha por dia)
  2026-04-14.md         ← relatório diário
  2026-04-15.md
  ...
```

## As 6 Dimensões e Limiares de Alerta

| Dimensão | Board(s) | Limiar de alerta | Agente acionado |
|---|---|---|---|
| **Renovações** | renovacao (9427535861) | Apólice vencendo em ≤7 dias sem status "em andamento" | especialista-renovacao |
| **Churn** | clientes (9332203920) | Cliente com score de risco alto sem plano de retenção ativo | analista-churn |
| **Pipeline Seguro Novo** | seguro_novo (9332203907) + leads (9332203913) | Lead parado há >5 dias ou forecast do mês <70% da meta | analista-pipeline |
| **NPS** | nps (9751082146) | Detrator (nota ≤6) sem atualização nos últimos 7 dias | analista-nps |
| **Qualidade das automações** | todos | Task com status `erro`/`parcial` no último ciclo; item criado por agente sem atualização em >3 dias | gerente-comercial |
| **Forecast** | apolices (9749857183) + seguro_novo | Desvio >15% entre forecast e realidade do mês corrente | analista-forecast |

O monitor detecta e delega — não toma decisões operacionais.

## Formato do Relatório Diário

```markdown
---
title: Monitor CRM — YYYY-MM-DD
type: analysis
status: ok | alertas | critico
created: YYYY-MM-DD
---

## Resumo
<N> alertas detectados. <N> crítico(s).

## Dimensões

### Renovações — ok | alerta | critico
- <observação>

### Churn — ok | alerta | critico
- <observação> → **<agente> acionado** (se alerta)

### Pipeline Seguro Novo — ok | alerta | critico
### NPS — ok | alerta | critico
### Qualidade das automações — ok | alerta | critico
### Forecast — ok | alerta | critico

## Ações disparadas
- [ ] <agente> — <motivo>
```

**Status do relatório:** `ok` (nenhum alerta) | `alertas` (≥1 alerta não crítico) | `critico` (≥1 dimensão crítica)

## Formato do Índice

`wiki/pages/analyses/crm-monitor/index.md` — uma linha por dia, ordem cronológica reversa:

```markdown
| Data       | Status   | Alertas                        |
|------------|----------|-------------------------------|
| 2026-04-14 | alertas  | churn (2), pipeline (crítico) |
| 2026-04-13 | ok       | —                             |
```

## Protocolo de Commit

O monitor-crm commita ao final de cada execução:

```
git add wiki/pages/analyses/crm-monitor/YYYY-MM-DD.md
git add wiki/pages/analyses/crm-monitor/index.md
git commit -m "monitor: YYYY-MM-DD <status> — <resumo de alertas>"
```

Regras: `git add` nos arquivos específicos (nunca `-A`), nunca `--no-verify`.

## Acionamento de Agentes

Quando o monitor detecta anomalia, inclui no output um bloco de contexto estruturado dirigido à task agendada responsável. As tasks locais compartilham o mesmo contexto Desktop — o monitor invoca diretamente a próxima task com os dados já contextualizados. Sem webhook, sem script auxiliar.

## Contexto do Sistema

- **Workspace Monday:** 11267903
- **Boards ativos:** renovacao, seguro_novo, leads, clientes, apolices, nps, sinistro, agendamentos
- **Agentes disponíveis:** 16 (ver `menegon-seguros/agents/`)
- **Tasks agendadas locais:** 11 (todas locais — limite de 3 cloud triggers)
- **MCP Monday:** disponível via `.mcp.json` (workspace 11267903)

## Critérios de Sucesso

- Todo dia às 06:00 há um relatório novo em `crm-monitor/`
- Nenhuma anomalia passa 24h sem ser detectada e delegada ao agente responsável
- O índice permite ver em segundos a evolução do status do CRM ao longo das semanas
- Qualquer agente futuro consegue ler os relatórios sem contexto adicional
