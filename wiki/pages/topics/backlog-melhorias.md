---
title: Backlog de Melhorias
type: topic
created: 2026-04-14
updated: 2026-04-14
sources: []
tags: [backlog, melhorias, plugins, agentes, skills, tarefas, crm, dados]
---

## Summary

Rastreamento centralizado de ideias de melhoria para todos os ativos do sistema: plugins, agentes, skills e tarefas agendadas. As melhorias são priorizadas em Alta / Média / Baixa e rastreadas com status Pendente / Em andamento / Concluído. As entradas de plugins com prioridade Alta envolvem habilitar paralelismo no monitor-crm e auditoria adversarial nas skills que escrevem no CRM. Os 6 agentes do grupo comercial já têm melhorias definidas, incluindo item crítico de skill ausente no hunter-cross-sell. Os 4 agentes do grupo marketing/conteúdo (cmo, analista-campanhas, criador-conteudo, especialista-inbound) também estão preenchidos. Os 7 agentes do grupo análise e monitoramento (analista-churn, executor-retencao, analista-forecast, monitor-crm, analista-nps, analista-pipeline, analista-performance) completam o levantamento — todos os 17 agentes do sistema têm pelo menos uma melhoria concreta documentada. As 5 skills do grupo CRM e dados (monday-crm-query, monday-crm-write, forecast-ponderado, analise-churn, analise-nps) têm melhorias documentadas, com foco em: formato de saída não definido, dependências não documentadas e lacunas de dados de entrada.

## Key points

- 6 melhorias identificadas para plugins `superpowers` e `codex`, todas com status Pendente
- 17 de 17 agentes com melhorias definidas: 6 grupo comercial + 4 grupo marketing/conteúdo + 7 grupo análise e monitoramento
- 5 de 14 skills com melhorias definidas: grupo CRM e dados (monday-crm-query, monday-crm-write, forecast-ponderado, analise-churn, analise-nps); as outras 9 skills permanecem com `—`
- Nenhuma tarefa agendada ativa no momento do levantamento (2026-04-14)

## Connections

- [Monitor CRM — Índice](../analyses/crm-monitor/index.md) — agente `monitor-crm` é alvo da melhoria de paralelismo (superpowers)
- Workspace n8n em menegon.app.n8n.cloud referenciado na melhoria de skills `n8n-*`

## Open questions

- Quais agentes têm maior prioridade para levantamento de melhorias específicas?
- A skill `forecast-ponderado` tem cobertura de testes antes de receber `codex:review`?
- O limite de 3 cloud triggers afeta a viabilidade de ativar tarefas agendadas no futuro?

## Changelog

- 2026-04-14 — página criada com 6 melhorias de plugins e tabelas-esqueleto para agentes, skills e tarefas
- 2026-04-14 — populadas 6 linhas de agentes do grupo comercial (diretor-comercial, gerente-comercial, especialista-renovacao, especialista-seguro-novo, hunter-cross-sell, qualificador-leads)
- 2026-04-14 — populadas 4 linhas de agentes do grupo marketing/conteúdo (cmo, analista-campanhas, criador-conteudo, especialista-inbound)
- 2026-04-14 — populadas 7 linhas de agentes do grupo análise e monitoramento (analista-churn, executor-retencao, analista-forecast, monitor-crm, analista-nps, analista-pipeline, analista-performance); todos os 17 agentes têm melhorias documentadas
- 2026-04-14 — populadas 5 linhas de skills do grupo CRM e dados (monday-crm-query, monday-crm-write, forecast-ponderado, analise-churn, analise-nps); Key points atualizado para 5 de 14 skills com melhorias definidas

---

## Plugins — 2 instalados

