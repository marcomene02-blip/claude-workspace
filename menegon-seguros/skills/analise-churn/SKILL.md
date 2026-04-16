---
name: Análise de Churn
description: Calcular o Health Score de clientes da carteira ativa e classificar por risco de não-renovação.
slug: analise-churn
schema: agentcompanies/v1
version: 1.0.0
---

> **Config:** leia `menegon-seguros/config/thresholds/analise-churn.yaml` no início da execução para obter os thresholds atuais. Os valores neste documento são apenas referência inicial — o YAML tem precedência.

Skill para calcular risco de churn na carteira Menegon Seguros. Produz lista priorizada de clientes com score, fatores de risco e classificação de urgência.

## Modelo de Health Score (0–100)

| Dimensão | Peso | Como calcular |
|---|---|---|
| Vencimento próximo | 30% | ≤ 30 dias sem cotação = risco alto |
| Histórico NPS | 25% | Detrator (0–6) = risco alto; sem resposta 12m = risco médio |
| Sinistros | 20% | 2+ no ano ou sinistro aberto = risco alto |
| Engajamento | 15% | Sem interação 60+ dias = risco médio |
| Monoproduto | 10% | 1 produto = risco baixo adicional |

**Score alto = cliente saudável. Score baixo = cliente em risco.**

### Fonte de dados por dimensão

| Dimensão | Campo/Board |
|---|---|
| Vencimento próximo | Campo `date_mkn8bwga` (data de vencimento) no board Renovação (9427535861) |
| Histórico NPS | Board NPS (9751082146), filtrado por cliente |
| Sinistros | Board Sinistros (18026494883), filtrado por cliente |
| Engajamento | Campo `last_updated_at` do item no board Clientes (9332203920) — se a última atualização for há 60+ dias, classificar como risco médio |
| Monoproduto | Contar itens ativos no board Apólices (9749857183) com `person` = corretor do cliente; se apenas 1 apólice ativa, classificar como monoproduto |

## Classificação de risco

| Score | Classificação | Prazo de ação |
|---|---|---|
| < 40 | Crítico | 48 horas |
| 40–60 | Em Risco | 7 dias |
| 61–80 | Monitorar | Próxima semana |
| > 80 | Saudável | Rotina normal |

## Fontes de dados

- Clientes: board 9332203920 (filtro `text_mkrtez0s = "Ativo"`)
- NPS: board 9751082146
- Sinistros: board 18026494883
- Renovação: board 9427535861 (para verificar se já tem cotação em andamento)
- Apólices: board 9749857183 (para verificar dimensão Monoproduto — contar apólices ativas por cliente)

## Saída esperada

```
ANÁLISE DE CHURN — [data]

Carteira analisada: X clientes ativos

CRÍTICOS (ação em 48h):
1. [Nome] | Score: XX | Prêmio: R$ X.XXX | Corretor: [Nome]
   Fatores: [NPS 3, sinistro aberto, vencimento em 12 dias]

EM RISCO (ação em 7 dias):
...

Resumo: X críticos | X em risco | X monitorando | X saudáveis
```

### Saída quando não há clientes críticos

```
ANÁLISE DE CHURN — [data]

Carteira analisada: X clientes ativos

NENHUM CLIENTE CRÍTICO identificado neste ciclo.

EM RISCO (ação em 7 dias):
[lista ou "Nenhum"]

MONITORAR:
[lista ou "Nenhum"]

Resumo: 0 críticos | X em risco | X monitorando | X saudáveis
Próxima análise recomendada: [data + 7 dias]
```
