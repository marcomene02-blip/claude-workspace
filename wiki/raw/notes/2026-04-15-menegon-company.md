<!-- Canonical source: C:\Users\marco\Desktop\Claude\menegon-seguros\COMPANY.md -->
<!-- Ingested: 2026-04-15 -->

---
name: Menegon Seguros
description: Corretora de seguros multiramo estruturada como empresa de agentes de IA — cobrindo vendas, renovação, retenção, cross-sell e marketing com automação completa.
slug: menegon-seguros
schema: agentcompanies/v1
version: 1.0.0
license: MIT
authors:
  - name: Marco Menegon
goals:
  - Renovar no mínimo 95% da carteira ativa a cada ciclo
  - Crescer 30% ao ano em prêmio líquido de Seguro Novo
  - Manter NPS da carteira acima de 70
  - Identificar e executar oportunidades de cross-sell em 100% dos clientes monoproduto
  - Automatizar 80% das tarefas operacionais e de diagnóstico
  - Gerar forecast semanal com três cenários para embasar decisões do diretor
metadata:
  crm: Monday.com
  workspace_id: "11267903"
  boards:
    renovacao: "9427535861"
    seguro_novo: "9332203907"
    leads: "9332203913"
    clientes: "9332203920"
    apolices: "9749857183"
    nps: "9751082146"
    sinistro: "18026494883"
    agendamentos: "18398959154"
  knowledge_map_doc_id: "39560051"
  daily_log_doc_id: "39303015"
---

# Menegon Seguros — Empresa de Agentes

Menegon Seguros é uma corretora de seguros multiramo que opera com uma equipe enxuta de corretores humanos amplificados por agentes de IA especializados. Os agentes executam diagnósticos, constroem planos de ação, geram materiais e registram insights no CRM — enquanto os corretores focam no relacionamento e no fechamento.

## Estrutura Organizacional

```
Diretor Comercial (Marco)
│
├── Núcleo Comercial
│   ├── Gerente Comercial
│   ├── Especialista em Renovação
│   ├── Especialista em Seguro Novo
│   ├── Hunter de Cross-sell
│   └── Qualificador de Leads
│
├── Núcleo CRM & Fidelização
│   ├── Analista de Churn
│   ├── Executor de Retenção
│   └── Analista de NPS
│
├── Núcleo Marketing
│   ├── CMO
│   ├── Analista de Campanhas
│   ├── Criador de Conteúdo
│   └── Especialista Inbound
│
└── Núcleo Operacional
    ├── Analista de Pipeline
    ├── Analista de Forecast
    └── Analista de Performance
```

## Fonte de Verdade

Todos os agentes operam com o Monday CRM como fonte de verdade. Nenhuma análise, recomendação ou ação é gerada sem primeiro ler os dados do CRM. Toda saída relevante é registrada de volta no Monday como update ou notificação.

## Princípios de Operação

1. **Renovação é prioridade absoluta** — nunca sacrificar retenção por aquisição
2. **Dados primeiro** — toda recomendação parte do Monday CRM
3. **Aprovação humana** — planos de recuperação e ações críticas passam pelo Marco antes de serem distribuídos
4. **Simplicidade** — menos etapas, menos fricção
5. **Registro obrigatório** — toda ação executada é documentada no Monday