| Nome | Versão | Melhoria | Prioridade | Status |
|------|--------|----------|------------|--------|
| superpowers | 5.0.7 | Habilitar `dispatching-parallel-agents` no agente `monitor-crm` para rodar forecast + pipeline + NPS em paralelo — reduz tempo de diagnóstico matinal de ~3 execuções sequenciais para 1 | Alta | Pendente |
| superpowers | 5.0.7 | Ativar skills `n8n-*` nos agentes que constroem ou debugam automações (especialista-renovacao, executor-retencao) — o workspace n8n em menegon.app.n8n.cloud já existe mas nenhum agente usa essas skills explicitamente | Alta | Pendente |
| superpowers | 5.0.7 | Integrar skill `notebooklm` ao agente `analista-nps` para consultar corpus de feedback de clientes acumulado (NPS board + apolices) sem precisar repassar dados brutos no prompt | Média | Pendente |
| superpowers | 5.0.7 | Usar skill `insights` no fluxo semanal do `diretor-comercial` para gerar relatório de uso de agentes — identifica quais agentes param de ser invocados e quais consomem mais tempo | Média | Pendente |
| codex | 1.0.3 | Rodar `codex:adversarial-review` nas skills `monday-crm-write` e `plano-retencao` — essas skills escrevem no CRM (fonte de verdade); um erro silencioso pode corromper dados de renovação para 95% da carteira | Alta | Pendente |
| codex | 1.0.3 | Rodar `codex:review` na skill `forecast-ponderado` — lógica de três cenários é complexa e ainda não foi auditada; erros afetam diretamente as decisões do Diretor Comercial | Média | Pendente |

---

## Agentes (17)

