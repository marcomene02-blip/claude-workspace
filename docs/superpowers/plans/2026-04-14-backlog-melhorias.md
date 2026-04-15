# Backlog de Melhorias — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Popular o backlog `wiki/pages/topics/backlog-melhorias.md` com ideias concretas de melhoria para cada um dos 33 ativos do projeto menegon-seguros.

**Architecture:** Leitura sequencial de cada `AGENTS.md` e `SKILL.md`, extração de lacunas/oportunidades, e edição da tabela correspondente no backlog. Ao final, um commit único por grupo.

**Tech Stack:** Markdown, ferramentas Read/Edit do Claude Code.

---

## Arquivos Envolvidos

| Ação | Caminho |
|------|---------|
| Editar | `wiki/pages/topics/backlog-melhorias.md` |
| Ler (fonte) | `menegon-seguros/agents/*/AGENTS.md` (17 arquivos) |
| Ler (fonte) | `menegon-seguros/skills/*/SKILL.md` (14 arquivos) |
| Ler (fonte) | `menegon-seguros/COMPANY.md` (contexto) |

---

## Task 1: Contexto da empresa e plugins

**Files:**
- Read: `menegon-seguros/COMPANY.md`
- Modify: `wiki/pages/topics/backlog-melhorias.md` (seção Plugins)

- [ ] **Step 1: Ler COMPANY.md para entender o negócio**

```
Read: menegon-seguros/COMPANY.md
```

Objetivo: entender o modelo de negócio, produtos (seguros), canais e métricas-chave para embasar as sugestões de melhoria.

- [ ] **Step 2: Avaliar plugins instalados**

Plugins ativos: `superpowers@5.0.7` e `codex@1.0.3`.

Para cada plugin, responder:
- Existe algum skill/agent do plugin que não está sendo usado mas seria útil?
- A versão está desatualizada?
- Há conflito ou sobreposição com outros ativos?

- [ ] **Step 3: Preencher seção Plugins no backlog**

Editar `wiki/pages/topics/backlog-melhorias.md`, substituir as linhas `—` da seção Plugins com ideias reais. Exemplo de formato:

```markdown
| superpowers | 5.0.7 | Verificar se nova versão disponível; avaliar skill `schedule` para automações | Média | Pendente |
| codex | 1.0.3 | Usar `/codex:review` nos PRs de agentes antes de merge | Baixa | Pendente |
```

- [ ] **Step 4: Commit**

```bash
git add wiki/pages/topics/backlog-melhorias.md
git commit -m "backlog: popula seção plugins"
```

---

## Task 2: Agentes — Grupo Comercial (6 agentes)

**Agentes:** diretor-comercial, gerente-comercial, especialista-renovacao, especialista-seguro-novo, hunter-cross-sell, qualificador-leads

**Files:**
- Read: `menegon-seguros/agents/diretor-comercial/AGENTS.md`
- Read: `menegon-seguros/agents/gerente-comercial/AGENTS.md`
- Read: `menegon-seguros/agents/especialista-renovacao/AGENTS.md`
- Read: `menegon-seguros/agents/especialista-seguro-novo/AGENTS.md`
- Read: `menegon-seguros/agents/hunter-cross-sell/AGENTS.md`
- Read: `menegon-seguros/agents/qualificador-leads/AGENTS.md`
- Modify: `wiki/pages/topics/backlog-melhorias.md`

- [ ] **Step 1: Ler os 6 AGENTS.md em paralelo**

Para cada arquivo, anotar:
- Quais ferramentas/skills o agente usa? Há lacunas óbvias?
- O prompt de sistema é específico o suficiente ou muito genérico?
- O agente tem critérios de saída claros?
- Há sobreposição de responsabilidade com outro agente?

- [ ] **Step 2: Preencher 6 linhas na seção Agentes do backlog**

Para cada agente, adicionar pelo menos uma ideia concreta. Exemplos de padrões a buscar:

| Padrão observado no AGENTS.md | Sugestão típica |
|-------------------------------|-----------------|
| Sem skill de escrita no CRM | Adicionar `monday-crm-write` às ferramentas |
| Critério de qualificação vago | Definir score numérico mínimo |
| Prompt sem exemplos de saída | Adicionar few-shot examples |
| Dependência implícita de outro agente | Documentar handoff explicitamente |

- [ ] **Step 3: Commit**

```bash
git add wiki/pages/topics/backlog-melhorias.md
git commit -m "backlog: popula agentes grupo comercial (6)"
```

---

## Task 3: Agentes — Grupo Marketing/Conteúdo (4 agentes)

**Agentes:** cmo, analista-campanhas, criador-conteudo, especialista-inbound

**Files:**
- Read: `menegon-seguros/agents/cmo/AGENTS.md`
- Read: `menegon-seguros/agents/analista-campanhas/AGENTS.md`
- Read: `menegon-seguros/agents/criador-conteudo/AGENTS.md`
- Read: `menegon-seguros/agents/especialista-inbound/AGENTS.md`
- Modify: `wiki/pages/topics/backlog-melhorias.md`

- [ ] **Step 1: Ler os 4 AGENTS.md em paralelo**

Focos específicos para este grupo:
- CMO: tem visão estratégica suficiente? Acessa dados de performance?
- Analista de campanhas: integração com fontes de dados reais?
- Criador de conteúdo: tem diretrizes de tom de voz da marca?
- Especialista inbound: funil definido? Handoff para qualificador-leads?

- [ ] **Step 2: Preencher 4 linhas na seção Agentes**

- [ ] **Step 3: Commit**

```bash
git add wiki/pages/topics/backlog-melhorias.md
git commit -m "backlog: popula agentes grupo marketing (4)"
```

