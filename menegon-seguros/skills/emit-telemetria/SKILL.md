# emit-telemetria

## Descrição
Skill reutilizável de registro de telemetria estruturada. Qualquer rotina Menegon Seguros invoca esta skill **duas vezes**: no início e no final de sua execução. Ela instrui o agente invocante sobre como ler thresholds de configuração, gravar o arquivo de análise canonical e fazer upsert no Pinecone.

## Invocação
Esta skill é uma **instrução de procedimento** — não tem código executável próprio. O agente invocante deve seguir os passos abaixo como parte de sua própria execução.

---

## PASSO 1 — Início da execução (ler thresholds)

Ao **iniciar** a execução, o agente deve:

1. Verificar se existe o arquivo `menegon-seguros/config/thresholds/<rotina>.yaml` (onde `<rotina>` é o nome canônico da rotina, ex: `monitor-crm`).
2. Se o arquivo existir: ler todos os campos e mantê-los em memória como `thresholds_em_vigor`. Esses valores serão copiados no frontmatter do arquivo de análise ao final.
3. Se o arquivo **não** existir: usar os defaults declarados no próprio AGENTS.md da rotina. Registrar `thresholds_em_vigor: {}` no frontmatter.

**Nota**: O arquivo de thresholds pode ser modificado pelo `recalibrador-menegon` entre execuções. Ler no início garante que a rotina opera com os parâmetros mais recentes e que o log reflete exatamente o que foi usado.

---

## PASSO 2 — Final da execução (gravar arquivo de análise)

Ao **finalizar** a execução, o agente deve criar o arquivo:

```
wiki/pages/analyses/<rotina>/YYYY-MM-DD.md
```

onde `YYYY-MM-DD` é a data local do dia da execução (timezone America/Sao_Paulo, UTC-3).

O arquivo deve ter **exatamente** este frontmatter YAML seguido de seções markdown:

```yaml
---
rotina: <nome-da-rotina>               # ex: monitor-crm
trigger_id: <id-do-trigger>            # ex: trig_01LGPjy... (obter do contexto de execução; null se não disponível)
execucao: <ISO8601-com-timezone>       # ex: 2026-04-15T06:30:00-03:00
# === MÉTRICAS FAMÍLIA A — Precisão preditiva (preencher se a rotina faz previsões) ===
metricas_preditivas:
  # Cada rotina preditiva define seus próprios campos; null se não aplicável
  # Exemplos: forecast_r_previsto, score_lead_calculado, prob_churn_estimada
metricas_preditivas_t7: null           # preenchido retroativamente em T+7 dias pelo recalibrador
metricas_preditivas_t14: null          # preenchido retroativamente em T+14 dias
metricas_preditivas_t30: null          # preenchido retroativamente em T+30 dias
# === MÉTRICAS FAMÍLIA B — Conversão de ação (preencher se a rotina gera alertas/recomendações) ===
metricas_acao:
  itens_avaliados: null                # quantos itens foram analisados nesta execução
  alertas_gerados: null                # quantos alertas/recomendações foram criados
  updates_escritos_no_monday: null     # quantos updates foram escritos no CRM
metricas_acao_t7: null                 # preenchido retroativamente: quantos alertas geraram ação humana
metricas_acao_t14: null
metricas_acao_t30: null
# === MÉTRICAS FAMÍLIA D — Feedback humano ===
feedback_humano:
  tag_util: null                       # "util" | "ignorar" | null (preenchido pelo especialista-performance)
  observacao: null                     # comentário livre opcional
# === THRESHOLDS EM VIGOR ===
thresholds_usados: {}                  # cópia dos valores do config/thresholds/<rotina>.yaml em vigor
# === RECALIBRADOR ===
alteracoes_aplicadas_por_recalibrador: []  # lista de {campo, valor_anterior, valor_novo, data}
modo_autonomia: auto                   # "auto" | "shadow" — determina se recalibrador pode auto-apply
toca_cliente_externo: false            # true = recalibrador nunca auto-aplica nessa rotina
---

# Narrativa — <Nome da Rotina> — <Data>

## Resumo executivo
[O agente preenche aqui um parágrafo com o que aconteceu nesta execução]

## Detalhes
[Conteúdo principal do relatório da rotina]

## Ações disparadas
- [ ] agente-responsavel — descrição da ação

## Observações para o recalibrador
[Qualquer anomalia, contexto ou ressalva que o recalibrador deve considerar ao analisar esta execução]
```

### Preenchimento obrigatório pelo agente invocante

