# Runbook — Migrar tarefas agendadas de Local (Desktop) para Remota (Cloud)

## Objetivo

Recriar 1:1 cada tarefa agendada que hoje roda como **Local / Desktop** (máquina do usuário) como uma tarefa **Remota / Cloud** (infra Anthropic), verificar que a versão remota executa com sucesso e só então desligar a local.

Referência: https://code.claude.com/docs/en/desktop-scheduled-tasks

## Quando usar este runbook

- Usuário pediu para "mover", "migrar" ou "recriar como remota" as tarefas agendadas
- Máquina do usuário fica desligada parte do dia e tarefas locais estão perdendo execuções
- Quer reduzir dependência do Desktop para automações recorrentes

## Pré-requisitos

1. **Executar este runbook dentro de uma sessão Desktop** na máquina do usuário — só ela enxerga `~/.claude/scheduled-tasks/` e o estado interno (schedule, folder, model, enabled) que não vive nos `SKILL.md`.
2. GitHub conectado ao Claude Code web (`/web-setup` se ainda não feito).
3. Repositório GitHub alvo identificado para cada folder local — a task remota clona um repo fresh a cada execução; sem repo não há como rodar.
4. Connectors MCP necessários já habilitados em Settings → Connectors no claude.ai. `.mcp.json` local **não é herdado** pela task remota.
5. Acesso a `claude.ai/code/scheduled` para inspecionar sessões remotas criadas.

## Comparação rápida Local vs Remota

| Aspecto | Local / Desktop | Remota / Cloud |
|---|---|---|
| Roda em | máquina do usuário | infra Anthropic |
| PC precisa estar ligado | sim | não |
| Mínimo de intervalo | 1 minuto | 1 hora |
| Acesso a arquivos locais fora do repo | sim | **não** — só o clone do repo |
| MCP servers via `.mcp.json` local | sim | **não** — usa Connectors Anthropic |
| Permission prompts | pode pausar e pedir | roda autônomo, não pede |

## Inputs

Lista das tasks locais a migrar. Para obter:

```
Na sessão Desktop, peça ao Claude:
  "mostre minhas tarefas agendadas locais com nome, prompt completo,
   schedule, folder, model e permission mode"
```

Para cada task, registre em uma tabela temporária (pode ser em `.tmp/migrate-scheduled-tasks.md`):

| # | Nome | Schedule atual | Folder local | Model | Permission mode | Usa `.mcp.json`? | Lê arquivos fora de um repo Git? |
|---|------|----------------|--------------|-------|-----------------|-------------------|----------------------------------|

A última coluna decide se a task é **migrável**. Se "sim", ela não pode virar remota sem reescrita de escopo — marque como **não migrável** e pergunte ao usuário o que fazer (manter local, reescrever para ler do repo, ou descartar).

## Passos (repetir por task migrável)

### 1. Capturar o estado atual

Na Desktop:

```
mostre a task agendada <nome> com prompt, schedule, folder, model,
permission mode e enabled state
```

Copie o prompt literal.

### 2. Mapear folder → repositório GitHub

- Se o `folder` local já é um clone de um repo GitHub, use esse repo.
- Se não, pergunte ao usuário qual repo deve ser usado. Não invente.
- Se a task não precisa de repo algum (ex.: só chama APIs externas), use um repo placeholder pequeno e documente isso no prompt.

### 3. Ajustar schedule para o mínimo Cloud

- Local tinha < 1h → arredonde para **hourly** e registre na tabela a mudança de cadência. Confirme com o usuário antes se for uma task crítica.
- Local era "manual" → crie a remota como manual (sem cron) também.
- Local era diário/semanal → mantenha igual.

### 4. Revisar o prompt

Cloud roda **autônomo**, num **clone fresh do repo**, sem arquivos fora dele, sem MCP local. O prompt precisa:

- Não referenciar paths absolutos da máquina (`C:\Users\...`, `/home/...`)
- Não depender de arquivos em `.tmp/`, `~/Desktop`, etc.
- Substituir menções a MCP locais por connectors Anthropic equivalentes (ex.: `.mcp.json` → n8n connector em Settings → Connectors)
- Ser explícito sobre o que fazer — não há humano para responder clarificações
- Se a task envolve escrever no repo, terminar com instrução de commit + push

