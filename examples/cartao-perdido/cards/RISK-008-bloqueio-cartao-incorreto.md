---
id: RISK-008
card_type: risk
title: Bloqueio do cartão incorreto
status: draft
risk_level: R3
likelihood: possible
impact: critical
governs:
  - "PB-012"
  - "WF-004"
  - "TOOL-007"
tested_by:
  - "TEST-034"
owner: Riscos e controles
---

# RISK-008 — Bloqueio do cartão incorreto

## Evento de risco obrigatório

O agente ou sistema bloqueia um cartão diferente daquele que o cliente pretendia proteger.

## Causas possíveis

- Inferência incorreta quando há múltiplos cartões.
- Uso de contexto desatualizado em [VAR-021-active-cards](VAR-021-active-cards.md).
- Confirmação ambígua ou ausente.
- Mapeamento incorreto entre rótulo mascarado e `selected_card_id`.
- Repetição ou concorrência de chamadas.

## Controles obrigatórios

- Seleção explícita quando houver mais de um cartão elegível.
- Apresentação apenas de identificadores mascarados e distinguíveis.
- Confirmação explícita imediatamente antes da ação.
- Vinculação entre confirmação, `selected_card_id` e `correlation_id`.
- Uso obrigatório de `idempotency_key`.
- Teste de múltiplos cartões com [TEST-034-multiplos-cartoes](TEST-034-multiplos-cartoes.md).

## Evidências de controle

- Evento [EVT-002-cartao-selecionado](EVT-002-cartao-selecionado.md).
- Registro da confirmação do cliente.
- Log da chamada a [TOOL-007-api-bloqueio](TOOL-007-api-bloqueio.md).
- Protocolo de [EVT-003-bloqueio-confirmado](EVT-003-bloqueio-confirmado.md).

## Variáveis selecionáveis

| Campo | Valores predefinidos |
|---|---|
| `likelihood` | `rare`, `unlikely`, `possible`, `likely`, `almost_certain` |
| `impact` | `low`, `moderate`, `high`, `critical` |
| `treatment` | `avoid`, `mitigate`, `transfer`, `accept` |
| `control_type` | `preventive`, `detective`, `corrective` |
| `control_status` | `planned`, `implemented`, `verified`, `ineffective` |

