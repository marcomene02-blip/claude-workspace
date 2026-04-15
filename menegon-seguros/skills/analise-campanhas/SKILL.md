---
name: Análise de Campanhas
description: Calcular KPIs de campanhas de marketing — leads gerados, conversão, ROI — e diagnosticar o que está funcionando.
slug: analise-campanhas
schema: agentcompanies/v1
version: 1.0.0
---

Skill para medir e diagnosticar performance de campanhas de marketing. Conecta dados de leads/CRM com resultados comerciais.

## Quando usar

Invocar via agente `analista-campanhas` nos seguintes gatilhos:

1. **Toda segunda-feira** — monitoramento contínuo de campanhas ativas.
2. **Ao encerrar qualquer campanha** — relatório final de performance.
3. **Solicitação de `monitor-crm` ou CMO** — revisão de performance sob demanda.

**Requisito mínimo de dados:** a campanha deve ter pelo menos 1 lead registrado. Sem isso, a skill encerra sem análise (evita divisão por zero na validação dos dados).

## KPIs calculados

| KPI | Fórmula | Meta de referência |
|---|---|---|
| Leads gerados | Contagem de items novos no período | Definido por campanha |
| Taxa de qualificação | Leads qualificados / Leads totais | ≥ 40% |
| Taxa de conversão | Apólices fechadas / Leads qualificados | ≥ 25% |
| Prêmio gerado | Σ prêmio dos deals fechados da campanha | Definido por campanha |
| ROI | (Prêmio gerado − Custo) / Custo × 100 | ≥ 300% |
| CPL | Custo total / Leads gerados | Referência por canal |

## Fontes de dados

- Leads gerados: board Leads (9332203913) e Seguro Novo (9332203907)
- Conversões: deals fechados com origem rastreável
- Custo: informado manualmente ou extraído de integração

## Diagnóstico por resultado

| Resultado | Hipótese | Ação |
|---|---|---|
| Leads altos, conversão baixa | Problema de qualificação ou abordagem | Revisar critérios de qualificação / script |
| Conversão alta, leads baixos | Canal com bom fit, volume insuficiente | Escalar investimento no canal |
| ROI negativo | CPL alto ou prêmio médio baixo | Redirecionar para produto de maior ticket |

## Saída esperada

```
PERFORMANCE DA CAMPANHA — [Nome] — [período]

Leads gerados: XX
Taxa de qualificação: XX%
Taxa de conversão: XX%
Prêmio gerado: R$ X.XXX
ROI: XXX%

DIAGNÓSTICO:
[O que está funcionando]
[O que não está funcionando]

RECOMENDAÇÃO:
[Manter / Ajustar / Pausar] — [o que mudar]
```
