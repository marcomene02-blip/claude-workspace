---
name: Auditoria de Pipeline
description: Verificar higiene, saúde e cobertura de meta do pipeline de Renovação e Seguro Novo no Monday CRM.
slug: auditoria-pipeline
schema: agentcompanies/v1
version: 1.0.0
---

Skill de health check do pipeline comercial. Detecta problemas de dados, deals estagnados e calcula cobertura de meta.

## Quando usar

**Quem invoca:** `analista-pipeline`

**Acionar quando:**
- Semanalmente, antes do standup comercial (segunda-feira de manhã)
- O agente `monitor-crm` emite alerta de Pipeline Seguro Novo (Dimensão 3)
- O diretor comercial solicita um relatório de pipeline

**Não acionar quando:**
- O objetivo for analisar NPS ou churn — use `analista-nps`
- Já foi executada nas últimas 24h sem mudanças no pipeline

## Checklist de higiene (por deal)

- [ ] Corretor responsável atribuído (`person`)
- [ ] Data de vencimento preenchida (`date_mks7vvn8`)
- [ ] Prêmio preenchido (`numeric_mks5gh0b` ou `numeric_mkvv8v53`)
- [ ] Produto definido (`dropdown_mm09hks6`)
- [ ] Estágio compatível com última movimentação
- [ ] Não está vencido sem status final (Renovado/Não Renovado)

## Indicadores de estagnação

- Deal sem movimentação há 7+ dias em qualquer estágio = alerta
- Deal sem movimentação há 14+ dias = crítico, escalar para Gerente

## Cálculo de cobertura de meta

```
Cobertura = Σ(Prêmio Líquido dos deals ativos) / Meta Mensal

Verde:  ≥ 3× a meta
Amarelo: 2–3× a meta
Vermelho: < 2× a meta
```

## Pipeline Health Score

| Dimensão | Meta | Peso |
|---|---|---|
| Cobertura de meta | ≥ 3× | 30% |
| % deals com dados completos | ≥ 90% | 25% |
| % deals sem estagnação | ≥ 80% | 25% |
| Distribuição equilibrada por estágio | Sim | 20% |

## Saída esperada

```
PIPELINE HEALTH CHECK — [data]

Renovação: X deals | R$ X.XXX total
  Higiene: XX% completos
  Estagnados: X deals (XX%)
  Cobertura meta: X.Xx

Seguro Novo: X deals | R$ X.XXX total
  Higiene: XX% completos
  Estagnados: X deals (XX%)

PROBLEMAS ENCONTRADOS:
1. X deals sem corretor atribuído → [lista]
2. X deals vencidos sem status final → [lista]
3. X deals críticos estagnados → [lista]

Health Score: XX/100 [Verde/Amarelo/Vermelho]
```
