---
id: METRIC-011
card_type: metric
title: Tempo até proteção
status: draft
metric_type: duration
unit: seconds
starts_at:
  - "[[EVT-001-perda-reportada|Perda reportada]]"
ends_at:
  - "[[EVT-003-bloqueio-confirmado|Bloqueio confirmado]]"
  - "[[HO-003-cartoes-fraude|Handoff aceito por cartões e fraude]]"
related_evaluation:
  - "[[EVAL-006-resolucao-segura|Resolução segura]]"
owner: Operações e analytics
---

# METRIC-011 — Tempo até proteção

## Definição obrigatória

Tempo decorrido entre o relato de perda e a primeira proteção confirmada ou a aceitação de um handoff seguro pela equipe especializada.

## Fórmula

`tempo_ate_protecao_seg = timestamp_fim - timestamp_perda_reportada`

## Início e fim

- Início: `occurred_at` de [[EVT-001-perda-reportada]].
- Fim primário: `completed_at` de [[EVT-003-bloqueio-confirmado]].
- Fim alternativo: aceite comprovado de [[HO-003-cartoes-fraude]].

## Dimensões selecionáveis

| Campo | Valores predefinidos |
|---|---|
| `outcome` | `blocked`, `handoff`, `safe_stop`, `abandoned`, `unresolved` |
| `channel` | `web_chat`, `app_chat`, `whatsapp`, `voice`, `other` |
| `incident_type` | `lost`, `stolen`, `temporarily_missing`, `fraud_suspected` |
| `authentication_state` | `authenticated`, `not_authenticated`, `expired` |
| `tool_result` | `success`, `rejected`, `error`, `timeout`, `not_called` |

## Exclusões obrigatórias

- Testes e ambientes não produtivos.
- Conversas duplicadas unidas pelo mesmo `correlation_id`.
- Contatos sem relato de perda ou necessidade de proteção.

## Metas a definir

- Percentil principal: `p50`, `p75`, `p90` ou `p95`.
- Meta de tempo por canal e nível de risco.
- Limite de alerta operacional.

