# Wiki Log

Append-only. Entry format: `## [YYYY-MM-DD] <op> | <title>`. Parseable with `grep "^## \[" wiki/log.md`.

## [2026-04-13] schema | wiki initialized
- Created `wiki/CLAUDE.md` schema with three-layer architecture (raw / pages / control).
- Created empty `wiki/index.md` catalog.
- Created `wiki/log.md` (this file).
- Created folder stubs: `raw/{articles,papers,notes,transcripts,images}`, `pages/{entities,concepts,topics,sources,analyses}`.
- Wiki ready for first ingest.

## [2026-04-14] ingest | Monitor CRM
- Criado `wiki/pages/analyses/crm-monitor/index.md` — índice de relatórios diários.
- Atualizado `wiki/index.md` com entrada em Analyses.

## [2026-04-14] refactor | backlog-melhorias criado sem frontmatter
- Adicionado YAML frontmatter ao `pages/topics/backlog-melhorias.md`
- Adicionadas seções obrigatórias (Summary, Key points, Connections, Open questions, Changelog)
- Adicionada entrada no índice `wiki/index.md`

## [2026-04-14] refactor | backlog-melhorias — agentes grupo comercial
- Populadas 6 linhas de agentes (diretor-comercial, gerente-comercial, especialista-renovacao, especialista-seguro-novo, hunter-cross-sell, qualificador-leads)

## [2026-04-14] refactor | backlog-melhorias — agentes grupo marketing/conteúdo
- Populadas 4 linhas de agentes (cmo, analista-campanhas, criador-conteudo, especialista-inbound)
- cmo: skill segmentacao-carteira ausente + exit criteria de planejamento faltando
- analista-campanhas: threshold numérico de intervenção ausente + skill segmentacao-carteira faltando
- criador-conteudo: exemplos concretos de tom/voz ausentes + consulta CRM antes de criar conteúdo personalizado
- especialista-inbound: passo de registro Monday no handoff ausente + skill segmentacao-carteira faltando
- Summary e Key points atualizados para refletir 10 agentes com melhorias definidas

## [2026-04-14] refactor | backlog-melhorias — agentes grupo análise e monitoramento
- Populadas 7 linhas de agentes (analista-churn, executor-retencao, analista-forecast, monitor-crm, analista-nps, analista-pipeline, analista-performance)
- analista-churn: rastreamento de tendência de health score (queda ≥15 pts em 7 dias) ausente + exit criteria do relatório indefinido
- executor-retencao: SLA de aprovação do Marco indefinido — clientes Críticos ficam sem escalada automática; skill nutricao-lead faltando para clientes Em Risco
- analista-forecast: MAPE nunca calculado, calibração dos multiplicadores sem base histórica; deals mid-week sem regra de inclusão definida
- monitor-crm: skill monday-crm-write ausente impede criar alertas no Monday; health score duplicado com analista-churn, frágil a mudanças de peso
- analista-nps: gatilho reativo sem cadência mínima garantida; skill nutricao-lead faltando para fluxo de referral de promotores
- analista-pipeline: escalada quando threshold violado sem prazo definido; critério de duplicata não especificado
- analista-performance: KPIs sem faixas de referência objetivas; recomendações anteriores nunca verificadas antes de novas
- Summary, Key points e Changelog da página atualizados; todos os 17 agentes têm melhorias documentadas

## [2026-04-14] refactor | backlog-melhorias — skills grupo CRM e dados
- Populadas 5 linhas de skills (monday-crm-query, monday-crm-write, forecast-ponderado, analise-churn, analise-nps)
- monday-crm-query: formato de saída indefinido + exemplo de paginação GraphQL ausente para board Apólices
- monday-crm-write: retorno de sucesso/erro não padronizado + rollback parcial não documentado + movimentação de grupo ausente da lista de ações críticas
- forecast-ponderado: fonte da meta mensal não especificada + calibração histórica dos multiplicadores ausente + regra para deals mid-period indefinida
- analise-churn: dimensão Engajamento sem fonte de dados mapeada (last_updated_at) + join com Apólices para monoproduto não documentado + caso zero-críticos ausente do template de saída
- analise-nps: tamanho mínimo de amostra não definido (risco de NPS espúrio) + column ID de feedback textual não documentado + cálculo de prêmio anual para escalada a Marco não especificado
- Key points atualizado: 5 de 14 skills com melhorias definidas

## [2026-04-14] refactor | backlog-melhorias — skills grupo comercial/retenção
- Populadas 5 linhas de skills (auditoria-pipeline, cross-sell-hunt, plano-retencao, qualificacao-lead, abordagem-comercial)
- auditoria-pipeline: gatilho ausente + dimensão "distribuição equilibrada" sem critério numérico + fonte da Meta Mensal não especificada
- cross-sell-hunt: gatilho e cadência ausentes + probabilidades sem calibração histórica + lógica de rotação de clientes inexistente
- plano-retencao: gatilho ausente + SLA de aprovação do Marco indefinido para clientes Críticos + output não definido para causa raiz indeterminável
- qualificacao-lead: score não inteiro por critério de contato (0.5) inconsistente com faixas de classificação inteiras + score não gravado no Monday + campo de motivo de descarte não definido
- abordagem-comercial: gatilho ausente em todas as 5 situações de template + template de email prometido nas regras mas inexistente na SKILL.md + limite de caracteres WhatsApp ambíguo
- Key points atualizado: 10 de 14 skills com melhorias definidas; Summary da página atualizado

## [2026-04-14] refactor | backlog-melhorias — skills grupo conteúdo/crescimento
- Populadas 4 linhas de skills (analise-campanhas, nutricao-lead, criacao-conteudo, segmentacao-carteira)
- analise-campanhas: gatilho ausente + custo sem fonte/coluna definida + divisão por zero não tratada em ROI/CPL/taxa
- nutricao-lead: gatilho ausente + limite de ciclos de cadência indefinido (risco de loop infinito) + templates incompletos para 2 personas (dias 7/10/14 faltando)
- criacao-conteudo: gatilho e formato de saída ausentes + processo de aprovação de cases não documentado + faixa de preço no one-pager sem fonte de dados especificada
- segmentacao-carteira: gatilho ausente + sem fallback quando health score não calculado + Marco omitido da distribuição por corretor + "contato direto" sem definição operacional
- Key points atualizado: 14 de 14 skills com melhorias definidas — backlog de skills completo; Summary da página atualizado
