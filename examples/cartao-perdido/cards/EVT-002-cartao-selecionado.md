---
id: EVT-002
card_type: event
title: Cartão selecionado
status: validating
owner: Produtos Cartões
emitted_by: ["PB-012"]
caused_by: ["EVT-001"]
consumed_by: ["WF-004"]
payload: [selected_card_id, incident_type, customer_confirmation, correlation_id]
correlation_key: correlation_id
---

# EVT-002 — Cartão selecionado

## Definição

Registra que o cliente escolheu explicitamente um cartão elegível e que o workflow de bloqueio pode iniciar.

## Pré-condições

- [Cliente autenticado](VAR-001-is-authenticated.md) com nível forte.
- [Cartões ativos](VAR-021-active-cards.md) carregados.
- `selected_card_id` corresponde a uma opção apresentada ao cliente.

## Estado posterior

- `selected_card_id`: preenchido.
- `customer_confirmation`: `false` até a confirmação imediatamente anterior à ação.
- Próximo consumidor: [Bloquear cartão](WF-004-bloquear-cartao.md).