---

## Task 4: Agentes — Grupo Análise e Monitoramento (7 agentes)

**Agentes:** analista-churn, executor-retencao, analista-forecast, monitor-crm, analista-nps, analista-pipeline, analista-performance

**Files:**
- Read: `menegon-seguros/agents/analista-churn/AGENTS.md`
- Read: `menegon-seguros/agents/executor-retencao/AGENTS.md`
- Read: `menegon-seguros/agents/analista-forecast/AGENTS.md`
- Read: `menegon-seguros/agents/monitor-crm/AGENTS.md`
- Read: `menegon-seguros/agents/analista-nps/AGENTS.md`
- Read: `menegon-seguros/agents/analista-pipeline/AGENTS.md`
- Read: `menegon-seguros/agents/analista-performance/AGENTS.md`
- Modify: `wiki/pages/topics/backlog-melhorias.md`

- [ ] **Step 1: Ler os 7 AGENTS.md em paralelo**

Focos específicos para este grupo:
- Agentes de análise: as métricas usadas são concretas e mensuráveis?
- Monitor-CRM: frequência de disparo definida? Limiar de alerta configurável?
- Executor-retencao: tem autonomia de ação ou só recomenda?
- Forecast: metodologia documentada? Margem de erro aceitável definida?

- [ ] **Step 2: Preencher 7 linhas na seção Agentes**

- [ ] **Step 3: Commit**

```bash
git add wiki/pages/topics/backlog-melhorias.md
git commit -m "backlog: popula agentes grupo análise (7)"
```

---

## Task 5: Skills — Grupo CRM e Dados (5 skills)

**Skills:** monday-crm-query, monday-crm-write, forecast-ponderado, analise-churn, analise-nps

**Files:**
- Read: `menegon-seguros/skills/monday-crm-query/SKILL.md`
- Read: `menegon-seguros/skills/monday-crm-write/SKILL.md`
- Read: `menegon-seguros/skills/forecast-ponderado/SKILL.md`
- Read: `menegon-seguros/skills/analise-churn/SKILL.md`
- Read: `menegon-seguros/skills/analise-nps/SKILL.md`
- Modify: `wiki/pages/topics/backlog-melhorias.md`

- [ ] **Step 1: Ler as 5 SKILL.md em paralelo**

Para cada skill, avaliar:
- O trigger de uso está claro?
- Os outputs são padronizados (formato de retorno definido)?
- Há dependências não documentadas?
- A skill é testável de forma isolada?

- [ ] **Step 2: Preencher 5 linhas na seção Skills**

- [ ] **Step 3: Commit**

```bash
git add wiki/pages/topics/backlog-melhorias.md
git commit -m "backlog: popula skills grupo CRM/dados (5)"
```

---

## Task 6: Skills — Grupo Comercial e Retenção (5 skills)

**Skills:** auditoria-pipeline, cross-sell-hunt, plano-retencao, qualificacao-lead, abordagem-comercial

**Files:**
- Read: `menegon-seguros/skills/auditoria-pipeline/SKILL.md`
- Read: `menegon-seguros/skills/cross-sell-hunt/SKILL.md`
- Read: `menegon-seguros/skills/plano-retencao/SKILL.md`
- Read: `menegon-seguros/skills/qualificacao-lead/SKILL.md`
- Read: `menegon-seguros/skills/abordagem-comercial/SKILL.md`
- Modify: `wiki/pages/topics/backlog-melhorias.md`

- [ ] **Step 1: Ler as 5 SKILL.md em paralelo**

- [ ] **Step 2: Preencher 5 linhas na seção Skills**

- [ ] **Step 3: Commit**

```bash
git add wiki/pages/topics/backlog-melhorias.md
git commit -m "backlog: popula skills grupo comercial/retenção (5)"
```

---

## Task 7: Skills — Grupo Conteúdo e Crescimento (4 skills)

**Skills:** analise-campanhas, nutricao-lead, criacao-conteudo, segmentacao-carteira

**Files:**
- Read: `menegon-seguros/skills/analise-campanhas/SKILL.md`
- Read: `menegon-seguros/skills/nutricao-lead/SKILL.md`
- Read: `menegon-seguros/skills/criacao-conteudo/SKILL.md`
- Read: `menegon-seguros/skills/segmentacao-carteira/SKILL.md`
- Modify: `wiki/pages/topics/backlog-melhorias.md`

- [ ] **Step 1: Ler as 4 SKILL.md em paralelo**

- [ ] **Step 2: Preencher 4 linhas na seção Skills**

- [ ] **Step 3: Commit**

```bash
git add wiki/pages/topics/backlog-melhorias.md
git commit -m "backlog: popula skills grupo conteúdo/crescimento (4)"
```

---

## Task 8: Revisão final e priorização

**Files:**
- Modify: `wiki/pages/topics/backlog-melhorias.md`

- [ ] **Step 1: Ler o backlog completo**

```
Read: wiki/pages/topics/backlog-melhorias.md
```

- [ ] **Step 2: Definir prioridades**

Para cada linha com `Prioridade: —`, definir Alta / Média / Baixa com base em:
- **Alta:** impacto direto em receita ou retenção, ou bloqueia outro ativo
- **Média:** melhora qualidade/consistência de um ativo relevante
- **Baixa:** nice-to-have, refinamento, documentação

- [ ] **Step 3: Atualizar data de última atualização**

No rodapé do backlog, atualizar:
```markdown
*Última atualização: YYYY-MM-DD*
```

- [ ] **Step 4: Commit final**

```bash
git add wiki/pages/topics/backlog-melhorias.md
git commit -m "backlog: prioridades definidas, populamento completo"
```
