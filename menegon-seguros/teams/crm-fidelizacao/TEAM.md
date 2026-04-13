---
name: Núcleo CRM & Fidelização
description: Time responsável por reter clientes, recuperar detratores e maximizar o LTV da carteira ativa.
slug: crm-fidelizacao
schema: agentcompanies/v1
version: 1.0.0
---

# Núcleo CRM & Fidelização

O Núcleo CRM & Fidelização protege a receita recorrente da Menegon Seguros. Enquanto o Comercial busca novas receitas, este núcleo garante que a base existente não se perca.

## Composição

| Agente | Papel |
|---|---|
| Analista de Churn | Detecta risco de perda antes que aconteça |
| Executor de Retenção | Constrói e executa planos de recuperação |
| Analista de NPS | Transforma satisfação em ação |

## Cadência de operação

| Momento | Ação |
|---|---|
| Segunda 10:00 | Analista de Churn executa varredura semanal |
| Após varredura | Executor recebe lista e constrói planos |
| Após aprovação do Marco | Executor registra planos no Monday e notifica corretores |
| Quando chega NPS | Analista de NPS classifica e aciona recuperação para detratores |
| Dia 1 do mês | Relatório consolidado de retenção para o Diretor |

## Fluxo integrado

```
Analista de Churn
  → lista priorizada de clientes em risco
    → Executor de Retenção
      → planos individuais de recuperação
        → Aprovação do Marco
          → Registro no Monday + Notificação ao corretor
            → Corretor executa o contato
              → Resultado registrado no Monday
                → Analista de Churn monitora evolução
```

## Integração com outros núcleos

- Recebe feedback de sinistros do board de Sinistro (18026494883)
- Integra NPS com histórico de renovação para diagnóstico completo
- Envia clientes recuperados com oportunidade de cross-sell para o **Hunter de Cross-sell**
- Escala casos críticos diretamente para o **Diretor Comercial**
