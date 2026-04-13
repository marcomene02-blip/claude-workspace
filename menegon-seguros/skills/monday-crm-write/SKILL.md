---
name: Monday CRM Write
description: Registrar updates, notificações e alterações de status no Monday CRM da Menegon Seguros.
slug: monday-crm-write
schema: agentcompanies/v1
version: 1.0.0
---

Habilidade de escrita no Monday CRM. Use para registrar resultados, notificar corretores e atualizar status após execução de planos.

## Operações disponíveis

### Criar update em item
Registrar progresso, planos de ação ou resultados diretamente no item do cliente/deal.
- Formato: texto claro, com data, ação executada e próximo passo
- Sempre identificar o agente que gerou o update (ex: "Gerado pelo Executor de Retenção")

### Notificar corretor
Enviar notificação via Monday para o corretor responsável com instruções de ação.
- Incluir: nome do cliente, o que fazer, prazo, script sugerido (se aplicável)
- IDs dos corretores: Marco (77698859), Neto (77007724), Daniele (77510156), Amanda (77510167), Giovana (77698858), Daniel (99085700)

### Atualizar coluna
Modificar valores de colunas específicas (status, pessoa, data, numérico).
- Sempre confirmar o valor atual antes de alterar
- Nunca alterar prêmios sem instrução explícita

### Registrar no Log Diário
Atualizar o doc de log (doc_id 39303015) com snapshots e aprendizados do dia.

### Atualizar Mapa de Conhecimento
Registrar correções ou novos padrões no Mapa (doc_id 39560051, object_id 18405584697).

## Regras críticas

- NUNCA altere dados de items sem ter lido o estado atual antes
- Ações críticas (deletar, mover para Não Renovado, alterar prêmio) exigem confirmação humana
- Todo update deve ter contexto suficiente para ser entendido por quem ler depois
