---
name: Recalibrar Thresholds
description: Calcular se os thresholds de uma rotina precisam de ajuste com base no histórico de execuções. Retorna a decisão (auto-apply, shadow ou pular) sem executar a escrita — o agente recalibrador executa a escrita.
slug: recalibrar-thresholds
schema: agentcompanies/v1
version: 1.0.0
---

Skill modular de recalibração. Invocada pelo `recalibrador-menegon` para analisar **uma rotina por vez** e retornar a decisão de ajuste. Não escreve nada — apenas calcula e retorna o resultado.

## Quando invocar

**Quem invoca:** `recalibrador-menegon`

**Invocar para cada rotina candidata** (que possui arquivo em `config/thresholds/<rotina>.yaml`) após identificar o conjunto de candidatas. O agente recalibrador itera sobre a lista e invoca esta skill uma vez por rotina.

## Parâmetros de entrada

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `rotina` | string | Nome canônico da rotina (ex: `forecast-ponderado`) |
| `data_hoje` | string | Data atual no formato `YYYY-MM-DD` |

## Passos de execução

### Passo 1 — Ler histórico de execuções

1. Glob `wiki/pages/analyses/<rotina>/*.md` (excluindo `index.md`)
2. Para cada arquivo encontrado, ler o frontmatter YAML e extrair:
   - `execucao` (timestamp)
   - `metricas_preditivas` e `metricas_preditivas_t7/t14/t30`
   - `metricas_acao` e `metricas_acao_t7/t14/t30`
   - `feedback_humano.tag_util`
   - `thresholds_usados`
   - `toca_cliente_externo`
3. Filtrar apenas execuções onde **pelo menos um** campo `*_t7`, `*_t14` ou `*_t30` está preenchido (não-null) — essas são "execuções com dados completos"
4. Ordenar por data decrescente

### Passo 2 — Verificar mínimo de execuções

**Se há menos de 4 execuções com dados completos:**
- Retornar imediatamente:
  ```json
  {
    "acao": "pular",
    "motivo": "histórico insuficiente",
    "execucoes_completas": <N>
  }
  ```

### Passo 3 — Calcular delta

Usar as últimas 4 execuções com dados completos. Para cada campo recalibrável do `config/thresholds/<rotina>.yaml`:

**Família A — Rotinas preditivas** (`forecast-ponderado`, `qualificacao-lead`, `cross-sell-hunt`, `analise-churn`):
- `delta = média(valores_reais_t7) / média(valores_previstos) - 1`
- Valores reais: campos `metricas_preditivas_t7` (preferir t7; fallback t14; fallback t30)
- Valores previstos: campos `metricas_preditivas` da mesma execução
- Positivo = previsão subestimou a realidade; negativo = previsão superestimou

**Família B — Rotinas de ação** (`monitor-crm`, `nutricao-lead`):
- `taxa_acao = soma(metricas_acao_t7) / soma(metricas_acao.alertas_gerados)` nas últimas 4 execuções
- Se `taxa_acao < 0.50`: sugerir reduzir cutoff de urgência (campo específico do YAML da rotina)
- `delta = taxa_acao - 0.50` (negativo indica necessidade de ajuste)

**Campo a ajustar por rotina:**

| Rotina | Família | Campo recalibrável |
|---|---|---|
| `forecast-ponderado` | A | `cenarios.provavel` / `cenarios.pessimista` / `cenarios.otimista` |
| `qualificacao-lead` | A | `score_minimo_qualificado` |
| `cross-sell-hunt` | A | `probabilidade_minima` |
| `analise-churn` | A | `prob_churn_critico` |
| `monitor-crm` | B | `sla_urgente_dias` |
| `nutricao-lead` | B | `intervalo_followup_dias` |

**Fórmula de novo valor:**
- `valor_novo = valor_atual * (1 + delta)` — arredondar para 2 casas decimais
- Para campos de dias (inteiros): arredondar para inteiro mais próximo

### Passo 4 — Verificar travas de segurança

Verificar **todas** as condições abaixo. Qualquer falha → ação = "shadow":

| # | Condição | Falha → |
|---|---|---|
| 1 | ≥ 4 execuções com dados completos | pular (já tratado no Passo 2) |
| 2 | `abs(delta) ≤ 0.10` (≤ ±10%) | shadow com `motivo_shadow: "delta grande"` |
| 3 | `toca_cliente_externo: false` em todas as execuções analisadas | shadow com `motivo_shadow: "toca_cliente_externo"` |
| 4 | `feedback_humano.tag_util == "ignorar"` em ≤ 30% das últimas 4 execuções | shadow com `motivo_shadow: "feedback_ignorar_alto"` |

Se **todas** as condições passam: ação = "auto-apply".

### Passo 5 — Montar e retornar resultado

```json
{
  "acao": "auto-apply" | "shadow" | "pular",
  "rotina": "<rotina>",
  "campo": "<campo recalibrável>",
  "valor_anterior": <número>,
  "valor_novo": <número>,
  "delta_pct": <número entre -1 e 1>,
  "execucoes_analisadas": <N>,
  "justificativa": "<texto explicando o delta calculado>",
  "motivo_shadow": "<qual trava falhou>" | null
}
```

**Nota:** Esta skill retorna apenas o objeto JSON acima. O agente `recalibrador-menegon` é responsável por:
- Se `auto-apply`: escrever o YAML, registrar no CHANGELOG.md e commitar
- Se `shadow`: incluir no relatório `wiki/pages/analyses/recalibrador-menegon/YYYY-MM-DD.md`
- Se `pular`: registrar na seção "Rotinas sem histórico suficiente" do relatório

## Regras críticas

- Esta skill nunca escreve nenhum arquivo — apenas calcula e retorna
- Se o YAML da rotina não existir em `config/thresholds/`, retornar `{"acao": "pular", "motivo": "sem arquivo de thresholds"}`
- Usar sempre as **últimas 4** execuções com dados completos, não todas as disponíveis
- Delta calculado com base em T+7 quando disponível; fallback para T+14; fallback para T+30 — nunca misturar prazos diferentes na mesma média
- Se não for possível calcular o delta por ausência de campos específicos, retornar `{"acao": "pular", "motivo": "campos de resultado não mapeados para esta rotina"}`