| Nome | Melhoria | Prioridade | Status |
|------|----------|------------|--------|
| analista-campanhas | Não tem threshold numérico que define quando uma campanha "precisa de intervenção" vs. está "dentro do esperado" — adicionar exit criteria explícito ao system prompt (ex.: conversão < 60% da meta por 3+ dias consecutivos = alertar CMO; ROI < 1,0 = pausar campanha); também falta skill `segmentacao-carteira` para cruzar performance de campanha com o segmento-alvo e identificar se o problema é de segmentação, não de canal | Alta | Pendente |
| analista-churn | Não rastreia a tendência do health score ao longo do tempo — um cliente que caiu de 75 para 42 em duas semanas é mais urgente que um que está estável em 38, mas ambos recebem o mesmo tratamento "Crítico"; adicionar ao system prompt a instrução de comparar o score atual com o score da semana anterior (armazenado no Monday como campo de nota ou update) e classificar como "deterioração rápida" quando a queda for ≥15 pts em 7 dias, elevando a prioridade acima dos críticos estáveis; também falta exit criteria explícito para o relatório semanal — definir quando a varredura está "completa" (ex.: todos os clientes com status Ativo processados, resumo executivo enviado ao Diretor) | Alta | Pendente |
| analista-forecast | O erro aceitável do forecast nunca foi definido — os multiplicadores de cenário (0,7× pessimista, 1,15× otimista) não têm calibração histórica documentada, então não há como saber se o modelo é preciso ou se os cenários são arbitrários; adicionar ao system prompt a instrução de calcular o erro médio absoluto percentual (MAPE) das últimas 4 semanas comparando forecast provável vs. receita real registrada no board Apólices (9749857183), e alertar o Diretor quando MAPE > 20% (indica que os pesos precisam de revisão); também não há tratamento explícito para deals criados no meio da semana — definir se eles entram no forecast corrente ou apenas no próximo ciclo | Alta | Pendente |
| analista-nps | Agente é puramente reativo (ativa apenas quando novo lote chega) mas não tem cadência mínima garantida — se nenhum NPS entrar por 30 dias, nenhuma análise de tendência é produzida; adicionar gatilho mensal explícito (Dia 1 de cada mês) para produzir relatório de evolução mesmo sem novos dados, usando histórico do board 9751082146; também falta skill `nutricao-lead` para o fluxo de promotores — hoje o agente apenas "lista promotores prontos para pedir indicação" mas não executa o contato de solicitação de referral, que poderia ser delegado com um script de nutrição personalizado | Média | Pendente |
| analista-performance | KPIs estão listados mas nenhum tem faixa aceitável definida — "taxa de conversão por estágio" sem benchmarks significa que o diagnóstico depende do feeling do agente, não de critérios objetivos; adicionar tabela de referência no system prompt com metas mínimas por KPI (ex.: conversão Follow-up→Fechamento ≥ 40%, ciclo médio ≤ 21 dias, taxa de churn ≤ 15%/mês) para que o diagnóstico seja comparativo e reproduzível; também não há rastreamento de recomendações anteriores — o agente produz "plano de ação para o próximo mês" toda semana mas nunca verifica se as recomendações da semana anterior foram implementadas; adicionar passo de verificação de recomendações pendentes antes de produzir novas | Alta | Pendente |
| analista-pipeline | Health Score do pipeline tem metas definidas mas não há escalada automática quando os thresholds são violados — o agente apenas "sugere ao Gerente Comercial" sem prazo ou protocolo claro; definir no system prompt que quando Cobertura de Meta < 2× ou Deals sem movimentação > 35%, o agente deve produzir um alerta estruturado com prazo de resposta do Gerente (48h) e escalar ao Diretor se não houver resolução; também a lógica de detecção de deals duplicados está mencionada na auditoria mas sem critério de similaridade definido — especificar que duplicata = mesmo cliente + mesmo produto + mesmo corretor com datas de vencimento a ≤30 dias de distância | Média | Pendente |
| cmo | Não tem skill `segmentacao-carteira` apesar de ser responsável por definir segmentação de campanhas — adicionar skill ao frontmatter e incluir passo explícito de consulta à carteira segmentada antes de planejar campanhas trimestrais; também faltam exit criteria para entrega de planejamento (ex.: o plano está aprovado quando contém: objetivo quantificado, canal priorizado, CPL-meta por canal e responsável definido) | Média | Pendente |
| criador-conteudo | Tom e voz estão descritos qualitativamente mas sem exemplos concretos aprovados e reprovados — adicionar ao system prompt pelo menos 1 exemplo de mensagem "certa" e 1 "errada" por tipo de conteúdo principal (script WhatsApp, email nurturing, post Instagram) para tornar as diretrizes reproduzíveis; também não há consulta de CRM para identificar qual produto/segmento o cliente-alvo possui antes de criar conteúdo personalizado — adicionar passo de `monday-crm-query` quando o contexto for um lead ou cliente específico | Média | Pendente |
| diretor-comercial | Adicionar few-shot examples de aprovação e rejeição no system prompt (ex: quando forecast < 80% com ≤7 dias para fechamento, output deve incluir justificativa estruturada de reprovação); hoje o agente não tem exemplos de saída | Alta | Pendente |
| especialista-inbound | O handoff para o qualificador-leads está implícito no gatilho "Qualificador devolve lead morno" mas o fluxo de 14 dias não tem passo explícito de registro no Monday antes de passar o lead adiante — adicionar passo 4b: gravar campos `status_nurturing` e `data_handoff` no item do Monday (via `monday-crm-write`) antes de enviar para o qualificador, evitando leads duplicados em nutrição e qualificação simultaneamente; também não usa skill `segmentacao-carteira` apesar de ter estratégia diferenciada por persona | Alta | Pendente |
| especialista-renovacao | Não tem critério numérico para priorização de cotação quando múltiplos vencimentos colidem no mesmo dia — definir score de urgência combinando dias para vencimento + prêmio líquido (`numeric_mkvv8v53`) para ordenar o lote diário; também está faltando skill `nutricao-lead` para clientes que ficam em "Follow-up" além de 7 dias sem resposta | Média | Pendente |
| especialista-seguro-novo | Handoff de pós-fechamento é implícito ("encaminhar para Analista de Churn") mas sem registro estruturado de conclusão no CRM — adicionar passo 6a: gravar campo `status_handoff` no item do Monday antes de encaminhar, garantindo que o Analista de Churn não processe um deal ainda em análise; também falta skill `nutricao-lead` para leads classificados como "frios" antes de arquivá-los | Média | Pendente |
| executor-retencao | Tem autonomia para construir planos mas zero autonomia para executar — tudo depende de aprovação do Marco sem SLA definido; se Marco não revisar em 48h, um cliente Crítico perde o janela de ação sem nenhuma escalada automática; adicionar ao system prompt regra de escalada: "Se aprovação não ocorrer em 24h para clientes Críticos (score < 40) ou em 72h para Em Risco, registrar lembrete automático no Monday (via `monday-crm-write`) no item do cliente com tag `[Aguardando Aprovação]` e notificar Marco novamente"; também falta skill `nutricao-lead` para o fluxo de clientes que estão Em Risco (score 40-60) com Follow-up além de 7 dias — hoje recebem apenas script de WhatsApp, mas poderiam receber sequência de nutrição estruturada antes de escalar | Alta | Pendente |
| gerente-comercial | Distribuição de prioridades é manual e sem critério de scoring documentado — definir fórmula de prioridade (ex.: `score = (30 - dias_vencimento) × prêmio_líquido`) e adicionar ao system prompt com exemplo de output de distribuição semanal para os especialistas (few-shot); também não tem exit criteria explícito para o resumo ao Diretor (quando o consolidado está "bom o suficiente" vs. precisa de aprovação) | Alta | Pendente |
| hunter-cross-sell | Skill `cross-sell-hunt` não está documentada no repositório de skills — verificar se a skill existe ou se precisa ser criada; critério de "probabilidade de fechar" no cálculo de valor esperado é totalmente subjetivo e pode gerar lists inconsistentes entre execuções, definir rubrica de scoring por perfil (ex.: cliente ativo há >1 ano = +2 pts, produto complementar natural = +3 pts) | Alta | Pendente |
| monitor-crm | Usa apenas `monday-crm-query` (somente leitura) mas não pode criar tasks ou updates no Monday quando detecta alertas — os acionamentos ficam apenas como texto no relatório markdown, sem garantia de que o agente responsável os veja; adicionar skill `monday-crm-write` para que alertas Críticos criem automaticamente um update no item do cliente/deal afetado com prefixo `[Monitor-CRM CRÍTICO]`, garantindo visibilidade no board sem depender de leitura do arquivo wiki; também a lógica de health score da Dimensão 2 (Churn) está duplicada no system prompt do monitor-crm e do analista-churn — se os pesos mudarem em um agente, o outro fica desatualizado; centralizar a fórmula na skill `analise-churn` e referenciar dela nos dois agentes | Alta | Pendente |
| qualificador-leads | Critérios BANT têm pesos definidos verbalmente (Alto/Médio/Baixo) mas sem escala numérica — especificar pontuação concreta por critério (ex.: Produto Alto = 3 pts, Perfil Alto = 3 pts, Timing Médio = 2 pts, Origem Médio = 2 pts, Contato Baixo = 1 pt; máx = 11) para tornar o score 8–10/5–7/0–4 reproduzível entre execuções; adicionar campo Monday target para registrar o score calculado por lead | Alta | Pendente |

