---
name: Dossiê 360 — Renovação T-15
description: Gera dossiê completo do cliente (apólices ativas e históricas, sinistros, LTV, sinais) para itens da Renovação que vencem em T-15 dias e cola como update no item do Monday.
slug: dossie-renovacao
schema: agentcompanies/v1
version: 1.0.0
---

Skill que entrega ao corretor o contexto 360 do cliente **15 dias antes do vencimento da renovação**, dentro do próprio item da Renovação no Monday. Substitui a coleta manual em 4 boards (Cliente → Apólices → Sinistros → NPS) por um update único e estruturado.

Pré-requisitos: leitura de `menegon-seguros/team.md` (resolução de corretor) e do Mapa de Conhecimento (doc_id 39560051) antes de interpretar dados não óbvios.

## Modos de execução

| Modo | Default | Comportamento |
|---|---|---|
| `relatorio` | sim | Gera o markdown do dossiê e devolve. **Não escreve no Monday.** Usar em dry-run e validação. |
| `executar` | não | Gera o dossiê E cola como update via `create_update` no item da Renovação. Usado pela rotina cloud. |

## Input

```json
{
  "modo": "relatorio" | "executar",
  "renovacao_item_ids": ["123","456"]   // opcional. Se omitido, faz a varredura T-15 automática
}
```

Se `renovacao_item_ids` vier vazio, a skill executa a varredura padrão:

```
board_insights(
  boardId=9427535861,
  aggregations=[{columnId:"name", function:"COUNT_ITEMS"}],
  filters=[
    {columnId:"date_mks7vvn8", operator:"exact", compareValue:"<HOJE+15>"},
    {columnId:"status", operator:"not_any_of", compareValue:["Renovado","Não Renovado"]}
  ]
)
```

E em seguida `get_board_items_page` filtrado pelos mesmos critérios para puxar os IDs.

## Boards e colunas

### Renovação (9427535861) — item de partida
- `date_mks7vvn8` — Vencimento (filtro T-15)
- `status` — estágio do funil
- `person` — corretor responsável
- `text_mks72r4c` — Apólice a Renovar (nº)
- `text_mks7z632` — Seguradora
- `dropdown_mm09hks6` — Produto
- `numeric_mks5gh0b` — Prêmio Atual
- `numeric_mkvv8v53` — Prêmio Líquido
- `numeric_mkv9sywr` — Comissão
- `phone_mm2c694m` — Telefone
- `board_relation_mm093n4q` → Apólices (resolve cliente)

### Apólices (9749857183)
- `data` — Início vigência
- `date_mkth8nwr` — Término vigência
- `color_mm16taeb` — Status (ATIVA, RENOVADA, VENCIDA, CANCELADA)
- `text_mkthd2f8` — Produto/Ramo
- `numeric_mkth6nhc` — Prêmio Líquido
- `numeric_mkth19pb` — Prêmio Total
- `board_relation_mkthmv5r` → Clientes
- `board_relation_mkw2x691` → Sinistros
- `board_relation_mm093dre` → Renovação

### Clientes (9332203920)
- `color_mm2048xk` — Status (Ativo/Inativo)
- `date_mm1qbtn8` — Cliente Desde
- `lookup_mm02hvyb` — LTV (mirror)
- `lookup_mkv2997t` — Produtos (mirror)
- `date_mm1q5g8w` — Último Contato
- `numeric_mm1q92a` — Indicações
- `dropdown_mm1hyc07` — Persona
- `board_relation_mkthvdt` → Apólices

### Sinistros (18026494883)
- `data` — Data ocorrência
- `date_mm26wfdr` — Data aviso
- `status` — Aberto, Pendente, Liquidado, Recusado, Em Análise
- `numeric_mkw2z2s7` — Valor indenização
- `board_relation_mkw2jfap` → Apólices

## Lógica de montagem (por item da Renovação)

1. **Resolver cliente** via `board_relation_mm093n4q` (Renovação → Apólice atual) → `board_relation_mkthmv5r` (Apólice → Cliente). Se a relação estiver vazia, gerar update curto: `[DOSSIÊ INDISPONÍVEL] Item sem vínculo com Apólice/Cliente — saneamento pendente.` e encerrar.

2. **Cabeçalho** do board Clientes: nome, persona, Cliente Desde (calcular anos), LTV, Produtos ativos, Último Contato, Indicações, status, telefone (do item Renovação), corretor (resolver via `team.md`).

3. **Apólice em renovação** (item Renovação): produto, seguradora, nº apólice, prêmio atual, líquido, comissão, vencimento.

4. **Apólices ativas** — `get_board_items_page` em Apólices filtrado por `board_relation_mkthmv5r = <cliente_id>` AND `color_mm16taeb = ATIVA`. Para cada: produto, seguradora, prêmio líquido, vigência fim.

