---
id: EVT-001
card_type: event
title: Perda reportada
status: approved
owner: Canais de Atendimento
emitted_by: [Canal de atendimento]
caused_by: [Mensagem inicial do cliente]
consumed_by: ["PB-012"]
payload: [conversation_id, correlation_id, channel, locale, last_user_utterance]
correlation_key: correlation_id
---

# EVT-001 — Perda reportada

## Definição

Evento inicial produzido quando o cliente relata perda, roubo ou ausência de posse do cartão.

## Condição de emissão

- A mensagem contém sinal suficiente de perda ou roubo; ou
- O cliente seleciona uma opção equivalente na interface.

## Estado anterior

Nenhum cenário de cartões está ativo.

## Estado posterior

O playbook [Entender ocorrência](PB-012-entender-ocorrencia.md) torna-se elegível.

## Regras

- Não incluir número completo de cartão no payload.
- Preservar a mensagem original somente conforme a política de transcrições e redação de dados.

