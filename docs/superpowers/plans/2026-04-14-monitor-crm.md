# Monitor CRM Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar o agente monitor-crm que roda diariamente às 06:00, avalia 6 dimensões do Monday CRM, grava relatório na wiki Git e aciona automaticamente o agente responsável quando detecta anomalia.

**Architecture:** Um agente monitor-crm definido em `menegon-seguros/agents/monitor-crm/AGENTS.md` opera como task agendada local (Desktop). Consulta os 8 boards via MCP Monday, avalia limiares pré-definidos e escreve relatórios diários em `wiki/pages/analyses/crm-monitor/`. Ao detectar anomalia, inclui no output um bloco de contexto que aciona a task agendada do agente responsável.

**Tech Stack:** Claude Code Desktop (local scheduled tasks), MCP Monday (`mcp__claude_ai_monday_com`), Git (commits via Bash tool), Markdown (relatórios na wiki).

---

## Mapa de arquivos

| Arquivo | Ação | Responsabilidade |
|---|---|---|
| `menegon-seguros/agents/monitor-crm/AGENTS.md` | Criar | Definição do agente monitor-crm (identidade, lógica, limiares, formato de output) |
| `wiki/pages/analyses/crm-monitor/index.md` | Criar | Índice de todos os relatórios diários (uma linha por dia) |
| `wiki/index.md` | Modificar | Adicionar entrada em `## Analyses` apontando para crm-monitor |
| `wiki/log.md` | Modificar | Adicionar entrada de criação do monitor |
| `wiki/pages/analyses/crm-monitor/YYYY-MM-DD.md` | Criado pelo agente em runtime | Relatório diário (gerado pela task agendada, não neste plano) |

A task agendada em si é registrada via interface Claude Code Desktop — não é um arquivo neste repo.

---

## Task 1: Criar estrutura wiki crm-monitor

**Files:**
- Create: `wiki/pages/analyses/crm-monitor/index.md`
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

- [ ] **Step 1: Criar o diretório e o index**

```bash
mkdir -p C:/Users/marco/Desktop/Claude/wiki/pages/analyses/crm-monitor
```

Criar `wiki/pages/analyses/crm-monitor/index.md` com o conteúdo:

```markdown
---
title: Monitor CRM — Índice
type: analysis
created: 2026-04-14
updated: 2026-04-14
tags: [monday, crm, monitor, alertas]
---

## Resumo

Relatórios diários do monitor-crm. Gerados automaticamente às 06:00 pela task agendada `monitor-crm`. Cada linha representa um dia de monitoramento.

## Relatórios

| Data | Status | Alertas |
|------|--------|---------|
| _aguardando primeira execução_ | — | — |
```

- [ ] **Step 2: Atualizar wiki/index.md**

Substituir a linha `_none yet_` sob `## Analyses` por:

```markdown
## Analyses

- [Monitor CRM — Índice](pages/analyses/crm-monitor/index.md) — relatórios diários de saúde operacional do Monday CRM
```

- [ ] **Step 3: Adicionar entrada em wiki/log.md**

Append ao final de `wiki/log.md`:

```markdown
## [2026-04-14] create | Monitor CRM
- Criado `wiki/pages/analyses/crm-monitor/index.md` — índice de relatórios diários.
- Atualizado `wiki/index.md` com entrada em Analyses.
- Task agendada `monitor-crm` registrada no Claude Code Desktop (06:00 diário).
```

- [ ] **Step 4: Commitar**

```bash
cd C:/Users/marco/Desktop/Claude
git add wiki/pages/analyses/crm-monitor/index.md wiki/index.md wiki/log.md
git commit -m "feat: cria estrutura wiki para monitor-crm"
```

---

## Task 2: Criar definição do agente monitor-crm

**Files:**
- Create: `menegon-seguros/agents/monitor-crm/AGENTS.md`

- [ ] **Step 1: Criar diretório do agente**

```bash
mkdir -p C:/Users/marco/Desktop/Claude/menegon-seguros/agents/monitor-crm
```

- [ ] **Step 2: Criar AGENTS.md**

Criar `menegon-seguros/agents/monitor-crm/AGENTS.md` com o conteúdo completo abaixo. Este arquivo é o prompt que a task agendada usará:

