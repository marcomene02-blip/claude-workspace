---
title: Rastreamento Sistemático de Melhorias do Monday CRM
type: analysis
created: 2026-04-14
updated: 2026-04-14
tags: [monday, crm, agentes, skills, tarefas-agendadas, wiki, changelog]
---

## Objetivo

Rastrear sistematicamente todas as melhorias do ecossistema Monday CRM — incluindo mudanças estruturais (agentes, skills, boards, tasks agendadas) e execuções rotineiras dos agentes — usando a wiki Git existente como fonte de verdade.

## Escopo

Cobre dois tipos de registro:

1. **Changelog estrutural** — quando o sistema muda (novo agente, skill, board, task agendada configurada ou alterada)
2. **Log de runtime** — quando os agentes executam suas tasks agendadas (resultado, métrica chave, status)

Não cobre: logs internos do Monday.com, histórico de conversas Claude, ou mudanças em arquivos que não sejam agentes/skills/tasks/boards.

## Estrutura de Arquivos

```
wiki/pages/analyses/
  monday-changelog.md    ← mudanças estruturais
  monday-runtime-log.md  ← execuções das tasks agendadas
```

Ambos seguem o frontmatter padrão da wiki (`title`, `type: analysis`, `created`, `updated`). Entradas em ordem cronológica reversa (mais recente no topo).

O `wiki/index.md` lista os dois arquivos em `## Analyses`. O `wiki/log.md` recebe entrada apenas na criação ou em mudanças de schema — não a cada execução de runtime.

## Formato das Entradas

### monday-changelog.md

```markdown
## [YYYY-MM-DD] <tipo> | <nome>
- **Tipo:** <tipo legível>
- **O quê:** descrição da mudança
- **Por quê:** motivação
- **Impacto:** boards, skills ou agentes afetados
- **Commit:** <hash curto>
```

**Tipos válidos:** `add-agent`, `add-skill`, `add-task`, `add-board`, `update-agent`, `update-skill`, `update-task`, `update-board`, `remove-agent`, `remove-skill`, `remove-task`, `remove-board`

### monday-runtime-log.md

```markdown
## [YYYY-MM-DD HH:MM] <nome-da-task> | <status>
- **Agente(s):** <lista>
- **Métrica chave:** <1–2 linhas com o resultado principal>
- **Duração:** <ex: 4m 12s>
- **Commit:** <hash curto>
```

**Status válidos:** `ok`, `erro`, `parcial`

## Protocolo de Commit

### Tasks agendadas (runtime)

Cada task agendada recebe a seguinte instrução no final do seu prompt:

> "Ao terminar, adicione uma entrada em `wiki/pages/analyses/monday-runtime-log.md` com data/hora UTC-3, nome da task, status (ok/erro/parcial), agente(s) envolvido(s), métrica chave (1–2 linhas) e duração. Faça commit apenas desse arquivo com mensagem `runtime: <nome-da-task> <status>`."

### Mudanças estruturais (changelog)

O agente que implementa a mudança (novo agente, skill, board ou task) é responsável por:

1. Adicionar entrada em `monday-changelog.md`
2. Commitar com mensagem `changelog: <tipo> | <nome>`

Não há automação externa — o próprio Claude faz o commit ao final da execução.

### Regras de commit

- Usar `git add` no arquivo específico (nunca `git add -A`)
- Mensagem curta e descritiva
- Nunca usar `--no-verify`
- Não atualizar `wiki/index.md` ou `wiki/log.md` a cada execução de runtime — apenas na criação dos arquivos ou em mudanças de schema

## Contexto do Sistema

- **Workspace Monday:** 11267903
- **Boards ativos:** renovacao, seguro_novo, leads, clientes, apolices, nps, sinistro, agendamentos
- **Agentes:** 16 (ver `menegon-seguros/`)
- **Skills:** 10 (ver `menegon-seguros/skills/`)
- **Tasks agendadas locais:** 11 (matinal, vespertina, semanal, churn, limpeza-pipeline, cross-sell, forecast, sprint-review, alerta-fim-semana, consolidacao-semanal, mensal)
- **Limite de cloud triggers:** 3 (todas as 11 tasks ficam como locais/Desktop)

## Critérios de Sucesso

- Após qualquer execução de task agendada, há uma entrada correspondente em `monday-runtime-log.md`
- Após qualquer mudança estrutural no sistema, há uma entrada em `monday-changelog.md`
- Os dois arquivos são legíveis por qualquer agente futuro sem contexto adicional
- O histórico Git reflete a evolução do sistema ao longo do tempo
