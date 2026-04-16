---
title: Workflow WAT — Lead Capture (Site → Monday CRM)
type: runbook
created: 2026-04-15
n8n_workflow_id: PENDENTE — API key com escopo mcp-server-api retorna 404 no management endpoint; criar workflow manualmente no n8n UI
webhook_url: https://menegon.app.n8n.cloud/webhook/lead-capture
monday_board: "9332203913"
tags: [n8n, inbound, lead, monday, webhook]
---

# WAT: Lead Capture — Site → Monday CRM

## Propósito

Capturar leads submetidos pelo formulário de cotação em `Sites/index.html` e criar itens no board Monday Leads (9332203913) com enriquecimento automático de persona e origem.

## Fluxo

```
Sites/index.html (form POST)
    │
    ▼
n8n Webhook /lead-capture
    │
    ▼
Code Node: validação + enriquecimento
    │  (adiciona persona_estimada, origem, data_captura)
    ▼
Monday.com: cria item no board Leads (9332203913)
    │
    ▼
Resposta ao form: {"status":"ok"}
```

## Configuração

- **Webhook URL:** `https://menegon.app.n8n.cloud/webhook/lead-capture`
- **Método:** POST
- **Content-Type:** application/json
- **Board Monday:** 9332203913 (Leads)
- **Grupo Monday:** `group_mm00cbwc` (Leads)

## Status de criação do workflow n8n

> **PENDENTE — criar manualmente no n8n UI**
>
> A API key configurada em `.mcp.json` tem audience `mcp-server-api` e retorna HTTP 404
> no endpoint `/api/v1/workflows`. O MCP health check conecta mas as chamadas de
> management falham. Para criar o workflow:
>
> 1. Acesse `https://menegon.app.n8n.cloud/`
> 2. Importe o workflow abaixo (JSON) ou crie manualmente os 4 nós
> 3. Ative o workflow
> 4. Atualize `n8n_workflow_id` neste runbook

## Definição do workflow n8n (JSON para importação)

```json
{
  "name": "wat-lead-capture",
  "nodes": [
    {
      "id": "node1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "parameters": {
        "httpMethod": "POST",
        "path": "lead-capture",
        "responseMode": "responseNode"
      }
    },
    {
      "id": "node2",
      "name": "Validate and Enrich",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [460, 300],
      "parameters": {
        "jsCode": "const body = $input.first().json.body || $input.first().json;\nconst required = ['produto', 'nome', 'contato', 'email', 'cep'];\nfor (const field of required) {\n  if (!body[field]) {\n    throw new Error(`Campo obrigatorio ausente: ${field}`);\n  }\n}\nconst personaMap = {\n  'Auto': 'Motorista PF (Rafael)',\n  'Residencial': 'Familia com casa propria (Sergio & Ana)',\n  'Empresarial': 'MEI / Empresario (Mauricio)',\n  'Vida': '30-45 anos com familia',\n  'Previdencia': '30-45 anos com familia'\n};\nreturn [{\n  json: {\n    nome: body.nome,\n    contato: body.contato,\n    email: body.email,\n    cep: body.cep,\n    produto: body.produto,\n    origem: body.origem || 'site',\n    persona_estimada: personaMap[body.produto] || 'ICP generico',\n    status_inicial: 'lead-novo',\n    data_captura: new Date().toISOString()\n  }\n}];"
      }
    },
    {
      "id": "node3",
      "name": "Monday Create Item",
      "type": "n8n-nodes-base.mondayCom",
      "typeVersion": 1,
      "position": [680, 300],
      "parameters": {
        "resource": "item",
        "operation": "create",
        "boardId": "9332203913",
        "groupId": "group_mm00cbwc",
        "name": "={{ $json.nome }} — {{ $json.produto }}",
        "columnValues": "={{ JSON.stringify({ email1jaru4e2: { email: $json.email, text: $json.email }, lead_phone: { phone: $json.contato, countryShortName: 'BR' }, long_text_mm2cb05d: { text: 'Produto: ' + $json.produto + ' | Origem: ' + $json.origem + ' | Persona: ' + $json.persona_estimada + ' | Capturado em: ' + $json.data_captura }, lead_status: { label: 'Novo Lead' } }) }}"
      }
    },
    {
      "id": "node4",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [900, 300],
      "parameters": {
        "respondWith": "json",
        "responseBody": "{\"status\":\"ok\",\"message\":\"Obrigado! Entraremos em contato em breve.\"}"
      }
    }
  ],
  "connections": {
    "Webhook": { "main": [[{"node": "Validate and Enrich", "type": "main", "index": 0}]] },
    "Validate and Enrich": { "main": [[{"node": "Monday Create Item", "type": "main", "index": 0}]] },
    "Monday Create Item": { "main": [[{"node": "Respond to Webhook", "type": "main", "index": 0}]] }
  },
  "settings": { "executionOrder": "v1" }
}
```

## Campos enviados pelo form

| Campo | Tipo | Descrição |
|---|---|---|
| `produto` | string | Auto/Residencial/Vida/Empresarial |
| `nome` | string | Nome completo do lead |
| `contato` | string | Telefone com DDD |
| `email` | string | Email |
| `cep` | string | CEP |
| `origem` | string | Sempre `"site"` neste webhook |

## Campos enriquecidos pelo n8n

| Campo | Como é calculado |
|---|---|
| `persona_estimada` | Mapeamento produto → persona |
| `origem` | Sempre `"site"` |
| `data_captura` | `new Date().toISOString()` |
| `status_inicial` | Sempre `"lead-novo"` |

## Colunas Monday usadas

| Column ID | Título | Tipo | Valor enviado |
|---|---|---|---|
| `email1jaru4e2` | E-mail | email | `{ email, text }` |
| `lead_phone` | Celular | phone | `{ phone, countryShortName: "BR" }` |
| `long_text_mm2cb05d` | Observações | long_text | Produto + Origem + Persona + Data |
| `lead_status` | Status | status | `"Novo Lead"` (id 5) |

## Mapa de persona por produto

| Produto | Persona |
|---|---|
| Auto | Motorista PF (Rafael) |
| Residencial | Família com casa própria (Sérgio & Ana) |
| Empresarial | MEI / Empresário (Maurício) |
| Vida / Previdência | 30-45 anos com família |

## Extensão futura

Quando o email transacional estiver configurado (Resend/Brevo):
1. Adicionar nó **Email** após o Monday node
2. Enviar confirmação para `{{$json.email}}` com número do protocolo
3. Nenhuma mudança necessária no site ou no formulário

## Troubleshooting

- **Lead não aparece no Monday:** verificar se o workflow está ativo no n8n; verificar credencial Monday
- **Erro 422 no webhook:** algum campo obrigatório ausente — ver nó Code no n8n
- **Formulário não envia:** verificar se a URL do webhook está correta no `Sites/index.html`
- **API key n8n 404:** a key atual tem audience `mcp-server-api`; para uso via API REST gerar nova key em Settings → API → Create API Key com escopo completo
