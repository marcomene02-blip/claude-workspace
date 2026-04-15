# Design: Backlog de Melhorias de Ativos

**Data:** 2026-04-14
**Escopo:** Sistema de rastreamento de melhorias para plugins, agentes, skills e tarefas agendadas do projeto menegon-seguros

---

## Objetivo

Criar uma página wiki única que funcione como backlog centralizado de ideias de melhoria para todos os ativos do sistema (33 itens: 2 plugins, 17 agentes, 14 skills, 0 tarefas agendadas ativas).

## Decisões de Design

- **Formato:** Página única com tabelas Markdown separadas por tipo de ativo
- **Localização:** `wiki/pages/topics/backlog-melhorias.md`
- **Estrutura por seção:** `| Nome | Melhoria | Prioridade | Status |`
- **Prioridade:** Alta / Média / Baixa
- **Status:** Pendente / Em andamento / Concluído
- **Populamento inicial:** Estrutura vazia — ideias adicionadas conforme surgem

## Ativos Rastreados

| Tipo | Quantidade |
|------|------------|
| Plugins | 2 |
| Agentes | 17 |
| Skills | 14 |
| Tarefas Agendadas | 0 (atualizar ao criar) |
| **Total** | **33** |

## Manutenção

- Adicionar nova linha ao identificar melhoria
- Atualizar status conforme progresso
- Ao criar nova tarefa agendada, adicionar linha na seção correspondente
- Atualizar contadores nos títulos das seções quando o inventário mudar
