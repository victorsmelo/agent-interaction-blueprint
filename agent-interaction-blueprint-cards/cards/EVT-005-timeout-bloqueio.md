---
id: EVT-005
card_type: event
title: Timeout do bloqueio
status: draft
event_type: exception
severity: critical
emitted_by:
  - "[[TOOL-007-api-bloqueio|API de bloqueio]]"
caused_by:
  - "[[WF-004-bloquear-cartao|Bloquear cartão]]"
consumed_by:
  - "[[HO-003-cartoes-fraude|Cartões e fraude]]"
  - "[[EVAL-006-resolucao-segura|Resolução segura]]"
owner: Tecnologia de cartões
---

# EVT-005 — Timeout do bloqueio

## Significado obrigatório

O limite de espera terminou sem um resultado conclusivo; o efeito real da operação pode ser desconhecido.

## Payload obrigatório

- `selected_card_id`.
- `correlation_id`.
- `idempotency_key`.
- `latency_ms`.
- `retry_count`.
- `occurred_at` em ISO 8601.

## Comportamento esperado

- Tratar o estado como `unknown`, nunca como sucesso ou falha definitiva.
- Consultar status, se existir uma operação segura para isso.
- Repetir somente com a mesma `idempotency_key` e conforme política aprovada.
- Oferecer [[HO-003-cartoes-fraude]] ou canal emergencial.

## Variáveis selecionáveis

| Campo | Valores predefinidos |
|---|---|
| `customer_message` | `temporary_issue`, `status_unknown`, `emergency_handoff` |
| `next_action` | `check_status`, `retry_same_key`, `handoff` |
| `urgency` | `normal`, `high`, `critical` |

