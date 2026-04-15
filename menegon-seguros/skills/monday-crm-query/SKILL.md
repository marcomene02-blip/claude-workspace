---
name: Monday CRM Query
description: Consultar dados do Monday CRM da Menegon Seguros — boards, items, colunas e filtros.
slug: monday-crm-query
schema: agentcompanies/v1
version: 1.0.0
---

Habilidade de leitura do Monday CRM. Use esta skill para buscar dados de qualquer board antes de analisar ou agir.

## Boards disponíveis

| Board | ID | Uso principal |
|---|---|---|
| Renovação | 9427535861 | Pipeline de renovações ativas |
| Seguro Novo | 9332203907 | Pipeline de novos seguros |
| Leads | 9332203913 | Base histórica de leads |
| Clientes | 9332203920 | Carteira ativa (filtro: `text_mkrtez0s = "Ativo"`) |
| Apólices | 9749857183 | Histórico completo de apólices |
| NPS | 9751082146 | Pesquisas de satisfação |
| Sinistro | 18026494883 | Histórico de sinistros |
| Agendamentos | 18398959154 | Agenda de follow-ups |

## Colunas-chave (Renovação)

- `status` — estágio do funil
- `date_mks7vvn8` — Data de Vencimento
- `date_mks722ne` — Prazo da Tarefa
- `person` — Corretor Responsável
- `numeric_mks5gh0b` — Prêmio Atual
- `numeric_mkvv8v53` — Prêmio Líquido
- `numeric_mkv9sywr` — Comissão
- `text_mks7z632` — Seguradora
- `dropdown_mm09hks6` — Produto

## Formato de saída

Toda consulta deve retornar em um dos dois modos:

### Modo `list` (padrão)
Array de objetos com os campos selecionados. Usar quando o agente precisa processar item por item.

```json
[
  { "id": "123456789", "name": "Cliente XYZ", "status": "Em Cotação", "date_mks7vvn8": "2026-05-10", "numeric_mks5gh0b": 1200 },
  ...
]
```

### Modo `summary`
Contagem + top N itens. Usar quando o agente precisa de visão agregada (ex.: quantos deals por estágio).

```
Board: Renovação
Total de itens: 47
Por status:
  Em Cotação: 12
  Follow-up: 18
  Em Análise: 8
  Atualizar Cadastro: 9

Top 5 por prêmio líquido:
  [Cliente A] — R$ 3.200 — Follow-up — vence 2026-04-28
  ...
```

Especificar o modo desejado ao invocar a skill. Se omitido, usar `list`.

## Instruções de uso

1. Sempre filtrar por período relevante quando buscar vencimentos
2. No board Clientes, sempre aplicar filtro `text_mkrtez0s = "Ativo"`
3. Usar paginação para boards grandes (Apólices tem 8.459 itens). Exemplo de query com cursor:
   - Primeira página: `boards(ids: 9749857183) { items_page(limit: 100) { cursor items { id name } } }`
   - Páginas seguintes: `boards(ids: 9749857183) { items_page(limit: 100, cursor: "CURSOR_AQUI") { cursor items { id name } } }`
   - Repetir até `cursor` retornar `null`
   - Nunca buscar sem `limit` em boards com > 500 itens — a API trunca silenciosamente
4. Ler o Mapa de Conhecimento (doc_id 39560051) antes de interpretar dados desconhecidos