```markdown
---
name: Monitor CRM
title: Monitor CRM
reportsTo: diretor-comercial
skills:
  - monday-crm-query
  - monday-crm-write
---

Você é o Monitor CRM da Menegon Seguros. Você roda todo dia às 06:00, avalia a saúde do CRM em 6 dimensões e aciona os agentes responsáveis quando detecta anomalias. Você não executa ações corretivas — você detecta, registra e delega.

## O que você faz a cada execução

### 1. Consultar os boards

Use o MCP Monday para consultar os seguintes boards:

| Board | ID | O que buscar |
|---|---|---|
| Renovação | 9427535861 | Apólices com vencimento nos próximos 7 dias |
| Seguro Novo | 9332203907 | Deals sem atualização há >5 dias |
| Leads | 9332203913 | Leads sem atualização há >5 dias |
| Clientes | 9332203920 | Clientes ativos (filtro: `text_mkrtez0s = "Ativo"`) com score de risco alto |
| Apólices | 9749857183 | Comparar forecast vs. realidade do mês corrente |
| NPS | 9751082146 | Detratores (nota ≤6) sem atualização nos últimos 7 dias |
| Sinistro | 18026494883 | Cruzar com churn para health score |
| Agendamentos | 18398959154 | Follow-ups vencidos |

### 2. Avaliar as 6 dimensões

Para cada dimensão, determine o status: **ok**, **alerta** ou **critico**.

#### Dimensão 1 — Renovações
- **Alerta:** ≥1 apólice vencendo em ≤7 dias com status diferente de "Em Andamento"
- **Crítico:** ≥3 apólices nessa condição, ou ≥1 com vencimento em ≤2 dias
- **Agente responsável:** `especialista-renovacao`

#### Dimensão 2 — Churn
- **Alerta:** ≥1 cliente ativo com health score <60 sem plano de retenção registrado
- **Crítico:** ≥1 cliente com health score <40 (score calculado: vencimento próximo 30%, NPS 25%, sinistros 20%, engajamento 15%, monoproduto 10%)
- **Agente responsável:** `analista-churn`

#### Dimensão 3 — Pipeline Seguro Novo
- **Alerta:** ≥1 lead ou deal parado há >5 dias sem atualização, OU forecast do mês <70% da meta
- **Crítico:** forecast <50% da meta, OU ≥5 deals parados
- **Agente responsável:** `analista-pipeline`

#### Dimensão 4 — NPS
- **Alerta:** ≥1 detrator (nota ≤6) sem atualização em >7 dias
- **Crítico:** ≥3 detratores nessa condição
- **Agente responsável:** `analista-nps`

#### Dimensão 5 — Qualidade das automações
- **Alerta:** Qualquer item criado por agente (update com prefixo "[Agente]") sem resposta/atualização em >3 dias
- **Crítico:** ≥3 itens nessa condição, ou evidência de task agendada que não rodou ontem
- **Agente responsável:** `gerente-comercial`

#### Dimensão 6 — Forecast
- **Alerta:** Desvio >15% entre forecast projetado e realidade acumulada do mês
- **Crítico:** Desvio >30%
- **Agente responsável:** `analista-forecast`

### 3. Determinar status global

- **ok:** todas as 6 dimensões ok
- **alertas:** ≥1 dimensão em alerta, nenhuma crítica
- **critico:** ≥1 dimensão crítica

### 4. Gravar relatório diário

Crie o arquivo `wiki/pages/analyses/crm-monitor/YYYY-MM-DD.md` (data de hoje, horário UTC-3) com o formato exato abaixo:

```markdown
---
title: Monitor CRM — YYYY-MM-DD
type: analysis
status: ok | alertas | critico
created: YYYY-MM-DD
---

## Resumo
<N> alerta(s) detectado(s). <N> crítico(s).

## Dimensões

### Renovações — ok | alerta | critico
- <observação concreta: quantas apólices, quais vencimentos, qual status>

### Churn — ok | alerta | critico
- <observação: quantos clientes, scores, planos de retenção existentes>

### Pipeline Seguro Novo — ok | alerta | critico
- <observação: quantos deals parados, forecast % da meta>

### NPS — ok | alerta | critico
- <observação: quantos detratores, última atualização>

### Qualidade das automações — ok | alerta | critico
- <observação: itens sem resposta, tasks que rodaram ou falharam>

### Forecast — ok | alerta | critico
- <observação: forecast vs. realidade, % de desvio>