5. **Histórico completo** — todas as apólices não-ATIVAS do cliente (status RENOVADA, VENCIDA, CANCELADA, NÃO RENOVADA). Sem corte temporal. Ordenar por `date_mkth8nwr` desc.

6. **Sinistros** — para cada apólice do cliente (ativa + histórica), checar `board_relation_mkw2x691`. Consolidar e agrupar por status. Listar até 10 mais recentes; se >10, mostrar agregado.

7. **Sinais computados:**
   - **Cross-sell gap** — comparar `lookup_mkv2997t` (produtos atuais) contra catálogo Menegon (Auto, Residencial, Vida Individual, Vida em Grupo, Empresarial, Condomínio, Consórcio, Previdência, RC Profissional, Transporte, Acidentes Pessoais, Saúde, Seguro Garantia, Fiança Locatícia). Listar gaps relevantes (não recomendar Empresarial para PF, etc — usar persona).
   - **Histórico de não-renovação** — se ≥1 apólice com status NÃO RENOVADA nos últimos 12 meses → flag `[!]`.
   - **Sinistralidade alta** — se Σ(valor sinistros liquidados) / Σ(prêmio acumulado) > 0.5 → flag `[!]`.
   - **Inatividade** — se dias desde Último Contato > 60 → flag `[!]` com nº de dias.

8. **Sugestão de abordagem** — 1 parágrafo direcional, NÃO um script. Cruzar produto em renovação + sinais + persona. Ex: "Cliente Premium, 6 anos de casa, zero sinistros: enfatizar continuidade e aproveitar para apresentar Vida em Grupo (gap evidente)."

## Output (formato do update colado no item)

```
DOSSIÊ 360 — RENOVAÇÃO T-15 (gerado <YYYY-MM-DD> 06:00)

CLIENTE: <nome> | <persona> | Cliente desde <data> (<X anos Y meses>)
LTV: R$ <valor> | Produtos ativos: <lista> | Último contato: <data> (<X dias>)
Telefone: <fone> | Corretor: <nome>

═ APÓLICE EM RENOVAÇÃO ═
<produto> @ <seguradora> | Apólice <nº> | Vence <data> (T-15)
Prêmio atual: R$ <X> | Líquido: R$ <Y> | Comissão: R$ <Z>

═ APÓLICES ATIVAS (<n>) ═
- <produto> @ <seguradora> | R$ <prêmio> | vigência até <data>
…

═ HISTÓRICO COMPLETO (<n>) ═
- <data fim> | <produto> @ <seguradora> | R$ <prêmio> | <status>
…

═ SINISTROS (<n>) ═
[Liquidados: <n>] [Em análise: <n>] [Recusados: <n>] [Aberto: <n>]
- <data> | R$ <valor> | <apólice> | <status>
…

═ SINAIS ═
[!] Histórico de não-renovação (<n> nos últimos 12m)
[!] Inativo há <X> dias
[!] Sinistralidade alta (<ratio>)
[+] Gap cross-sell: <ramos faltantes>

═ SUGESTÃO DE ABORDAGEM ═
<1 parágrafo direcional>

— gerado por skill dossie-renovacao v1.0
```

## Regras de truncamento

Updates do Monday têm limite prático ~10 000 caracteres. Se o dossiê ultrapassar:
- Histórico: mostrar 20 mais recentes + linha `… (+N apólices anteriores)`.
- Sinistros: mostrar 10 mais recentes + linha `… (+N sinistros anteriores)`.

## Modo `executar` — escrita

Para cada item processado:
1. Montar dossiê (lógica acima).
2. `create_update(item_id=<renovacao_item_id>, body=<dossiê>)`.
3. Registrar resultado JSON conforme schema de retorno do `monday-crm-write`.
4. Em caso de erro de escrita: registrar `[ERRO-DOSSIÊ] <mensagem>` no próprio item se possível; reportar e seguir para o próximo item (não abortar batch).

## Idempotência

Antes de colar update, verificar se já existe update com prefixo `DOSSIÊ 360 — RENOVAÇÃO T-15` gerado nas últimas 24h no mesmo item (via `get_updates`). Se sim, pular para evitar duplicidade quando a rotina rodar mais de uma vez no dia.

## Saída em modo `relatorio` (consolidado)

```
DOSSIÊS T-15 — <data>
Itens processados: <n>
- <cliente A> (item <id>) — OK
- <cliente B> (item <id>) — SEM VÍNCULO (saneamento pendente)
- <cliente C> (item <id>) — OK
```

## Limites e dependências

- Reusa `monday-crm-query` para leitura e `monday-crm-write` para escrita.
- Depende de `team.md` para nome de corretor (não hardcodar IDs).
- Não substitui o agente `especialista-renovacao` — esta skill é apenas geradora de contexto, não toma decisão de cotação.
- Roda diariamente — se nenhum item vencer em T-15, sair silenciosamente com `Nenhum dossiê hoje.`
