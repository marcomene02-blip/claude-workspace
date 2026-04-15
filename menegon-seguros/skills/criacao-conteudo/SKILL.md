---
name: Criação de Conteúdo
description: Produzir scripts de WhatsApp, one-pagers, posts, emails de nurturing, propostas e cases de cliente para a Menegon Seguros, sempre com voz humana e contextualizada.
slug: criacao-conteudo
schema: agentcompanies/v1
version: 1.0.0
---

Skill para criar qualquer material de comunicação da Menegon Seguros. Cobre scripts de abordagem, materiais de vendas, conteúdo educativo e provas sociais.

## Quando usar

**Agente invocador:** `criador-conteudo`

| Gatilho | Conteúdo gerado |
|---|---|
| Novo lead — Dia 0 (inbound) | Script WhatsApp de apresentação |
| Lead sem resposta — Dia 3–7 | Script WhatsApp de follow-up |
| Lead morno — Dia 14+ | E-mail de nurturing |
| Campanha ativa | Post para redes sociais / anúncio |
| Cliente promotor (NPS 9–10) | Mensagem de pedido de indicação |

**Formato de saída obrigatório:**
- `tipo`: categoria do conteúdo (script-whatsapp, email, post, anuncio, mensagem-indicacao)
- `canal`: whatsapp | email | instagram | linkedin
- `versao`: número sequencial (ex.: v1)
- `texto`: conteúdo pronto para envio

## Voz e tom Menegon

| Atributo | O que significa na prática |
|---|---|
| **Humano** | Começa pela pessoa, não pelo produto. Usa o nome. Menciona contexto real. |
| **Simples** | Zero jargão técnico (sem "prêmio", "franquia", "sinistro" no primeiro contato). |
| **Direto** | Uma ideia por mensagem. Uma pergunta por vez. |
| **Confiante** | Posiciona a Menegon como especialista, não como vendedor. |
| **Local** | Linguagem de quem conhece a vida do cliente (cidade, profissão, família). |

## Tipos de conteúdo e estruturas

### Script de WhatsApp (abordagem / follow-up)
- **Tamanho**: máximo 5 linhas
- **Estrutura**: cumprimento + contexto + uma pergunta ou CTA
- **Emojis**: máximo 1, nunca no início
- **Tom**: conversa, não mensagem de empresa

### One-pager de produto (email ou PDF)
- **Estrutura**:
  1. Título — o problema que o produto resolve (não o nome do produto)
  2. Para quem é — persona em linguagem simples
  3. O que cobre — 3 coberturas principais em bullet
  4. Quanto custa — faixa estimada ou "solicite cotação"
  5. CTA — "Fale com [Corretor]"
- **Tamanho**: 1 página A4 ou email de até 300 palavras

### Post educativo (Instagram / LinkedIn)
- **Estrutura**: gancho (pergunta ou dado impactante) + desenvolvimento + CTA suave
- **Tamanho**: 80–150 palavras no corpo
- **Tom**: Instagram = mais leve; LinkedIn = mais profissional, para PJ
- **Imagem sugerida**: descrever o visual em 1 frase para o designer

### Email de nurturing (cadência)
- **Assunto**: faz uma pergunta ou apresenta um cenário de risco real
- **Corpo**: 2 parágrafos educativos + 1 parágrafo de CTA
- **Assinatura**: sempre com nome do corretor responsável, não "Menegon Seguros" genérico

### Proposta personalizada (email + PDF)
- **Estrutura**:
  1. Contexto do cliente (o que ele precisa proteger)
  2. Solução recomendada com justificativa
  3. Tabela comparativa (mínimo 3 seguradoras)
  4. Próximo passo claro com prazo
- **Regra**: nunca envie proposta sem ter entendido o que o cliente realmente precisa proteger

### Case de cliente (prova social)
- **Estrutura**: situação (o que aconteceu) → solução (o seguro cobriu) → resultado (o que mudou para o cliente)
- **Tamanho**: 3–5 frases para WhatsApp; parágrafo completo para email
- **Atenção**: usar apenas casos reais ou composites aprovados — nunca inventar dados

## Regras críticas

- O nome do cliente ou corretor responsável é **obrigatório** em todo material
- Nunca invente dados, estatísticas ou resultados — use os reais do CRM ou deixe espaço em branco
- Evite jargão técnico de seguro nos primeiros contatos: franquia, prêmio, sinistro, LMI
- Scripts de WhatsApp: máximo 5 linhas, uma pergunta no final
- Email: sempre com assunto personalizado (nunca "Seguro Auto" genérico)
- Todo material deve ter CTA claro — o próximo passo deve ser óbvio para o leitor

## Produtos e ângulos de valor por persona

| Produto | Persona principal | Argumento central |
|---|---|---|
| Auto | Motorista PF, carro novo ou financiado | Patrimônio + terceiros + assistência 24h |
| Residencial | Família com casa própria | Proteção do lar, eletrodomésticos, responsabilidade vizinhos |
| Vida Individual | 30–55 anos, família dependente | Futuro da família se faltar o provedor |
| Previdência | 25–50 anos, MEI ou CLT | Aposentadoria complementar + benefício fiscal |
| Empresarial | MEI, ME, empresas até 50 funcionários | Continuidade do negócio em caso de sinistro |
| Vida em Grupo | Empresas com 5+ funcionários | Benefício competitivo para reter talentos |
| Residencial Cond. | Síndico ou administradora | Cobertura das áreas comuns e responsabilidade civil |
