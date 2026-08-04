---
id: TOOL-007
card_type: tool
title: API de bloqueio
status: draft
system: Plataforma de cartões
used_by:
  - "WF-004"
success_event: "EVT-003"
error_event: "EVT-004"
timeout_event: "EVT-005"
governed_by:
  - "RISK-008"
owner: Tecnologia de cartões
---

# TOOL-007 — API de bloqueio

## Responsabilidade obrigatória

Solicitar o bloqueio de um cartão e retornar uma evidência inequívoca do resultado.

## Entradas obrigatórias

| Campo | Regra |
|---|---|
| `customer_id` | Identificador interno; nunca expor ao cliente |
| `selected_card_id` | Deve corresponder ao cartão confirmado |
| `incident_type` | Valor do catálogo predefinido |
| `confirmation_event_id` | Evidência da confirmação explícita |
| `correlation_id` | Rastreia toda a cadeia de eventos |
| `idempotency_key` | Impede bloqueios duplicados |

## Saídas obrigatórias

| Campo | Valores ou formato |
|---|---|
| `blocked` | `true`, `false` |
| `status` | `success`, `rejected`, `error`, `timeout`, `unknown` |
| `protocol_id` | Texto; obrigatório no sucesso quando disponível |
| `completed_at` | Data e hora ISO 8601 |
| `error_code` | Catálogo técnico, quando houver falha |

## Política de resultado

- `blocked = true`: emitir [EVT-003-bloqueio-confirmado](EVT-003-bloqueio-confirmado.md).
- rejeição ou erro confirmado: emitir [EVT-004-bloqueio-nao-confirmado](EVT-004-bloqueio-nao-confirmado.md).
- ausência de resposta no limite: emitir [EVT-005-timeout-bloqueio](EVT-005-timeout-bloqueio.md).
- Status `unknown` nunca pode ser apresentado como sucesso.

## Variáveis selecionáveis

| Campo | Valores predefinidos |
|---|---|
| `authentication_scope` | `customer_read`, `card_block` |
| `timeout_policy` | `5s`, `10s`, `30s` |
| `retry_mode` | `never`, `same_idempotency_key_once` |
| `effect_type` | `read_only`, `reversible_write`, `irreversible_write` |
| `data_classification` | `public`, `internal`, `confidential`, `restricted` |

