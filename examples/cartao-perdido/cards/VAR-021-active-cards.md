---
id: VAR-021
card_type: variable
title: Cartões ativos
variable_name: active_cards
status: validating
owner: Plataforma de Cartões
data_type: array
default: []
source: API de cartões
required_at: antes da seleção do cartão
data_classification: financial
persistence: session
masking: marca, tipo e quatro últimos dígitos
allowed_consumers:
  - "PB-012"
  - "WF-004"
---

# VAR-021 — Cartões ativos

## Estrutura mínima

```yaml
- card_id: identificador-interno
  display_name: Cartão Visa final 1234
  product_type: credit
  eligible_for_block: true
```

## Regras

- Nunca armazenar ou exibir o número completo.
- Remover cartões inelegíveis antes de apresentar opções.
- Se a lista estiver vazia ou indisponível, não permitir seleção manual de identificador.

