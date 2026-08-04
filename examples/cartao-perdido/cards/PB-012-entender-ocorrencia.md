---
id: PB-012
card_type: playbook
title: Entender ocorrência de cartão
status: validating
owner: Produtos Cartões
treatment_type: agentic
risk_level: R2-sensitive
channels: [mobile_app, web]
triggered_by: ["EVT-001"]
emits: ["EVT-002"]
queries_kb: ["KB-003"]
reads:
  - "VAR-001"
  - "VAR-021"
routes_to: ["WF-004"]
governed_by: ["RISK-008"]
escalates_to: ["HO-003"]
tested_by: ["TEST-034"]
evaluated_by: ["EVAL-006"]
measured_by: ["METRIC-011"]
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

- Cartão selecionado: emitir [Cartão selecionado](EVT-002-cartao-selecionado.md).
- Falta de confiança, falha de autenticação ou fraude crítica: encaminhar para [Cartões e Fraude](HO-003-cartoes-fraude.md).
