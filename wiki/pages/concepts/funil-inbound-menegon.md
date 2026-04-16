---
title: Funil Inbound — Menegon Seguros
type: concept
created: 2026-04-15
tags: [funil, inbound, crm, handoff]
---

# Funil Inbound — Menegon Seguros

## Visão geral

Lead entra → qualificação BANT → nurturing (se morno) → handoff ao especialista (se quente) → proposta → fechamento → cliente.

## Estágios do funil

| Estágio | Status Monday | Score | Próxima ação | Agente responsável | SLA |
|---|---|---|---|---|---|
| Novo | lead-novo | — | Qualificar em 24h | qualificacao-inbound-menegon | 24h |
| Quente | Quente | 8–10 | Encaminhar ao Especialista imediatamente | qualificador-leads | Imediato |
| Morno | Morno | 5–7 | Iniciar cadência de nurturing 14 dias | nurturing-inbound-menegon | D0 = hoje |
| Frio | Frio | 0–4 | Arquivar com motivo | qualificador-leads | — |
| Em nurturing | Morno (nurturing) | 5–7 | Cadência D0/D3/D7/D10/D14 | nurturing-inbound-menegon | Conforme cadência |
| Handoff comercial | Em Cotação | ≥8 | Especialista envia cotação | especialista-seguro-novo / especialista-renovacao | 2h |
| Proposta enviada | Follow-up | — | Follow-up em 3 dias | especialista | 3 dias |
| Ganho | Renovado / Emitido | — | Criar apólice no board Apólices | — | — |
| Perdido | Não Renovado / Arquivado | — | Mover para base fria | — | — |

## Critérios de handoff (morno → especialista)

Um lead em nurturing avança para especialista quando:
1. Responde positivamente em qualquer etapa da cadência, OU
2. Pede cotação explicitamente, OU
3. Aceita conversar / agendar

## Campos obrigatórios no board Leads (9332203913)

| Campo | Valor esperado | Preenchido por |
|---|---|---|
| Nome | Nome completo | Form do site / WhatsApp |
| Produto | Auto/Residencial/Vida/Empresarial | Form do site |
| Contato | WhatsApp ou email | Form do site |
| CEP | CEP do imóvel/veículo | Form do site |
| Origem | site/whatsapp/indicação | n8n (webhook) |
| Persona estimada | Motorista PF / Família casa própria / MEI / 30-45 família | n8n (heurística por produto) |
| Score BANT | 0–10 | qualificacao-inbound-menegon |
| Status | lead-novo / Quente / Morno / Frio | qualificacao-inbound-menegon |
| Tag nurturing | [nurturing-D0] ... [nurturing-D14] | nurturing-inbound-menegon |
| Data captura | ISO date | n8n (webhook) |

## Mapeamento de personas por produto

| Produto selecionado | Persona estimada (heurística n8n) |
|---|---|
| Auto | Motorista PF |
| Residencial | Família com casa própria |
| Empresarial | MEI / Empresário |
| Vida / Previdência | 30-45 anos com família |
| Outro / Múltiplos | ICP genérico |

## Métricas do funil (para analise-conversao-inbound-menegon)

- **Taxa de qualificação:** leads qualificados / leads novos (meta: >80%)
- **Taxa de morno→quente:** leads que avançam na cadência / leads mornos (meta: >30%)
- **CPL (Custo por Lead):** investimento / leads novos (referência quando houver mídia paga)
- **Taxa de conversão total:** clientes ganhos / leads novos (meta: >15%)
- **Tempo médio de ciclo:** data captura → data fechamento (referência: <30 dias para mornos)
