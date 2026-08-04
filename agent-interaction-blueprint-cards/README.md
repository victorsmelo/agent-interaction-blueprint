# Agent Interaction Blueprint — pacote de cartões

Conjunto de notas interligadas para o exemplo **Cartão perdido**, derivado de `agent-interaction-blueprint-campos.md`.

## Como usar

1. Copie a pasta para um vault do Obsidian ou abra os arquivos em qualquer editor Markdown.
2. Mantenha o ID e o nome do arquivo estáveis; altere o título legível por meio do alias após `|` no wikilink.
3. Use as propriedades em `relations` como fonte dos relacionamentos.
4. Use o Graph View ou um board apenas como visualização contextual.
5. Substitua valores `A definir` antes de aprovar a implementação.

## Convenção

- Ação: verbo no infinitivo, como `Bloquear cartão`.
- Evento: fato no passado, como `Bloqueio confirmado`.
- Relação: verbo explícito, como `triggered_by`, `emits`, `on_success` ou `tested_by`.
- ID: permanece estável mesmo que o título seja refinado.

## Índice

| Tipo | Nota |
|---|---|
| Playbook | [[PB-012-entender-ocorrencia|Entender ocorrência]] |
| Evento | [[EVT-001-perda-reportada|Perda reportada]] |
| Evento | [[EVT-002-cartao-selecionado|Cartão selecionado]] |
| Workflow | [[WF-004-bloquear-cartao|Bloquear cartão]] |
| Tool | [[TOOL-007-api-bloqueio|API de bloqueio]] |
| Evento | [[EVT-003-bloqueio-confirmado|Bloqueio confirmado]] |
| Evento | [[EVT-004-bloqueio-nao-confirmado|Bloqueio não confirmado]] |
| Evento | [[EVT-005-timeout-bloqueio|Timeout ocorrido]] |
| Conhecimento | [[KB-003-politica-cartoes|Política de cartões]] |
| Variável | [[VAR-001-is-authenticated|Cliente autenticado]] |
| Variável | [[VAR-021-active-cards|Cartões ativos]] |
| Risco | [[RISK-008-bloqueio-cartao-incorreto|Bloqueio do cartão incorreto]] |
| Handoff | [[HO-003-cartoes-fraude|Cartões e Fraude]] |
| Teste | [[TEST-034-multiplos-cartoes|Cliente com múltiplos cartões]] |
| Avaliação | [[EVAL-006-resolucao-segura|Resolução segura]] |
| Alias | [[EVAL-006-resolucao|Resolução]] |
| Métrica | [[METRIC-011-tempo-protecao|Tempo até proteção]] |

## Cadeia principal

[[EVT-001-perda-reportada|Perda reportada]] → [[PB-012-entender-ocorrencia|Entender ocorrência]] → [[EVT-002-cartao-selecionado|Cartão selecionado]] → [[WF-004-bloquear-cartao|Bloquear cartão]] → [[TOOL-007-api-bloqueio|API de bloqueio]]

- Sucesso: [[EVT-003-bloqueio-confirmado|Bloqueio confirmado]].
- Erro: [[EVT-004-bloqueio-nao-confirmado|Bloqueio não confirmado]].
- Timeout: [[EVT-005-timeout-bloqueio|Timeout ocorrido]].
- Contingência: [[HO-003-cartoes-fraude|Cartões e Fraude]].

> `EVAL-006-resolucao.md` é uma nota de compatibilidade. A nota canônica é `EVAL-006-resolucao-segura.md`.

