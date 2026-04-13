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

## Instruções de uso

1. Sempre filtrar por período relevante quando buscar vencimentos
2. No board Clientes, sempre aplicar filtro `text_mkrtez0s = "Ativo"`
3. Usar paginação para boards grandes (Apólices tem 8.459 itens)
4. Ler o Mapa de Conhecimento (doc_id 39560051) antes de interpretar dados desconhecidos
