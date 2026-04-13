---
name: Forecast Ponderado
description: Calcular forecast de receita com três cenários (pessimista, provável, otimista) com base no pipeline real do Monday CRM.
slug: forecast-ponderado
schema: agentcompanies/v1
version: 1.0.0
---

Skill de cálculo de forecast ponderado por estágio do funil. Produz três cenários de receita para embasar decisões comerciais.

## Método de cálculo

### Passo 1 — Coleta

Buscar todos os deals ativos nos boards Renovação (9427535861) e Seguro Novo (9332203907), filtrados pelo período de interesse (mês corrente + seguinte).

### Passo 2 — Pesos por estágio

| Estágio | Renovação | Seguro Novo |
|---|---|---|
| Atualizar Cadastro / Prospecção | 15% | 10% |
| Em Cotação | 35% | 25% |
| Follow-up | 55% | 40% |
| Em Análise/Aprovação | 80% | 70% |

### Passo 3 — Valor ponderado por deal

`Valor Ponderado = Prêmio Líquido × Peso do Estágio`

### Passo 4 — Cenários

| Cenário | Multiplicador | Interpretação |
|---|---|---|
| Pessimista | × 0.70 | Conversão 30% abaixo da média histórica |
| Provável | × 1.00 | Conversão dentro da média histórica |
| Otimista | × 1.15 | Conversão 15% acima da média histórica |

### Passo 5 — Saída

```
FORECAST SEMANAL — [data]

Renovação
  Pessimista: R$ X.XXX
  Provável:   R$ X.XXX
  Otimista:   R$ X.XXX

Seguro Novo
  Pessimista: R$ X.XXX
  Provável:   R$ X.XXX
  Otimista:   R$ X.XXX

TOTAL
  Pessimista: R$ X.XXX
  Provável:   R$ X.XXX
  Otimista:   R$ X.XXX

Meta do mês: R$ X.XXX
Gap (cenário provável): R$ X.XXX [acima/abaixo]

TOP 5 deals que mais impactam o forecast:
1. [Cliente] — R$ X.XXX — [Estágio] — [Vencimento]
...
```

## Regras críticas

- Excluir deals sem prêmio preenchido (registrar como "dados incompletos")
- Excluir deals nos estágios "Renovado" e "Não Renovado"
- Nunca apresentar apenas um cenário
