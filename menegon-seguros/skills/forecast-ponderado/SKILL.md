---
name: Forecast Ponderado
description: Calcular forecast de receita com três cenários (pessimista, provável, otimista) com base no pipeline real do Monday CRM.
slug: forecast-ponderado
schema: agentcompanies/v1
version: 1.0.0
---

Skill de cálculo de forecast ponderado por estágio do funil. Produz três cenários de receita para embasar decisões comerciais.

## Quando usar

**Quem invoca:** `analista-forecast`

**Acionar quando:**
- Toda sexta-feira (relatório semanal para o Diretor Comercial)
- Antes de qualquer reunião de planejamento ou revisão de meta
- Quando o `monitor-crm` detecta desvio > 15% na Dimensão 6 (Forecast)

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

### Meta do mês

Ler a meta do mês do **Mapa de Conhecimento** (Monday Docs, doc_id 39560051). Se não estiver registrada, solicitar ao `diretor-comercial` antes de calcular o gap. Nunca usar valor estimado ou do período anterior sem confirmação explícita.

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

### Passo 6 — Calibração (MAPE)

A cada execução, calcular o erro médio absoluto percentual (MAPE) das últimas 4 semanas comparando o cenário **Provável** de cada semana com a receita real (board Apólices 9749857183, prêmios pagos no período):

```
MAPE = média( |Provável_semana_N − Real_semana_N| / Real_semana_N ) × 100
```

| MAPE | Interpretação | Ação |
|---|---|---|
| < 10% | Modelo calibrado | Nenhuma |
| 10–20% | Desvio moderado | Registrar como observação no relatório |
| > 20% | Modelo descalibrado | Alertar `analista-forecast` para revisar multiplicadores |

Incluir o MAPE calculado no rodapé do relatório de forecast.

## Regras críticas

- Excluir deals sem prêmio preenchido (registrar como "dados incompletos")
- Excluir deals nos estágios "Renovado" e "Não Renovado"
- Nunca apresentar apenas um cenário
- Deals criados após o dia 15 do mês corrente: incluir no forecast do mês seguinte, não do corrente (pró-rata distorceria o resultado)
- Deals criados até o dia 15: incluir normalmente no forecast do mês corrente
