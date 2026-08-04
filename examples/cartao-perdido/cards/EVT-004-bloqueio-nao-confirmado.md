---
id: EVT-004
card_type: event
title: Bloqueio não confirmado
status: draft
event_type: exception
severity: high
emitted_by:
  - "[[TOOL-007-api-bloqueio|API de bloqueio]]"
caused_by:
  - "[[WF-004-bloquear-cartao|Bloquear cartão]]"
consumed_by:
  - "[[HO-003-cartoes-fraude|Cartões e fraude]]"
  - "[[EVAL-006-resolucao-segura|Resolução segura]]"
payload: [selected_card_id, tool_status, error_code, retry_count, correlation_id, idempotency_key, occurred_at]
correlation_key: correlation_id
owner: Operações de cartões
---

# EVT-004 — Bloqueio não confirmado

## Significado obrigatório

A ferramenta respondeu, mas não confirmou que o cartão foi bloqueado.

## Payload obrigatório

- `selected_card_id`.
- `tool_status` — `rejected`, `error` ou `unknown`.
- `error_code`, quando disponível.
- `retry_count`.
- `correlation_id`.
- `idempotency_key`.
- `occurred_at` em ISO 8601.

## Comportamento esperado

- Não afirmar que o bloqueio ocorreu.
- Explicar a situação em linguagem simples, sem expor detalhes internos.
- Aplicar a política de repetição definida em [[WF-004-bloquear-cartao]].
- Encaminhar para [[HO-003-cartoes-fraude]] quando não houver recuperação segura.
