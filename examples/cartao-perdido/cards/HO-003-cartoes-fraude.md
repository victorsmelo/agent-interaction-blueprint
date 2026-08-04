---
id: HO-003
card_type: handoff
title: Cartões e fraude
status: draft
destination: Fila especializada de cartões e fraude
triggered_by:
  - "EVT-004"
  - "EVT-005"
related_workflow:
  - "WF-004"
owner: Atendimento especializado
---

# HO-003 — Cartões e fraude

## Objetivo obrigatório

Transferir o cliente com contexto suficiente quando o agente não puder concluir a proteção de forma segura.

## Motivos de transferência predefinidos

- `tool_failure` — falha confirmada da ferramenta.
- `status_unknown` — timeout ou resultado inconclusivo.
- `authentication_failure` — não foi possível autenticar com segurança.
- `fraud_signal` — indício de fraude ou transação não reconhecida.
- `customer_vulnerability` — coerção, vulnerabilidade ou urgência crítica.
- `customer_request` — cliente pediu atendimento humano.

## Pacote de contexto obrigatório

- Resumo objetivo da solicitação.
- `correlation_id` e motivo de transferência.
- Autenticação realizada ou pendente.
- Cartão selecionado, sempre mascarado.
- Tipo de ocorrência e nível de urgência.
- Tentativas e resultados das ferramentas.
- Último estado conhecido do bloqueio.
- Próxima ação recomendada.

## Experiência do cliente

- Informar por que a transferência é necessária.
- Informar fila, disponibilidade e estimativa quando conhecidas.
- Não pedir que o cliente repita dados já coletados, salvo necessidade de segurança.
- Definir alternativa se a fila estiver indisponível.

## Variáveis selecionáveis

| Campo | Valores predefinidos |
|---|---|
| `handoff_mode` | `live_transfer`, `callback`, `ticket`, `emergency_channel` |
| `priority` | `normal`, `high`, `urgent`, `critical` |
| `availability` | `open`, `closed`, `degraded`, `unknown` |
| `return_path` | `human_closes`, `returns_to_agent`, `async_notification` |
| `summary_format` | `structured`, `narrative`, `both` |

