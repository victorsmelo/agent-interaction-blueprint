---
id: VAR-001
card_type: variable
title: Cliente autenticado
variable_name: is_authenticated
status: approved
owner: Plataforma de Identidade
data_type: boolean
default: false
source: sessão autenticada
required_at: antes de consultar ou alterar cartões
data_classification: authentication
persistence: session
masking: não exibir
allowed_consumers:
  - "PB-012"
  - "WF-004"
---

# VAR-001 — Cliente autenticado

## Definição

Indica que a identidade do cliente foi validada para a sessão atual.

## Valores

- `false`: identidade ausente, expirada ou insuficiente.
- `true`: autenticação válida; o nível ainda deve ser verificado para ações sensíveis.

## Ausência ou valor inválido

Tratar como `false`. Não listar cartões nem expor dados financeiros.

