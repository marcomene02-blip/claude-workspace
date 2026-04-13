# Menegon Seguros — Empresa de Agentes no Paperclip

Modelo completo de empresa para a **Menegon Seguros** no formato [Agent Companies spec](https://agentcompanies.io/specification), pronto para importar no [Paperclip](https://paperclip.ing/).

## Importar

```bash
paperclipai company import --from ./menegon-seguros
```

Ou dry-run para validar antes:

```bash
paperclipai company import --from ./menegon-seguros --dry-run
```

---

## Estrutura

```
menegon-seguros/
├── COMPANY.md                          # Raiz da empresa
├── README.md                           # Este arquivo
│
├── agents/
│   ├── diretor-comercial/              # Marco — CEO / aprovador final
│   ├── gerente-comercial/              # Coordena o núcleo comercial
│   ├── especialista-renovacao/         # Foco em carteira existente
│   ├── especialista-seguro-novo/       # Foco em novos negócios
│   ├── hunter-cross-sell/              # Expande receita na base ativa
│   ├── qualificador-leads/             # Qualifica e prioriza leads
│   ├── analista-churn/                 # Detecta risco de não-renovação
│   ├── executor-retencao/              # Executa planos de recuperação
│   ├── analista-nps/                   # Analisa satisfação e detratores
│   ├── cmo/                            # Estratégia de marketing
│   ├── analista-campanhas/             # Performance de campanhas
│   ├── criador-conteudo/               # Materiais e posts
│   ├── especialista-inbound/           # Geração e nutrição de leads
│   ├── analista-pipeline/              # Auditoria e saúde do pipeline
│   ├── analista-forecast/              # Previsão de receita semanal
│   └── analista-performance/           # KPIs e diagnóstico comercial
│
├── skills/
│   ├── monday-crm-query/               # Consultar dados do Monday CRM
│   ├── monday-crm-write/               # Registrar updates e notificações
│   ├── forecast-ponderado/             # Calcular forecast com 3 cenários
│   ├── analise-churn/                  # Score de risco por cliente
│   ├── auditoria-pipeline/             # Health check do pipeline
│   ├── cross-sell-hunt/                # Identificar gaps de produto
│   ├── plano-retencao/                 # Gerar plano de recuperação
│   ├── analise-campanhas/              # Calcular KPIs de campanha
│   ├── qualificacao-lead/              # Pontuar e priorizar leads
│   └── abordagem-comercial/            # Gerar script de abordagem
│
└── teams/
    ├── comercial/                      # Renovação + Seguro Novo + Leads
    ├── crm-fidelizacao/                # Churn + Retenção + NPS
    └── marketing/                      # CMO + Campanhas + Conteúdo + Inbound
```

---

## Núcleos e Responsabilidades

| Núcleo | Agentes | Objetivo Principal |
|---|---|---|
| **Comercial** | 5 | Fechar renovações, novos seguros e cross-sells |
| **CRM & Fidelização** | 3 | Reter clientes, recuperar detratores, expandir LTV |
| **Marketing** | 4 | Gerar leads qualificados e nutrir a base |
| **Operacional** | 3 | Visibilidade do pipeline, forecast e performance |

---

## Integrações

- **Monday CRM** (workspace 11267903) — fonte de verdade para todos os agentes
- **Google Calendar** — agendamentos de follow-up e reuniões
- **WhatsApp** — canal de contato preferencial (via scripts gerados pelos agentes)

---

## Rotinas Ativas

| Frequência | Hora | Agente Responsável |
|---|---|---|
| Seg–Sex | 07:30 | Analista de Pipeline (briefing matinal) |
| Seg–Sex | 18:00 | Analista de Performance (fechamento) |
| Segunda | 10:00 | Analista de Churn (varredura semanal) |
| Quarta | 09:00 | Hunter de Cross-sell |
| Sexta | 14:00 | Analista de Forecast |
| Sábado | 09:00 | Alerta de vencimentos críticos |
| Domingo | 20:00 | Consolidação semanal |
| Dia 1 | 08:00 | Relatório mensal completo |
