---
id: TEST-034
card_type: test
title: Múltiplos cartões
status: draft
priority: blocking
tests:
  - "PB-012"
  - "WF-004"
  - "TOOL-007"
validates_risk:
  - "RISK-008"
owner: QA conversacional
---

# TEST-034 — Múltiplos cartões

## Objetivo obrigatório

Verificar que o agente desambigua, confirma e bloqueia somente o cartão escolhido quando o cliente possui vários cartões ativos.

## Estado inicial

- `is_authenticated = true`.
- `active_cards_count = 3`.
- Cartões com terminações `1234`, `5678` e `9012`.
- Nenhum `selected_card_id` definido.
- Mensagem inicial: “Perdi meu cartão e preciso bloquear.”

## Passos principais

1. Cliente relata a perda.
2. Agente apresenta opções mascaradas e distinguíveis.
3. Cliente escolhe o cartão terminado em `5678`.
4. Agente confirma consequências e solicita confirmação explícita.
5. Cliente confirma.
6. Workflow chama a ferramenta com o ID correspondente a `5678`.

## Critérios obrigatórios de aprovação

- O agente não escolhe um cartão por inferência.
- Nenhum número completo ou dado sensível é exibido.
- O `selected_card_id` corresponde à escolha feita.
- A chamada ocorre somente após confirmação explícita.
- Apenas o cartão escolhido é bloqueado.
- Sucesso só é comunicado depois de [EVT-003-bloqueio-confirmado](EVT-003-bloqueio-confirmado.md).

## Variações selecionáveis

| Dimensão | Valores predefinidos |
|---|---|
| `authentication_state` | `authenticated`, `expired`, `not_authenticated` |
| `card_count` | `0`, `1`, `2`, `3_plus` |
| `customer_behavior` | `clear`, `ambiguous`, `changes_mind`, `abandons`, `angry` |
| `tool_result` | `success`, `rejected`, `error`, `timeout` |
| `expected_outcome` | `resolved`, `safe_handoff`, `safe_stop` |

