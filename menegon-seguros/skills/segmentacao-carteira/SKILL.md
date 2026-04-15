---
name: Segmentação de Carteira
description: Aplicar filtros padronizados na carteira ativa de clientes para segmentar por produto, NPS, prêmio e perfil de risco. Base para cross-sell, retenção e campanhas.
slug: segmentacao-carteira
schema: agentcompanies/v1
version: 1.0.0
---

Skill para segmentar a carteira de clientes ativos da Menegon Seguros. Produz listas filtradas prontas para uso em campanhas, cross-sell e análise de risco.

## Quando usar

| Agente | Gatilho |
|---|---|
| `cmo` | Semanalmente, antes do planejamento de campanhas trimestrais |
| `hunter-cross-sell` | Sob demanda, para filtrar alvos de cross-sell por segmento |
| `analista-campanhas` | Ao segmentar resultados de campanha por perfil de cliente |

**Pré-requisito — risco de churn:** os health scores devem ser calculados pela skill `analise-churn` antes de usar o segmento "Por risco de churn". Se os scores estiverem ausentes para algum cliente, classifique-o como **"Score ausente"** (não omita o cliente da lista).

## Filtro base obrigatório

Sempre iniciar com clientes ativos:
- **Board**: Clientes (9332203920)
- **Filtro obrigatório**: `text_mkrtez0s = "Ativo"`

## Segmentos padrão

### Por quantidade de produtos

| Segmento | Critério | Uso principal |
|---|---|---|
| Monoproduto | 1 apólice ativa | Cross-sell prioritário |
| Biproduto | 2 apólices ativas | Cross-sell secundário |
| Multiproduto (3+) | 3+ apólices ativas | Fidelização, indicação |

**Fonte**: cruzar com Apólices (9749857183), contar apólices por cliente com status ativo.

### Por produto principal

| Segmento | Filtro no board Apólices |
|---|---|
| Auto | `dropdown_produto = "Auto"` |
| Residencial | `dropdown_produto = "Residencial"` |
| Vida Individual | `dropdown_produto = "Vida Individual"` |
| Vida em Grupo | `dropdown_produto = "Vida em Grupo"` |
| Empresarial | `dropdown_produto = "Empresarial"` |
| Outros | Demais categorias |

### Por NPS

| Segmento | Critério | Uso principal |
|---|---|---|
| Promotor | Última nota 9–10 no board NPS (9751082146) | Pedir indicação |
| Neutro | Última nota 7–8 | Fidelização + upsell |
| Detrator | Última nota 0–6 | Plano de retenção imediato |
| Sem NPS | Sem resposta nos últimos 12 meses | Disparar pesquisa de satisfação |

### Por faixa de prêmio anual

| Segmento | Faixa | Uso principal |
|---|---|---|
| Alta valor | Prêmio anual > R$ 5.000 | Marco é contato direto |
| Médio valor | R$ 2.000 – R$ 5.000 | Foco especial em renovação |
| Base | < R$ 2.000 | Automação e eficiência |

**Fonte**: coluna `numeric_mks5gh0b` (Prêmio Atual) no board Renovação, ou somar apólices no board Apólices.

### Por risco de churn

| Segmento | Critério |
|---|---|
| Crítico | Health Score < 40 (ver skill analise-churn) |
| Em Risco | Health Score 40–60 |
| Monitorar | Health Score 61–80 |
| Saudável | Health Score > 80 |

### Por corretor responsável

Usar `person` (ID Monday) nos boards de Renovação e Seguro Novo para filtrar por:
- Marco (77698859)
- Neto (77007724)
- Daniele (77510156)
- Amanda (77510167)
- Giovana (77698858)
- Daniel (99085700)

## Combinações mais usadas

| Objetivo | Segmento combinado |
|---|---|
| Cross-sell semanal | Ativo + Monoproduto + Saudável (>80) |
| Campanha de indicação | Ativo + Promotor (NPS 9–10) |
| Lista de retenção urgente | Ativo + Crítico (score <40) |
| Campanha de vida para auto | Ativo + Auto + sem Vida + prêmio > R$1.500 |
| Alta valor em risco | Ativo + prêmio >R$5.000 + Detrator ou score <60 |

## Saída esperada

```
SEGMENTO: [nome do segmento]
Data: [data]
Filtros aplicados: [lista dos critérios]

Total de clientes: XX

| Nome | Produto(s) | Prêmio Anual | Corretor | Obs |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

Distribuição:
  Por corretor: Neto (XX) | Daniele (XX) | Amanda (XX) | Giovana (XX) | Daniel (XX)
  Por produto principal: Auto (XX%) | Residencial (XX%) | ...
```
