---
name: Nutrição de Lead
description: Conduzir leads mornos (score 5–7) por uma cadência de 14 dias com mensagens educativas e provas sociais, até ficarem prontos para compra ou serem descartados com motivo registrado.
slug: nutricao-lead
schema: agentcompanies/v1
version: 1.0.0
---

> **Config:** leia `menegon-seguros/config/thresholds/nutricao-lead.yaml` no início da execução para obter os thresholds atuais. Os valores neste documento são apenas referência inicial — o YAML tem precedência.

Skill para executar a cadência de nurturing de leads mornos. Produz a sequência completa de mensagens por persona, com timing, canal e critérios de saída.

## Quando usar

- **`especialista-inbound`** — invocar quando um lead conclui o fluxo inbound de 14 dias sem converter e seu status no Monday CRM é "Morno" ou "Morto".
- **`executor-retencao`** — invocar para clientes em risco (health score 40–60) que não responderam em 7 ou mais dias de follow-up.
- **Limite de ciclos:** máximo 2 cadências completas por lead/cliente. Se não houver resposta após o 2º ciclo, descartar com motivo "Esgotado após 2 cadências".
- **Não invocar** para clientes Críticos (score < 40) — encaminhar diretamente para a skill `plano-retencao`.

## Cadência padrão (14 dias)

| Dia | Canal | Tipo de mensagem | Objetivo |
|---|---|---|---|
| 0 | WhatsApp | Boas-vindas + diagnóstico | Entender a necessidade real |
| 3 | Email | Conteúdo educativo | Mostrar por que o produto importa |
| 7 | WhatsApp | Prova social / case | Gerar confiança com história real |
| 10 | WhatsApp | Convite para cotação | Chamada para ação clara |
| 14 | WhatsApp | Requalificação ou descarte | Decidir o próximo passo |

## Critérios de saída antecipada

- **Avança** (passa para Especialista): responde positivamente em qualquer etapa, pede cotação, aceita conversar
- **Descarta** (arquiva com motivo): não responde em nenhum dos 5 contatos, diz explicitamente que não tem interesse, número inválido
- **Continua**: responde mas ainda não está pronto — reinicia cadência do dia 3

## Templates por persona

### Motorista PF — produto Auto

**Dia 0 — WhatsApp boas-vindas**
```
Oi [Nome], tudo bem?
Sou [Corretor] da Menegon Seguros.
Vi que você tem interesse em seguro de carro — qual modelo você tem?
```

**Dia 3 — Email educativo**
```
Assunto: Seu carro está realmente protegido?

[Nome], você sabia que [X]% dos motoristas ficam desprotegidos
nos primeiros dias após vencer o seguro?

[Parágrafo sobre riscos: colisão, furto, terceiros]

Quando quiser comparar opções, é só responder este email.
[Corretor] — Menegon Seguros
```

**Dia 7 — WhatsApp prova social**
```
Oi [Nome]! Semana passada um cliente aqui em [cidade]
teve o carro batido na saída da escola do filho.
O seguro cobriu tudo — carro reserva, guincho, reparo.
Você teria essa tranquilidade hoje?
```

**Dia 10 — WhatsApp CTA**
```
Oi [Nome], ainda consigo preparar uma cotação pra você essa semana.
Leva 5 minutos — só preciso do modelo e ano do carro.
Quer que eu mande as opções?
```

**Dia 14 — Requalificação**
```
Oi [Nome], esse será meu último contato por enquanto.
Se você ainda estiver pensando no seguro, pode me chamar quando quiser.
Guardo seu cadastro aqui com carinho.
```

---

### Família com casa própria — produto Residencial

**Dia 0**
```
Oi [Nome]! Sou [Corretor] da Menegon.
Você mora em casa própria ou apartamento?
Quero entender o que faria mais sentido pra você.
```

**Dia 3 — Email**
```
Assunto: O que acontece se sua casa pegar fogo amanhã?

[Nome], residencial não é só incêndio — cobre raio, roubo,
danos elétricos e até responsabilidade com vizinhos.
[2 parágrafos educativos sobre coberturas]
```

**Dia 7 — WhatsApp**
```
Oi [Nome]! Uma cliente nossa em [cidade] teve um curto-circuito
que queimou os eletrodomésticos todos. O seguro residencial cobriu
a reposição completa em 15 dias.
```

**Dia 10 — CTA**
```
[Nome], consigo fazer uma cotação de residencial pra você em minutos.
Qual o endereço aproximado do imóvel?
```

---

### MEI / Empresário — produto Empresarial

**Dia 0**
```
Oi [Nome], tudo bem?
Sou [Corretor] da Menegon Seguros.
Queria entender melhor o seu negócio — qual é o ramo?
```

**Dia 3 — Email**
```
Assunto: Se algo parar seu negócio amanhã, você está coberto?

[Nome], empresarial cobre incêndio, roubo de equipamentos,
responsabilidade civil e perda de lucros.
[2 parágrafos sobre impacto de sinistro sem seguro]
```

---

### 30–45 anos com família — produto Vida + Previdência

**Dia 0**
```
Oi [Nome]! Você já tem proteção pra sua família caso aconteça algo com você?
Tenho uma proposta que pode te surpreender no valor.
```

**Dia 3 — Email**
```
Assunto: Quanto custa proteger sua família por R$XX/mês?

[Nome], seguro de vida não é sobre morte — é sobre tranquilidade.
[Explicação de coberturas: invalidez, doenças graves, morte]
```

---

## Registro obrigatório no Monday

Após cada contato na cadência, registrar como update no item do lead:
- Data do contato
- Canal utilizado (WhatsApp/email)
- Resposta recebida (respondeu / não respondeu / sem interesse)
- Próximo passo planejado

## Regras críticas

- Nunca pule etapas: cadência é sequencial
- Todo lead descartado no dia 14 deve ter motivo registrado no Monday antes de arquivar
- Nunca force venda em lead que não está pronto — queima relacionamento e NPS futuro
- Personalizar sempre: nome, produto específico e contexto real (cidade, situação mencionada)