- `rotina`: nome canônico da rotina (ex: `monitor-crm`)
- `trigger_id`: ID do trigger de execução, obtido do contexto; `null` se não disponível
- `execucao`: timestamp ISO8601 com timezone `-03:00` (São Paulo)
- `metricas_preditivas`: preencher campos específicos da família A se a rotina faz previsões; `null` se não aplicável
- `metricas_acao.itens_avaliados`, `alertas_gerados`, `updates_escritos_no_monday`: preencher se família B
- `thresholds_usados`: copiar exatamente os valores lidos no Passo 1 (ou `{}` se não havia arquivo)
- `modo_autonomia`: `"auto"` por padrão; `"shadow"` se a rotina tem `toca_cliente_externo: true` ou foi configurada assim pelo recalibrador
- `toca_cliente_externo`: `true` se a rotina envia mensagens/emails/notificações para clientes externos da Menegon

### Atualizar o index.md da rotina

Após gravar o arquivo de análise diário, o agente deve:
1. Abrir `wiki/pages/analyses/<rotina>/index.md`
2. Atualizar o campo `## Última execução` com data e status resumido
3. Adicionar uma linha à seção `## Execuções` no topo da lista (ordem reversa cronológica), no formato:
   ```
   - [YYYY-MM-DD](YYYY-MM-DD.md) — <status resumido em ≤15 palavras>
   ```

---

## PASSO 3 — Final da execução (upsert no Pinecone)

Após gravar o arquivo markdown, o agente deve fazer upsert no Pinecone index **`menegon-telemetria`** usando a ferramenta MCP `mcp__plugin_pinecone_pinecone__upsert-records`.

### Estrutura do registro

```json
{
  "_id": "<rotina>-<YYYY-MM-DD>",
  "corpo_narrativa": "<texto completo após o frontmatter YAML, sem o bloco --- ...  --->"
}
```

Exemplo de `_id`: `monitor-crm-2026-04-15`

### Metadata a incluir nos campos do registro

Os seguintes campos devem ser incluídos como campos de nível superior no objeto de upsert (não dentro de um objeto `metadata` aninhado — o Pinecone MCP não aceita objetos aninhados):

| Campo | Fonte no frontmatter |
|-------|---------------------|
| `rotina` | `rotina` |
| `execucao` | `execucao` |
| `alertas_gerados` | `metricas_acao.alertas_gerados` (null se não aplicável) |
| `tag_util` | `feedback_humano.tag_util` — usar `""` (string vazia) quando null; Pinecone não aceita null |
| `toca_cliente_externo` | `toca_cliente_externo` |
| `modo_autonomia` | `modo_autonomia` |

### Estrutura completa do objeto de upsert

```json
{
  "_id": "monitor-crm-2026-04-15",
  "corpo_narrativa": "# Narrativa — Monitor CRM — 2026-04-15\n\n## Resumo executivo\n...",
  "rotina": "monitor-crm",
  "execucao": "2026-04-15T06:30:00-03:00",
  "alertas_gerados": 3,
  "tag_util": "",
  "toca_cliente_externo": false,
  "modo_autonomia": "auto"
}
```

### Tratamento de erros no upsert

Se a ferramenta `mcp__plugin_pinecone_pinecone__upsert-records` não estiver disponível ou retornar erro:
1. Registrar no campo `## Observações para o recalibrador` do arquivo markdown: `"PINECONE_UPSERT_FAILED: <motivo>"`
2. Continuar normalmente — o arquivo markdown é o registro canônico; o Pinecone é índice secundário

---

## Resumo do fluxo completo

```
[início da rotina]
  └─ emit-telemetria PASSO 1: ler config/thresholds/<rotina>.yaml
       └─ guardar thresholds_em_vigor em memória

[execução principal da rotina]
  └─ processar dados, gerar alertas, escrever no Monday, etc.

[final da rotina]
  └─ emit-telemetria PASSO 2: gravar wiki/pages/analyses/<rotina>/YYYY-MM-DD.md
       └─ atualizar wiki/pages/analyses/<rotina>/index.md
  └─ emit-telemetria PASSO 3: upsert no Pinecone "menegon-telemetria"
```

---

## Contratos com outros agentes

- **recalibrador-menegon**: lê os arquivos `YYYY-MM-DD.md` para analisar tendências e ajustar thresholds. Os campos `metricas_preditivas_t7/t14/t30` e `metricas_acao_t7/t14/t30` são preenchidos retroativamente pelo recalibrador.
- **especialista-performance**: preenche `feedback_humano.tag_util` e `feedback_humano.observacao` na revisão semanal (sexta 16h).
- **Pinecone index `menegon-telemetria`**: usado pelo recalibrador para recall semântico de execuções similares.

## Dependências

- Acesso de escrita a `wiki/pages/analyses/`
- Ferramenta MCP `mcp__plugin_pinecone_pinecone__upsert-records` (disponível em runtime)
- Index Pinecone `menegon-telemetria` deve existir (criado na T3 do plano de meta-aprendizado)
