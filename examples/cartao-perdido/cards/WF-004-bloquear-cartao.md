---
id: WF-004
card_type: workflow
title: Bloquear cartão
status: draft
risk_level: R2
triggered_by:
  - "EVT-002"
requires:
  - "VAR-001"
  - "VAR-021"
uses:
  - "TOOL-007"
success_event: "EVT-003"
error_event: "EVT-004"
timeout_event: "EVT-005"
governed_by:
  - "RISK-008"
escalates_to:
  - "HO-003"
tested_by:
  - "TEST-034"
evaluated_by:
  - "EVAL-006"
measured_by:
  - "METRIC-011"
owner: Operações de cartões
---

# WF-004 — Bloquear cartão

## Objetivo obrigatório

Bloquear exatamente o cartão selecionado pelo cliente e comunicar apenas o resultado confirmado pelo sistema.

## Pré-condições obrigatórias

- `is_authenticated = true`.
- Um único `selected_card_id` validado e apresentado de forma mascarada.
- Consequências explicadas ao cliente.
- Confirmação explícita registrada.

## Sequência controlada

1. Validar autenticação e sessão.
2. Confirmar o cartão selecionado com dados mascarados.
3. Explicar efeito e reversibilidade do bloqueio.
4. Solicitar confirmação explícita.
5. Gerar `correlation_id` e `idempotency_key`.
6. Chamar [TOOL-007-api-bloqueio](TOOL-007-api-bloqueio.md).
7. Interpretar o resultado real da ferramenta.
8. Emitir o evento correspondente e informar protocolo quando disponível.

## Regras obrigatórias

- Nunca inferir qual cartão deve ser bloqueado.
- Nunca declarar sucesso sem `blocked = true` retornado pela ferramenta.
- Não repetir a operação com uma nova chave de idempotência após timeout.
- Encaminhar falhas persistentes ou suspeita de fraude para [HO-003-cartoes-fraude](HO-003-cartoes-fraude.md).

## Variáveis selecionáveis

| Campo | Valores predefinidos |
|---|---|
| `confirmation_mode` | `explicit_text`, `button`, `authenticated_action` |
| `retry_policy` | `no_retry`, `same_key_once`, `handoff` |
| `reversibility` | `reversible`, `conditionally_reversible`, `irreversible` |
| `fallback_route` | `retry`, `human_handoff`, `emergency_channel` |

