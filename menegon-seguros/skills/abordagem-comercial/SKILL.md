---
name: Abordagem Comercial
description: Gerar scripts personalizados de abordagem para WhatsApp e email, baseados no perfil do cliente/lead e no produto de interesse.
slug: abordagem-comercial
schema: agentcompanies/v1
version: 1.0.0
---

Skill para criar scripts de abordagem comercial contextualizados. Produz textos prontos para uso no WhatsApp ou email pelo corretor responsável.

## Quando usar

**Quem invoca:** qualquer agente que precise gerar script de contato com cliente ou lead.

**Acionar quando:**
1. Lead novo entra no pipeline e precisa de mensagem de abertura (indicação ou inbound)
2. Renovação a ≤ 30 dias sem cotação enviada — script de renovação próxima
3. Follow-up sem resposta após 3+ dias — script de segundo contato
4. Oportunidade de cross-sell identificada pelo hunter-cross-sell — script de cross-sell
5. Cliente classificado como Em Risco pelo analista-churn — script de recuperação

**Não acionar** para comunicações internas entre agentes ou para notificações automáticas no Monday — apenas para scripts destinados a clientes reais.

## Princípios de comunicação Menegon

1. **Humano primeiro** — começa pela pessoa, não pelo produto
2. **Uma pergunta por mensagem** — nunca sobrecarregue o cliente
3. **Curto para WhatsApp** — máximo 320 caracteres (padrão WhatsApp Business) — contar antes de enviar
4. **Contexto real** — use o nome, o produto específico, a situação concreta
5. **Chamada para ação clara** — sempre termina com um próximo passo definido

## Templates por situação

### Abertura — lead novo (indicação)
```
Oi [Nome], tudo bem?
Sou [Corretor] da Menegon Seguros.
[Quem indicou] me falou que você pode precisar de [produto].
Posso te mandar uma cotação rápida pra você ver?
```

### Abertura — renovação próxima
```
Oi [Nome]! Aqui é [Corretor] da Menegon.
Seu [produto] vence em [prazo] e já preparei algumas opções pra você.
Posso te enviar agora?
```

### Follow-up — sem resposta (2º contato)
```
Oi [Nome], tentei te falar essa semana.
Queria garantir que você não fica sem proteção no [produto].
Quando seria um bom momento pra conversar?
```

### Cross-sell — cliente ativo
```
Oi [Nome]! Já cuidamos do seu [produto atual] há [tempo].
Vi uma oportunidade de proteger também [novo produto] por um valor bem acessível.
Posso te mandar os detalhes?
```

### Recuperação — cliente em risco
```
Oi [Nome], tudo bem?
Aqui é [Corretor]. Faz um tempo que não falamos e queria saber como você está.
[Contexto específico, ex: "Sei que teve um sinistro recentemente"] —
quero garantir que você está satisfeito com nosso atendimento.
Podemos conversar?
```

### Email — renovação

```
Assunto: Seu [produto] vence em [prazo] — veja as opções que preparei

Olá, [Nome].

Seu seguro de [produto] está próximo do vencimento ([data]) e já preparei algumas opções de renovação para você comparar.

[Opção 1]: [Seguradora A] — R$ X/mês — [cobertura resumida]
[Opção 2]: [Seguradora B] — R$ Y/mês — [cobertura resumida]

Posso te ligar amanhã para conversar sobre a melhor opção?

[Corretor]
Menegon Seguros | [telefone]
```

### Email — cross-sell

```
Assunto: Uma proteção que faz sentido para você, [Nome]

Olá, [Nome].

Já cuidamos do seu [produto atual] há [tempo] e queria te mostrar uma oportunidade.

Clientes com [produto atual] que adicionam [novo produto] ficam com uma cobertura muito mais completa — e o custo adicional costuma ser menor do que se imagina.

Preparei uma proposta rápida. Posso te enviar por aqui ou prefere uma ligação?

[Corretor]
Menegon Seguros | [telefone]
```

## Regras críticas

- Nunca use scripts genéricos — o nome do cliente é obrigatório
- Evite jargão técnico de seguro (franquia, prêmio, sinistro) no primeiro contato
- Emojis: máximo 1 por mensagem, nunca no início
- Email: tom mais formal, estrutura com assunto, corpo e CTA claro
