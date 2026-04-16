---
title: Lead Capture — Menegon Seguros
type: entity
created: 2026-04-15
tags: [lead, inbound, site, n8n, monday]
---

# Lead Capture — Menegon Seguros

## O que é

O sistema de captura de leads que conecta o formulário de cotação do site ao Monday CRM. Qualquer visitante que preencher o form em `Sites/index.html` é automaticamente criado como item no board Leads (9332203913), com persona estimada e origem registrados.

## Componentes

| Componente | Localização | Função |
|---|---|---|
| Formulário | `Sites/index.html` (form#cotacao-form) | Interface com o visitante |
| Webhook | n8n `/lead-capture` | Recebe e valida os dados |
| Enriquecimento | n8n Code Node | Adiciona persona, origem, timestamp |
| Destino | Monday board 9332203913 (Leads) | Armazenamento canônico |
| Runbook | `docs/workflows/wat-lead-capture.md` | Documentação operacional |

## Ciclo de vida do lead após captura

1. Lead criado no Monday com `status = Novo Lead`
2. `qualificacao-inbound-menegon` (08:30, Seg-Sex) lê leads novos e aplica BANT
3. Se score 8-10 → status `Quente`, encaminhar ao especialista
4. Se score 5-7 → status `Morno`, entrar na cadência de nurturing
5. Se score 0-4 → status `Frio`, arquivar com motivo

## Canais de entrada de lead (além do site)

Por enquanto, apenas o site está integrado. Futuros canais:
- WhatsApp Business (manual → create item no Monday)
- Indicação (manual → create item no Monday)
- Mídia paga (landing pages com UTM → webhook n8n com origem=utm)