---

## Skills (14)

| Nome | Melhoria | Prioridade | Status |
|------|----------|------------|--------|
| abordagem-comercial | — | — | Pendente |
| analise-campanhas | — | — | Pendente |
| analise-churn | A dimensão "Engajamento" (15% do score) não tem fonte de dados documentada — o Monday não tem campo nativo de "última interação"; especificar que a data de engajamento deve ser lida do último update registrado no item (via API `last_updated_at`) e documentar esse mapeamento na SKILL.md; também a verificação de monoproduto exige cross-reference com o board Apólices (9749857183) mas nenhuma instrução de join está documentada — adicionar passo explícito de busca no board Apólices filtrando por cliente antes de calcular a dimensão; por fim, não há saída definida para o caso em que a carteira tem zero clientes Críticos — adicionar esse caso ao template de saída esperada | Alta | Pendente |
| analise-nps | Não há tamanho mínimo de amostra definido — com 1 resposta, a skill tecnicamente produz um NPS de −100 ou +100 que é matematicamente correto mas estatisticamente inútil; adicionar regra explícita: "se total de respostas no período < 5, emitir aviso de amostra insuficiente e não apresentar score por produto ou corretor (segmentação requer ≥ 5 por categoria)"; também o campo de feedback textual dos detratores não tem seu column ID documentado no SKILL.md — identificar e registrar o ID da coluna de texto livre do board 9751082146 para que a análise de categorias (Preço/Atendimento/Sinistro/Produto) seja reproduzível; e o fluxo de escalada para Marco (detratores com prêmio > R$ 3.000/ano) não documenta como calcular o prêmio anual — especificar que é o campo `numeric_mks5gh0b` (Prêmio Atual) do board Clientes cruzado por CPF/nome | Alta | Pendente |
| auditoria-pipeline | — | — | Pendente |
| criacao-conteudo | — | — | Pendente |
| cross-sell-hunt | — | — | Pendente |
| forecast-ponderado | Os multiplicadores de cenário (0,70× pessimista / 1,15× otimista) não têm calibração histórica documentada e a fonte do valor "Meta do mês" não está especificada — definir de onde buscar a meta (hardcoded no SKILL.md? campo em um board Monday? doc_id no Monday Docs?) e adicionar instrução de calcular o erro médio absoluto percentual (MAPE) das últimas 4 semanas comparando o cenário Provável com a receita real (board Apólices 9749857183, coluna de prêmio pago) para calibrar os multiplicadores; também não há regra para deals criados no meio do período — definir se entram no forecast corrente (pró-rata pelo tempo restante) ou apenas no próximo ciclo, e documentar a regra no SKILL.md | Alta | Pendente |
| monday-crm-query | Não há formato de saída definido — a skill descreve quais boards e colunas existem mas não especifica o schema do objeto retornado ao agente que a chama (lista de dicts? markdown table? JSON?); padronizar o formato de retorno com pelo menos dois modos: `list` (array de objetos com campos selecionados) e `summary` (contagem + top N) e documentar no SKILL.md; também a instrução de paginação ("usar paginação para boards grandes") não fornece o cursor correto da API Monday — adicionar exemplo de query GraphQL com `limit` e `cursor` para o board Apólices (8.459 itens) para evitar que agentes façam requisições sem paginação e recebam dados truncados silenciosamente | Média | Pendente |
| monday-crm-write | Não há formato de retorno definido para nenhuma das 5 operações — o agente que chama a skill não sabe se a escrita foi bem-sucedida ou falhou; padronizar retorno mínimo `{ "status": "ok"|"error", "item_id": X, "message": "..." }` para todas as operações e documentar no SKILL.md; também a regra "confirmar o valor atual antes de alterar" (atualização de coluna) é boa prática mas não tem instrução de rollback — se a escrita falhar a meio (ex.: update criado mas coluna não atualizada), o item fica em estado inconsistente; adicionar instrução explícita: em caso de erro parcial, registrar o estado inconsistente como update no próprio item com prefixo `[ERRO-WRITE]` para auditoria manual; e a lista de ações críticas que exigem confirmação humana não inclui movimentação de grupo (ex.: mover deal de "Follow-up" para "Não Renovado"), que é irreversível — adicionar à lista de ações bloqueadas sem aprovação | Alta | Pendente |
| nutricao-lead | — | — | Pendente |
| plano-retencao | — | — | Pendente |
| qualificacao-lead | — | — | Pendente |
| segmentacao-carteira | — | — | Pendente |

---

## Tarefas Agendadas (0)

| Nome | Melhoria | Prioridade | Status |
|------|----------|------------|--------|
| *nenhuma ativa no momento* | — | — | — |

---

*Última atualização: 2026-04-14*
