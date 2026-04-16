# Changelog de Thresholds — Menegon Seguros

Histórico de todas as alterações automáticas e manuais nos arquivos de threshold.
Editado pelo `recalibrador-menegon` (automático) ou pelo usuário (manual).

## Formato de entrada

```
### YYYY-MM-DD HH:MM — <rotina> — <campo>
- **Valor anterior:** <valor>
- **Valor novo:** <valor>
- **Justificativa:** <motivo da mudança>
- **Fonte:** recalibrador-menegon | manual
- **Reverter:** `<campo>: <valor_anterior>` em `config/thresholds/<rotina>.yaml`
```

## Entradas

<!-- O recalibrador-menegon adiciona entradas aqui automaticamente -->
<!-- Entradas mais recentes no topo -->

### 2026-04-15 — setup inicial
- Todos os arquivos criados com valores hardcoded extraídos das SKILL.md originais
- Fonte: manual (T2 do plano rotinas-autonomas)
- Nenhum histórico de calibração disponível — recalibrador aguarda ≥4 execuções com dados completos
