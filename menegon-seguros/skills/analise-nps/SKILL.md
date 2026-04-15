---
name: Análise de NPS
description: Calcular o score NPS, segmentar respostas em Promotores / Neutros / Detratores e identificar padrões de insatisfação por produto, corretor e seguradora.
slug: analise-nps
schema: agentcompanies/v1
version: 1.0.0
---

Skill para transformar dados do board NPS (9751082146) em inteligência acionável. Produz score, segmentação, análise de padrões e lista de ações por grupo.

## Cálculo do NPS

```
NPS = % Promotores − % Detratores

Promotores:  nota 9–10
Neutros:     nota 7–8
Detratores:  nota 0–6
```

| Faixa NPS | Classificação |
|---|---|
| ≥ 70 | Excelente |
| 50–69 | Bom |
| 0–49 | Precisa de atenção |
| < 0 | Crítico |

**Meta Menegon: NPS ≥ 70**

## Fonte de dados

- Board NPS: 9751082146
- Cruzar com Clientes (9332203920) para identificar produto, prêmio e corretor responsável
- Cruzar com Sinistros (18026494883) para correlacionar sinistro aberto × NPS baixo

## Segmentações obrigatórias

### Por grupo (sempre)
- Promotores (9–10): candidatos a indicação
- Neutros (7–8): oportunidade de upsell e fidelização
- Detratores (0–6): acionar Executor de Retenção imediatamente

### Por produto (quando ≥ 5 respostas por categoria)
- Auto | Residencial | Vida | Empresarial | Outros

### Por corretor responsável
- Compara taxa de detratores por corretor para identificar padrão de atendimento

### Por seguradora
- Qual seguradora gera mais detratores? (indicativo de problemas de sinistro ou renovação)

### Evolução mensal
- Score NPS mês a mês (mínimo últimos 3 meses quando disponível)

## Tamanho mínimo de amostra

Antes de calcular qualquer score, verificar o total de respostas no período:

| Condição | Ação |
|---|---|
| Total de respostas < 5 | Emitir aviso `AMOSTRA INSUFICIENTE` e encerrar (ver template abaixo) |
| Total ≥ 5, mas categoria < 5 | Calcular NPS global; omitir segmentação por produto/corretor para categorias abaixo do mínimo |
| Total ≥ 5, todas as categorias ≥ 5 | Produzir relatório completo |

**Template AMOSTRA INSUFICIENTE:**
```
ANÁLISE DE NPS — [data]

AMOSTRA INSUFICIENTE
Respostas no período: [N] (mínimo exigido: 5)
Score NPS não calculado.

Ação: aguardar novas respostas ou ampliar o período de coleta.
```

## Análise de padrões

**Campo de feedback textual:** coluna `text_mkrtez0s` do board NPS (9751082146).
*(Verificar ID real via MCP Monday se a coluna não retornar dados — pode variar por workspace.)*

Para cada detrator, categorizar o feedback textual em:
- **Preço** — reclamação de valor do prêmio
- **Atendimento** — demora, falta de retorno, corretor
- **Sinistro** — demora ou recusa de sinistro
- **Produto** — cobertura insuficiente

## Saída esperada

```
ANÁLISE DE NPS — [data]

Score NPS: XX ([Excelente/Bom/Atenção/Crítico])
Respostas no período: XX
  Promotores (9–10): XX (XX%)
  Neutros (7–8):     XX (XX%)
  Detratores (0–6):  XX (XX%)

NPS POR PRODUTO:
  Auto:         XX (XX respostas)
  Residencial:  XX (XX respostas)
  Vida:         XX (XX respostas)

NPS POR CORRETOR:
  [Nome]: XX (XX respostas)
  ...

DETRATORES PRIORITÁRIOS (por valor de prêmio anual):
1. [Nome] | Nota: X | Prêmio: R$ X.XXX | Corretor: [Nome]
   Categoria: [Sinistro/Preço/Atendimento/Produto]
   Observação: "[trecho do feedback]"

PROMOTORES PARA PEDIR INDICAÇÃO:
1. [Nome] | Nota: XX | Produto: [Auto] | Corretor: [Nome]

AÇÕES RECOMENDADAS:
- Detratores: encaminhar [N] casos ao Executor de Retenção (ver lista acima)
- Neutros: [ação de upsell ou fidelização sugerida]
- Promotores: solicitar indicação por [canal]
```

## Regras críticas

- Detrator com prêmio acima de R$ 3.000/ano → escalar para Marco diretamente (não apenas para Executor)
  - Prêmio anual = campo `numeric_mks5gh0b` (Prêmio Atual) no board Clientes (9332203920), cruzado pelo nome do cliente
  - Se o campo estiver vazio, tratar como prêmio desconhecido e incluir na lista de escalada com marcação `[prêmio a confirmar]`
- Feedback textual deve ser lido — nunca usar apenas a nota numérica
- NPS sem benchmark de mês anterior não tem valor — sempre comparar com período anterior
- Nunca apresentar NPS como métrica de vaidade: todo relatório termina com ação concreta
