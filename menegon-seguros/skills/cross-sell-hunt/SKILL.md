---
name: Cross-sell Hunt
description: Identificar gaps de produto na carteira ativa e calcular o valor esperado de cada oportunidade de cross-sell.
slug: cross-sell-hunt
schema: agentcompanies/v1
version: 1.0.0
---

> **Config:** leia `menegon-seguros/config/thresholds/cross-sell-hunt.yaml` no início da execução para obter os thresholds atuais. Os valores neste documento são apenas referência inicial — o YAML tem precedência.

Skill para mapear oportunidades de cross-sell na base de clientes ativos. Produz lista priorizada por valor esperado com plano de abordagem.

## Quando usar

- **Agente invocador:** `hunter-cross-sell`
- **Cadência:** toda segunda-feira de manhã (execução semanal)
- **Destino da saída:** atualização no item do cliente no Monday CRM via skill `monday-crm-write`
- **Exclusão:** não processar clientes que já foram abordados nos últimos 30 dias — evita repetir o mesmo top 10 da semana anterior

## Fontes de dados

- Clientes: board 9332203920 (filtro Ativo)
- Apólices: board 9749857183 (histórico completo de produtos por cliente)

## Matriz de fit de produtos

| Cliente tem | Oportunidade imediata | Oportunidade secundária |
|---|---|---|
| Auto | Residencial, Vida | Previdência, AP |
| Residencial | Auto, Vida | Condomínio |
| Vida | Previdência | AP, RC |
| Auto + Residencial | Vida | Previdência |
| Empresarial | Vida em Grupo, RC | Garantia, Transporte |
| Consórcio | Vida, Residencial | Auto |

## Cálculo de valor esperado

```
Valor Esperado = Prêmio Estimado do Produto × Probabilidade de Fechar

Probabilidades base:
  Indicação direta do cliente = 60%
  Perfil de alto fit = 40%
  Fit moderado = 20%
```

## Prêmios médios estimados por produto

| Produto | Prêmio Médio Estimado |
|---|---|
| Auto | R$ 2.800/ano |
| Residencial | R$ 900/ano |
| Vida Individual | R$ 1.200/ano |
| Previdência | R$ 3.600/ano |
| Vida em Grupo | R$ 4.800/ano (PJ) |
| Empresarial | R$ 5.500/ano |

## Saída esperada (top 10 por semana)

```
OPORTUNIDADES DE CROSS-SELL — [data]

1. [Nome do cliente]
   Tem: Auto (Porto Seguro, vence [data])
   Oportunidade: Residencial
   Valor esperado: R$ 360/ano (40% prob.)
   Corretor: [Nome]
   Script sugerido: "Oi [Nome], vi que seu auto está renovado.
   Você já tem proteção pra sua casa também? Consigo uma cotação
   em menos de 5 minutos..."
```
