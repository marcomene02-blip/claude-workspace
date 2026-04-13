---
name: Análise de Churn
description: Calcular o Health Score de clientes da carteira ativa e classificar por risco de não-renovação.
slug: analise-churn
schema: agentcompanies/v1
version: 1.0.0
---

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
