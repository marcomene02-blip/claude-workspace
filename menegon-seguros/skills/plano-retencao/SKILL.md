---
name: Plano de Retenção
description: Construir planos individuais de recuperação para clientes em risco de churn, com diagnóstico de causa raiz, ação recomendada e script personalizado.
slug: plano-retencao
schema: agentcompanies/v1
version: 1.0.0
---

Skill para construir planos de recuperação individualizados. Cada plano identifica a causa raiz, define a ação correta e entrega um script pronto para o corretor.

## Causas raiz mais comuns

| Causa | Sinais no CRM | Ação recomendada |
|---|---|---|
| Preço alto | Comparou cotações, está "Em Análise" há dias | Contato proativo com nova cotação competitiva |
| Sinistro mal resolvido | Sinistro aberto/demorado + NPS baixo | Escalonar para Marco + acompanhar resolução pessoalmente |
| Falta de contato | Sem interação há 60+ dias | Ligar ou WhatsApp com conteúdo de valor |
| Concorrente ativo | Mencionou outro corretor/seguradora | Apresentar diferenciais + reforçar relacionamento |
| Mudança de vida | Mudança de emprego, cidade, estado civil | Revisão completa da carteira + adequação ao novo momento |

## Estrutura do plano (por cliente)

```
PLANO DE RECUPERAÇÃO — [Nome do Cliente]
Data: [data]
Gerado por: Executor de Retenção

Score de risco: XX/100 (Crítico/Em Risco)
Valor do prêmio anual: R$ X.XXX
Corretor responsável: [Nome]

CAUSA RAIZ IDENTIFICADA:
[Descrição baseada em dados do CRM]

AÇÃO RECOMENDADA:
[O que fazer, como fazer, até quando]

SCRIPT DE WhatsApp:
"[Texto pronto, no tom humano, com o nome do cliente]"

PRAZO: [data limite para o primeiro contato]

MÉTRICA DE SUCESSO:
[O que significa "recuperado" neste caso]

STATUS: Aguardando aprovação do Marco
```

## Regras críticas

- Script nunca pode ser genérico — deve ter nome do cliente, produto específico, contexto real
- Causa raiz deve ser baseada em evidência do CRM, não em suposição
- Nunca recomendar desconto sem aprovação do Marco
- Plano de cliente com prêmio > R$ 5.000/ano → Marco deve ser o responsável pelo contato