### 5. Criar a task remota

Ainda na Desktop (ou em qualquer sessão conectada):

```
/schedule
```

Preencha:
- **Nome**: `<nome>-remote` (sufixo facilita distinguir das locais durante a migração)
- **Repository**: o repo do passo 2
- **Environment**: `Default` exceto se precisar de env vars específicas (liste quais)
- **Connectors**: só os MCPs que a task realmente usa
- **Schedule**: do passo 3
- **Prompt**: do passo 4
- **Model**: o mesmo da local

### 6. Verificar primeira execução

Clique **Run now** no form da task remota. Abra a sessão criada em `claude.ai/code/scheduled` e confirme:

- Sessão terminou sem erro
- Saídas esperadas aconteceram (commit, mensagem, linha no sheet, etc.)
- Nenhuma permissão negada em silêncio

Se falhou: ajuste prompt/connectors/env e rode `Run now` de novo. **Não prossiga para o passo 7 enquanto a remota não rodar limpa.**

### 7. Pausar a task local (não deletar)

```
desative o toggle "repeats" da task agendada local <nome>
```

Mantenha o SKILL.md local — é o seu rollback se algo der errado dias depois.

### 8. Próxima task

Volte ao passo 1.

## Cleanup final

**Só execute depois que todas as tasks remotas tiverem rodado pelo menos uma vez no schedule real** (não só o `Run now` manual). Espere um ciclo completo.

```
delete minha task agendada local <nome>
```

para cada uma. Opcional: renomeie as remotas removendo o sufixo `-remote`.

## Rollback

Se uma task remota estiver causando problemas depois do cleanup:

1. Reative a versão local com `ative o toggle repeats da task <nome>` (se ainda existir) **ou** recrie a partir do histórico de commits do `SKILL.md` local
2. Delete a remota com `delete my <nome>-remote cloud task`
3. Abra issue descrevendo o que quebrou — normalmente é `.mcp.json` ausente ou path absoluto no prompt

## Caveats — leia antes de começar

- **Mínimo Cloud = 1 hora.** Tasks que rodavam a cada 5 ou 15 minutos **não** sobrevivem 1:1. Confirme com o usuário antes de migrar essas.
- **Sem arquivos locais.** Qualquer task que lê `~/Desktop/...`, `.tmp/`, `credentials.json` fora do repo, ou qualquer coisa fora do clone GitHub, **não é migrável** sem reescrita.
- **`.mcp.json` local não é herdado.** Neste workspace o único MCP local é `n8n` (ver [../../.mcp.json](../../.mcp.json)). Se alguma task usa, precisa existir connector n8n equivalente em Settings → Connectors no claude.ai, senão a task remota quebra.
- **Autonomia.** Cloud não pede permissão — o prompt precisa assumir que tudo é auto-aprovado. Para ações sensíveis (push, envio de email, etc.), deixe o gating explícito no prompt, não confie em confirmação interativa.
- **Credenciais.** Env vars / `.env` locais não são herdados. Tasks que precisam de chaves devem usar o Environment "Default" com as secrets configuradas no claude.ai ou connectors que já encapsulam auth.
- **Ordem importa.** Nunca delete a local antes da remota rodar limpa pelo menos um ciclo real — senão você perde o prompt e o histórico.

## Failure modes conhecidos

| Sintoma | Causa provável | Fix |
|---|---|---|
| Remota falha em "tool not found" | MCP local não virou connector | Adicionar connector em Settings ou remover uso do MCP do prompt |
| Remota falha em "file not found" | Prompt tem path absoluto local | Reescrever para path relativo ao repo |
| Remota trava / não termina | Prompt pede input interativo | Tornar prompt autônomo, remover perguntas |
| Remota roda mas não commita | Prompt não termina com `git push` | Adicionar passo de commit/push explícito |
| Schedule sumiu do form | Intervalo < 1h rejeitado | Arredondar para hourly |
