---
id: EVT-002
card_type: event
title: Cartão selecionado
status: validating
owner: Produtos Cartões
emitted_by: ["[[PB-012-entender-ocorrencia|Entender ocorrência]]"]
caused_by: ["[[EVT-001-perda-reportada|Perda reportada]]"]
consumed_by: ["[[WF-004-bloquear-cartao|Bloquear cartão]]"]
payload: [selected_card_id, incident_type, customer_confirmation, correlation_id]
correlation_key: correlation_id
---

# EVT-002 — Cartão selecionado

## Definição

Registra que o cliente escolheu explicitamente um cartão elegível e que o workflow de bloqueio pode iniciar.

## Pré-condições

- [[VAR-001-is-authenticated|Cliente autenticado]] com nível forte.
- [[VAR-021-active-cards|Cartões ativos]] carregados.
- `selected_card_id` corresponde a uma opção apresentada ao cliente.

## Estado posterior

- `selected_card_id`: preenchido.
- `customer_confirmation`: `false` até a confirmação imediatamente anterior à ação.
- Próximo consumidor: [[WF-004-bloquear-cartao|Bloquear cartão]].