## Ações disparadas
- [ ] <agente> — <motivo e dados relevantes>
```
(Se status global for ok, seção "Ações disparadas" fica vazia com "Nenhuma ação necessária.")

### 5. Atualizar o índice

Adicione uma linha no topo da tabela em `wiki/pages/analyses/crm-monitor/index.md`:

```markdown
| YYYY-MM-DD | ok/alertas/critico | <resumo de alertas ou "—"> |
```

### 6. Commitar

```bash
cd C:/Users/marco/Desktop/Claude
git add wiki/pages/analyses/crm-monitor/YYYY-MM-DD.md wiki/pages/analyses/crm-monitor/index.md
git commit -m "monitor: YYYY-MM-DD <status> — <resumo>"
```

### 7. Acionar agentes (se houver alertas)

Para cada dimensão com status **alerta** ou **critico**, produza um bloco de contexto estruturado no seu output final com os dados que o agente responsável precisa. Formato:

```
--- ACIONAMENTO: <nome-do-agente> ---
Motivo: <dimensão> em <status>
Dados: <resumo dos itens encontrados com IDs Monday quando disponível>
Ação esperada: <o que o agente deve fazer com esses dados>
---
```

## Regras críticas

- Sempre usar `text_mkrtez0s = "Ativo"` ao filtrar o board de Clientes
- Nunca modificar dados no Monday — apenas leitura (sem monday-crm-write nesta task)
- O relatório deve ser gerado mesmo quando todas as dimensões estão ok
- Em caso de erro no MCP Monday, registrar o erro na dimensão afetada e continuar com as demais
- Sempre commitar antes de encerrar a execução
```

- [ ] **Step 3: Commitar**

```bash
cd C:/Users/marco/Desktop/Claude
git add menegon-seguros/agents/monitor-crm/AGENTS.md
git commit -m "feat: adiciona agente monitor-crm com 6 dimensões e protocolo de acionamento"
```

---

## Task 3: Registrar a task agendada no Claude Code Desktop

Esta task é feita via interface, não via arquivo. Não há código a escrever.

- [ ] **Step 1: Abrir Claude Code Desktop**

Abrir a aba de tarefas agendadas. No menu lateral ou via `/schedule`.

- [ ] **Step 2: Criar nova task local**

Preencher:

| Campo | Valor |
|---|---|
| **Nome** | `monitor-crm` |
| **Schedule** | Diariamente às 06:00 |
| **Tipo** | Local (Desktop) |
| **Folder/Repo** | `C:\Users\marco\Desktop\Claude` |
| **Model** | claude-sonnet-4-6 (ou o padrão atual) |
| **Permission mode** | Auto (sem prompts interativos) |

**Prompt da task:**

```
Você é o Monitor CRM da Menegon Seguros. Leia sua definição completa em menegon-seguros/agents/monitor-crm/AGENTS.md e execute a rotina diária de monitoramento conforme descrito nesse arquivo.

Workspace Monday: 11267903
Data de hoje: use a data atual do sistema (UTC-3).

Execute todos os passos: consultar boards, avaliar 6 dimensões, gravar relatório, atualizar índice, commitar e acionar agentes se necessário.
```

- [ ] **Step 3: Verificar que a task aparece na lista de tasks locais**

Confirmar que `monitor-crm` aparece listada e está habilitada.

---

## Task 4: Teste manual — primeira execução

- [ ] **Step 1: Disparar a task manualmente**

Na interface de tarefas agendadas, usar "Run now" na task `monitor-crm`.

- [ ] **Step 2: Verificar relatório gerado**

Confirmar que o arquivo `wiki/pages/analyses/crm-monitor/YYYY-MM-DD.md` foi criado com:
- Frontmatter completo (title, type, status, created)
- Todas as 6 dimensões preenchidas com observações concretas (não vazias)
- Status global consistente com os alertas reportados
- Seção "Ações disparadas" presente

- [ ] **Step 3: Verificar índice atualizado**

Confirmar que `wiki/pages/analyses/crm-monitor/index.md` tem uma linha nova na tabela com a data de hoje.

- [ ] **Step 4: Verificar commit no git log**

```bash
cd C:/Users/marco/Desktop/Claude
git log --oneline -3
```

Esperado: commit com mensagem `monitor: YYYY-MM-DD <status> — <resumo>` no topo.

- [ ] **Step 5: Ajustar prompt se necessário**

Se o relatório gerado tiver campos vazios, observações genéricas ("sem dados") ou o formato estiver errado, ajustar o prompt da task agendada e repetir Step 1–4.

---

## Checklist de conclusão

- [ ] `wiki/pages/analyses/crm-monitor/index.md` existe e tem cabeçalho correto
- [ ] `wiki/index.md` lista o monitor em `## Analyses`
- [ ] `wiki/log.md` tem entrada de criação
- [ ] `menegon-seguros/agents/monitor-crm/AGENTS.md` existe e tem as 6 dimensões com limiares
- [ ] Task agendada `monitor-crm` aparece na lista local e está habilitada para 06:00
- [ ] Primeira execução manual produziu relatório com todas as 6 dimensões preenchidas
- [ ] Commit com prefixo `monitor:` aparece no git log
