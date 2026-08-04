---
id: EVT-003
card_type: event
title: Bloqueio confirmado
status: draft
event_type: domain
severity: info
emitted_by:
  - "[[TOOL-007-api-bloqueio|API de bloqueio]]"
caused_by:
  - "[[WF-004-bloquear-cartao|Bloquear cartão]]"
consumed_by:
  - "[[EVAL-006-resolucao-segura|Resolução segura]]"
  - "[[METRIC-011-tempo-protecao|Tempo até proteção]]"
payload: [selected_card_id, protocol_id, completed_at, correlation_id, idempotency_key]
correlation_key: correlation_id
owner: Operações de cartões
---

# EVT-003 — Bloqueio confirmado

## Significado obrigatório

O sistema responsável confirmou que o cartão selecionado foi bloqueado.

## Payload obrigatório

- `selected_card_id` — identificador interno do cartão confirmado.
- `protocol_id` — protocolo devolvido pelo sistema, quando aplicável.
- `completed_at` — data e hora ISO 8601.
- `correlation_id` — o mesmo identificador iniciado na cadeia.
- `idempotency_key` — chave utilizada na operação.

## Consumidores esperados

- A conversa, para informar conclusão e próximos passos.
- [[EVAL-006-resolucao-segura]], para classificar o desfecho.
- [[METRIC-011-tempo-protecao]], para encerrar a medição.

## Regra de idempotência

Eventos com a mesma combinação de `selected_card_id` e `idempotency_key` representam o mesmo resultado e não devem duplicar efeitos.
