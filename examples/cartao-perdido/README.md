# Exemplo — cartão perdido

Este cenário ilustra uma interação de risco R2/R3: o agente entende a ocorrência, coleta a seleção explícita do cartão e executa o bloqueio somente após confirmação.

## Índice navegável

| Tipo | Cartão |
|---|---|
| Playbook | [PB-012 — Entender ocorrência](cards/PB-012-entender-ocorrencia.md) |
| Workflow | [WF-004 — Bloquear cartão](cards/WF-004-bloquear-cartao.md) |
| Ferramenta | [TOOL-007 — API de bloqueio](cards/TOOL-007-api-bloqueio.md) |
| Eventos | [EVT-001](cards/EVT-001-perda-reportada.md), [EVT-002](cards/EVT-002-cartao-selecionado.md), [EVT-003](cards/EVT-003-bloqueio-confirmado.md), [EVT-004](cards/EVT-004-bloqueio-nao-confirmado.md), [EVT-005](cards/EVT-005-timeout-bloqueio.md) |
| Governança | [RISK-008](cards/RISK-008-bloqueio-cartao-incorreto.md), [HO-003](cards/HO-003-cartoes-fraude.md) |
| Qualidade | [TEST-034](cards/TEST-034-multiplos-cartoes.md), [EVAL-006](cards/EVAL-006-resolucao-segura.md), [METRIC-011](cards/METRIC-011-tempo-protecao.md) |

## Fluxo principal

1. [[EVT-001-perda-reportada|Perda reportada]] torna [[PB-012-entender-ocorrencia|Entender ocorrência]] elegível.
2. O playbook identifica o cartão e emite [[EVT-002-cartao-selecionado|Cartão selecionado]].
3. [[WF-004-bloquear-cartao|Bloquear cartão]] chama [[TOOL-007-api-bloqueio|API de bloqueio]].
4. O resultado é [[EVT-003-bloqueio-confirmado|confirmado]] ou tratado com [[HO-003-cartoes-fraude|handoff seguro]].

