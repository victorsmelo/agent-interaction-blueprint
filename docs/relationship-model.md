# Modelo de relações

O blueprint representa um grafo dirigido: cada relação registra o papel de origem, o alvo e o significado do vínculo. Nem toda relação precisa aparecer nos dois cartões; o backlink é derivado pelo grafo, não mantido manualmente.

## Convenções

| Relação | Origem → destino |
|---|---|
| `triggered_by` | capacidade → evento ou condição que a ativa |
| `emits` | capacidade → evento produzido |
| `uses` | workflow/playbook → ferramenta |
| `reads` | capacidade → variável |
| `queries_kb` | capacidade → conhecimento |
| `routes_to` / `escalates_to` | capacidade → workflow ou handoff |
| `consumed_by` | evento → consumidor |
| `governed_by` | capacidade/ferramenta → risco ou controle |
| `tested_by` / `evaluated_by` / `measured_by` | capacidade → qualidade ou métrica |

## Wikilinks e GitHub

- `[[ID-arquivo|Rótulo]]` é a referência canônica e permite Graph View no Obsidian.
- Índices README usam links Markdown relativos para permanecerem navegáveis no GitHub.
- Não substitua IDs no nome do arquivo; atualize apenas o rótulo depois de `|` quando o título mudar.

## Cadeias de eventos

Cada evento deve trazer `correlation_key`. Para efeitos sensíveis, a ferramenta recebe e propaga `correlation_id` e `idempotency_key`; sucesso, erro e timeout tornam-se eventos distintos, evitando declarar um resultado que não foi confirmado.

