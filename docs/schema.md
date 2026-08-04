# Schema do blueprint

## Campos-base obrigatórios

Todos os cartões canônicos precisam declarar no frontmatter:

| Campo | Regra |
|---|---|
| `id` | Único, estável e com prefixo do tipo, por exemplo `WF-004` |
| `card_type` | Tipo listado abaixo |
| `title` | Nome legível e orientado à finalidade |
| `status` | `draft`, `validating`, `approved` ou `deprecated` |
| `owner` | Área ou pessoa responsável |

`alias` é o único tipo sem `id` e sem `owner`; ele deve declarar `alias_of`.

## Tipos de cartão

`playbook`, `workflow`, `event`, `tool`, `knowledge`, `variable`, `risk`, `handoff`, `test`, `evaluation`, `metric` e `alias`.

## Modelo de relações

As relações ficam como propriedades YAML de primeiro nível, sempre com nomes de verbo explícitos. Seus valores podem ser um wikilink ou uma lista de wikilinks.

Exemplos: `triggered_by`, `emits`, `uses`, `reads`, `routes_to`, `consumed_by`, `governed_by`, `tested_by`, `evaluated_by` e `measured_by`.

Não use uma propriedade genérica `relations`: ela dificulta validação, consultas e consistência entre tipos.

## Regras por tipo

| Tipo | Campos adicionais mínimos |
|---|---|
| `event` | `emitted_by`, `consumed_by`, `payload`, `correlation_key` |
| `variable` | `variable_name`, `data_type`, `data_classification`, `persistence` |
| `tool` | `system` e política de resultados/erros no corpo |
| `risk` | `risk_level`, `likelihood`, `impact` |
| `metric` | `metric_type`, `unit`, `starts_at`, `ends_at` |
| `handoff` | `destination`, `triggered_by` |

## Dados e eventos

- Eventos devem declarar payload no frontmatter e explicá-lo no corpo.
- Toda cadeia assíncrona deve carregar `correlation_id` ou equivalente.
- Operações com efeito devem declarar `idempotency_key` e o comportamento de timeout.
- Dados classificados como `confidential` ou `restricted` não devem aparecer sem mascaramento no conteúdo conversacional.

