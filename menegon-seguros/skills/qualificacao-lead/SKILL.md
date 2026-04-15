---
name: Qualificação de Lead
description: Pontuar e classificar leads com base em perfil, produto, timing e origem. Produzir score e recomendação de próxima ação.
slug: qualificacao-lead
schema: agentcompanies/v1
version: 1.0.0
---

Skill para qualificar leads antes de passá-los ao time comercial. Aplica modelo BANT adaptado ao contexto de seguros.

## Modelo de pontuação (0–10)

| Critério | Peso | Pontuação |
|---|---|---|
| Produto de interesse definido | 2 pts | Sim = 2, Vago = 1, Não = 0 |
| Perfil com fit para o produto | 2 pts | Alto = 2, Médio = 1, Baixo = 0 |
| Timing favorável | 2 pts | Vencendo em 60 dias = 2, Situação nova = 1, Sem urgência = 0 |
| Origem do lead | 2 pts | Indicação = 2, Inbound orgânico = 1, Frio = 0 |
| Contato verificado | 1 pt | WhatsApp válido = 1, Só email = 0, Nenhum = 0 |
| Histórico de cliente Menegon | 1 pt | Cliente anterior = 1, Novo = 0 |

## Classificação

| Score | Classificação | Próxima ação |
|---|---|---|
| 8–10 | Quente | Encaminhar imediatamente ao Especialista correto |
| 5–7 | Morno | Entrar na cadência de nurturing (Especialista Inbound) |
| 0–4 | Frio | Arquivar com motivo registrado |

## Quando usar

**Quem invoca:** `qualificador-leads`

**Acionar quando:** novo lead entra no board Leads (9332203913) com status "Novo" ou "A qualificar".

**Não acionar** para leads já qualificados (status "Quente", "Morno" ou "Frio") — apenas reclassificar se houver mudança relevante de contexto (ex.: cliente indicou novo interesse).

## Registro obrigatório no Monday

Após calcular o score, **antes de encaminhar o lead**, registrar via `monday-crm-write`:

| Campo | O que gravar |
|---|---|
| Coluna de nota/score | Score numérico calculado (ex.: `7`) |
| Update no item | Texto completo da qualificação (copiar saída esperada abaixo) |
| Status | Atualizar para "Quente", "Morno" ou "Frio" conforme classificação |

Para leads **Frios (0–4):** registrar o motivo de descarte no campo de texto do item (ex.: "Frio — sem timing e contato apenas por email") antes de arquivar.

## Saída esperada por lead

```
QUALIFICAÇÃO — [Nome do Lead]
Data: [data]

Score: X/10 — [Quente/Morno/Frio]

Pontuação detalhada:
  Produto definido: X/2 — [Auto / Vago / Nenhum]
  Fit de perfil: X/2 — [PF motorista, 35 anos, carro novo]
  Timing: X/2 — [Seguro vence em 45 dias]
  Origem: X/2 — [Indicação da cliente Maria]
  Contato: X/1 — [WhatsApp verificado]
  Histórico: X/1 — [Novo]

RECOMENDAÇÃO:
  Produto: Auto
  Encaminhar para: [Especialista em Seguro Novo]
  Corretor sugerido: [Nome]

SCRIPT DE ABERTURA:
"Oi [Nome], tudo bem? Sou da Menegon Seguros.
[Nome da Maria] me indicou você — disse que você está
renovando o seguro do seu carro em breve. Posso te
enviar uma cotação rápida pra comparar?"
```
