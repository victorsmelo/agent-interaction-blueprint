---
id: PB-012
card_type: playbook
title: Entender ocorrência de cartão
status: validating
owner: Produtos Cartões
treatment_type: agentic
risk_level: R2-sensitive
channels: [mobile_app, web]
relations:
  triggered_by: ["[[EVT-001-perda-reportada|Perda reportada]]"]
  emits: ["[[EVT-002-cartao-selecionado|Cartão selecionado]]"]
  queries_kb: ["[[KB-003-politica-cartoes|Política de cartões]]"]
  reads:
    - "[[VAR-001-is-authenticated|Cliente autenticado]]"
    - "[[VAR-021-active-cards|Cartões ativos]]"
  routes_to: ["[[WF-004-bloquear-cartao|Bloquear cartão]]"]
  governed_by: ["[[RISK-008-bloqueio-cartao-incorreto|Bloqueio do cartão incorreto]]"]
  escalates_to: ["[[HO-003-cartoes-fraude|Cartões e Fraude]]"]
  tested_by: ["[[TEST-034-multiplos-cartoes|Cliente com múltiplos cartões]]"]
  evaluated_by: ["[[EVAL-006-resolucao-segura|Resolução segura]]"]
  measured_by: ["[[METRIC-011-tempo-protecao|Tempo até proteção]]"]
---

# PB-012 — Entender ocorrência de cartão

## Objetivo

Compreender se houve perda, roubo, ausência temporária de posse ou suspeita de fraude; identificar o cartão correto e preparar uma ação segura.

## Quando usar

- Cliente relata perda, roubo ou que não encontra o cartão físico.
- A intenção ainda precisa ser diferenciada de compra não reconhecida ou cartão retido.

## Quando não usar

- Contestação de transação sem perda do cartão.
- Pedido de desbloqueio.
- Cartão retido em caixa eletrônico.

## Comportamento esperado

1. Reconhecer urgência sem dramatizar.
2. Fazer uma pergunta por vez.
3. Desambiguar perda, roubo e fraude.
4. Consultar apenas cartões elegíveis.
5. Exibir marca e final mascarado.
6. Coletar seleção explícita.
7. Explicar que o bloqueio exige confirmação no workflow.

## Ações proibidas

- Escolher o cartão por suposição.
- Expor número completo ou dado de autenticação.
- Declarar que o cartão foi bloqueado.

## Saídas

- Cartão selecionado: emitir [[EVT-002-cartao-selecionado|Cartão selecionado]].
- Falta de confiança, falha de autenticação ou fraude crítica: encaminhar para [[HO-003-cartoes-fraude|Cartões e Fraude]].

