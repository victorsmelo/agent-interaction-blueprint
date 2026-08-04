# Agent Interaction Blueprint — campos para mapeamento

Template para mapear interações de chatbots e AI agents em atendimento a clientes. Pode ser usado como roteiro de workshop, estrutura de cards no FigJam ou base para especificação funcional.

## Legenda de preenchimento

- **[OBRIGATÓRIO]**: necessário para que o cenário possa ser compreendido, avaliado e implementado com segurança.
- **[CONDICIONAL]**: obrigatório quando o cenário envolver aquele elemento, como uma API, dado pessoal ou handoff humano.
- **[OPCIONAL]**: enriquece o mapeamento, mas pode ser adicionado posteriormente.

> Regra prática: se um campo obrigatório ainda não puder ser respondido, registre `A definir`, o responsável pela decisão e a data esperada. Não deixe o campo silenciosamente em branco.

---

# Bloco 1 — Template para preenchimento

## Catálogos predefinidos para seleção

Use estes valores como chips, dropdowns, propriedades ou stamps no FigJam. O objetivo é reduzir variações de nomenclatura e permitir filtros, automações e análises posteriores. Inclua `outro` somente quando houver owner responsável por revisar e incorporar novos valores ao catálogo.

| Campo selecionável | Valores predefinidos recomendados |
|---|---|
| `card_type` | `agent`, `event`, `playbook`, `workflow`, `tool`, `knowledge`, `variable`, `risk`, `handoff`, `test`, `evaluation`, `metric`, `decision`, `outcome` |
| `status` | `discovery`, `designing`, `validating`, `approved`, `implemented`, `monitoring`, `paused`, `deprecated` |
| `treatment_type` | `informational`, `agentic`, `deterministic`, `hybrid`, `direct_handoff`, `decline` |
| `risk_level` | `R0-informational`, `R1-assisted`, `R2-sensitive`, `R3-critical` |
| `channel` | `mobile_app`, `web`, `whatsapp`, `chat`, `voice`, `phone`, `ivr`, `internal_assistant`, `api` |
| `actor` | `customer`, `agent`, `system`, `human_agent`, `external_service` |
| `relationship_type` | `triggered_by`, `triggers`, `routes_to`, `emits`, `on_success`, `on_error`, `on_timeout`, `on_cancel`, `requires`, `uses_tool`, `queries_kb`, `reads`, `writes`, `governs`, `governed_by`, `blocked_by`, `escalates_to`, `returns_to`, `tested_by`, `evaluated_by`, `measured_by`, `caused_by`, `observed_in`, `correlates`, `prevents_duplicate`, `improves`, `replaces` |
| `outcome` | `resolved`, `successful_handoff`, `unresolved`, `abandoned`, `unrelated`, `cancelled`, `blocked_for_safety` |
| `severity` | `low`, `medium`, `high`, `blocking` |
| `data_classification` | `public`, `internal`, `confidential`, `personal`, `sensitive_personal`, `financial`, `authentication`, `secret` |
| `persistence` | `turn`, `session`, `cross_session`, `permanent_record`, `not_persisted` |
| `action_effect` | `read_only`, `reversible_change`, `irreversible_change`, `financial_transaction`, `external_communication` |
| `test_type` | `happy_path`, `ambiguity`, `edge_case`, `tool_failure`, `safety`, `privacy`, `accessibility`, `handoff`, `regression` |
| `evaluation_type` | `binary`, `rating`, `categories`, `text` |
| `handoff_reason` | `out_of_scope`, `customer_request`, `low_confidence`, `authentication_failure`, `tool_failure`, `policy_requirement`, `fraud_or_abuse`, `vulnerability`, `human_judgment` |
| `accessibility_need` | `screen_reader`, `keyboard_only`, `voice_alternative`, `simple_language`, `additional_time`, `reduced_cognitive_load`, `captions_or_transcript` |

### Convenção de IDs

| Prefixo | Tipo de cartão | Exemplo |
|---|---|---|
| `AGT` | Agente | `AGT-001` |
| `EVT` | Evento | `EVT-001` |
| `PB` | Playbook | `PB-012` |
| `WF` | Workflow | `WF-004` |
| `STEP` | Etapa determinística | `STEP-018` |
| `TOOL` | Ferramenta, API ou MCP | `TOOL-007` |
| `KB` | Conhecimento | `KB-003` |
| `VAR` | Variável | `VAR-021` |
| `RISK` | Risco ou guardrail | `RISK-008` |
| `HO` | Handoff | `HO-003` |
| `TEST` | Teste | `TEST-034` |
| `EVAL` | Avaliação | `EVAL-006` |
| `METRIC` | Métrica | `METRIC-011` |
| `DEC` | Decisão | `DEC-005` |
| `OUT` | Resultado | `OUT-002` |

O ID é estável. O título pode mudar sem quebrar referências. Para wikilinks, prefira `[[PB-012-entender-ocorrencia|Entender ocorrência]]`: o primeiro valor é o destino estável; o texto após `|` é o rótulo legível.

## Biblioteca de variáveis predefinidas

Estas variáveis formam um catálogo inicial. Elas podem ser selecionadas nos cards sem que cada equipe recrie nomes e definições. Isso **não significa que todas estarão automaticamente disponíveis em runtime**: a origem real, a autorização e a persistência precisam ser confirmadas na implementação.

| Grupo | Variável | Tipo sugerido | Uso principal | Default sugerido |
|---|---|---|---|---|
| Identidade | `user_id` | `string` | Identificador técnico do usuário | `null` |
| Identidade | `customer_id` | `string` | Identificador do cliente no domínio | `null` |
| Identidade | `is_authenticated` | `boolean` | Indica autenticação válida | `false` |
| Identidade | `authentication_level` | `enum` | `none`, `basic`, `strong` | `none` |
| Sessão | `session_id` | `string` | Identifica a sessão atual | gerado no início |
| Sessão | `conversation_id` | `string` | Identifica a conversa ou transcrição | gerado no início |
| Sessão | `correlation_id` | `string` | Agrupa eventos da mesma jornada | gerado no início |
| Sessão | `channel` | `enum` | Canal atual | detectado |
| Sessão | `locale` | `string` | Idioma e região | detectado ou padrão |
| Sessão | `timezone` | `string` | Interpretação de datas e horários | detectado ou padrão |
| Sessão | `current_datetime` | `datetime` | Data e hora de referência | gerado pelo sistema |
| Conversa | `current_intent` | `string` | Intenção atualmente reconhecida | `null` |
| Conversa | `previous_intent` | `string` | Intenção anterior para retomada | `null` |
| Conversa | `last_user_utterance` | `string` | Última mensagem do cliente | `null` |
| Conversa | `last_agent_response` | `string` | Última resposta do agente | `null` |
| Conversa | `sentiment` | `enum` | `positive`, `neutral`, `frustrated`, `distressed`, `unknown` | `unknown` |
| Conversa | `urgency_level` | `enum` | `normal`, `urgent`, `emergency` | `normal` |
| Conversa | `risk_level` | `enum` | R0, R1, R2 ou R3 | definido pelo cenário |
| Orquestração | `active_playbook_id` | `string` | Playbook em execução | `null` |
| Orquestração | `active_workflow_id` | `string` | Workflow em execução | `null` |
| Orquestração | `current_step_id` | `string` | Etapa determinística atual | `null` |
| Orquestração | `route_confidence` | `number` | Confiança do roteamento, quando aplicável | `null` |
| Produto | `customer_segment` | `enum` | Segmentação aplicável | `unknown` |
| Produto | `product_context` | `string` | Produto ou domínio atual | `null` |
| Ação | `selected_item_id` | `string` | Item selecionado pelo cliente | `null` |
| Ação | `customer_confirmation` | `boolean` | Confirmação explícita para uma ação | `false` |
| Ação | `idempotency_key` | `string` | Evita execução duplicada | gerado antes da ação |
| Ação | `tool_status` | `enum` | `not_called`, `pending`, `success`, `error`, `timeout`, `unknown` | `not_called` |
| Ação | `error_code` | `string` | Código normalizado de erro | `null` |
| Ação | `retry_count` | `integer` | Número de tentativas | `0` |
| Ação | `protocol_id` | `string` | Evidência ou protocolo gerado | `null` |
| Handoff | `handoff_required` | `boolean` | Indica necessidade de atendimento humano | `false` |
| Handoff | `handoff_reason` | `enum` | Motivo padronizado do handoff | `null` |
| Handoff | `handoff_queue` | `string` | Fila ou especialidade de destino | `null` |
| Handoff | `handoff_status` | `enum` | `not_started`, `queued`, `connected`, `failed`, `completed` | `not_started` |
| Resultado | `resolution_outcome` | `enum` | Resultado final padronizado | `null` |
| Resultado | `started_at` | `datetime` | Início da jornada ou ação | gerado ao iniciar |
| Resultado | `completed_at` | `datetime` | Conclusão da jornada ou ação | `null` |
| Resultado | `latency_ms` | `integer` | Latência total ou de ferramenta | `null` |

Para cada variável selecionada, ainda devem ser definidos: `source`, `required_at`, `data_classification`, `persistence`, `masking`, `retention`, `allowed_consumers` e comportamento quando ausente.

## 0. Identificação do artefato

| Campo | Prioridade | O que registrar |
|---|---|---|
| ID do agente ou iniciativa | **[OBRIGATÓRIO]** | Identificador único e estável. Ex.: `AGT-CARTOES-01`. |
| Nome | **[OBRIGATÓRIO]** | Nome claro da iniciativa ou agente. |
| Objetivo do documento | **[OBRIGATÓRIO]** | Decisão, workshop ou implementação que este mapeamento deve apoiar. |
| Owner principal | **[OBRIGATÓRIO]** | Pessoa ou área responsável pela evolução do agente. |
| Áreas participantes | **[OBRIGATÓRIO]** | Negócio, atendimento, design, conteúdo, tecnologia, dados, segurança, jurídico, acessibilidade etc. |
| Status | **[OBRIGATÓRIO]** | Descoberta, em desenho, em validação, aprovado, implementado, monitorado ou descontinuado. |
| Versão e data | **[OBRIGATÓRIO]** | Versão atual e data da última alteração. |
| Links relacionados | [OPCIONAL] | Figma, FigJam, backlog, documentação, protótipo, analytics ou repositório. |

## 1. Brief do agente

| Campo | Prioridade | O que registrar |
|---|---|---|
| Problema do cliente | **[OBRIGATÓRIO]** | Necessidade ou dificuldade que justifica o agente. |
| Público-alvo | **[OBRIGATÓRIO]** | Quem será atendido e quais segmentos merecem tratamento específico. |
| Canais | **[OBRIGATÓRIO]** | App, web, WhatsApp, voz, telefone, assistente interno etc. |
| Produtos ou domínios | **[OBRIGATÓRIO]** | Produtos, serviços e temas cobertos. |
| Escopo | **[OBRIGATÓRIO]** | O que o agente pode informar, orientar, executar ou encaminhar. |
| Fora de escopo | **[OBRIGATÓRIO]** | O que o agente não deve tratar ou executar. |
| Resultado primário | **[OBRIGATÓRIO]** | Mudança observável que representa valor para o cliente. |
| Valor para o negócio | **[OBRIGATÓRIO]** | Benefício esperado: resolução, eficiência, prevenção de perdas, satisfação etc. |
| Restrições conhecidas | [CONDICIONAL] | Limitações técnicas, legais, operacionais ou de canal. |
| Hipóteses | [OPCIONAL] | Suposições que ainda precisam ser validadas. |

## 2. Agent Charter

| Campo | Prioridade | O que registrar |
|---|---|---|
| Papel do agente | **[OBRIGATÓRIO]** | Quem o agente representa e qual responsabilidade assume. |
| Objetivo global | **[OBRIGATÓRIO]** | Resultado que orienta o comportamento em situações ambíguas. |
| Tom e estilo | **[OBRIGATÓRIO]** | Formalidade, concisão, empatia, vocabulário e adaptação ao contexto. |
| Princípios de comportamento | **[OBRIGATÓRIO]** | Regras positivas que devem aparecer em todas as interações. |
| Guardrails globais | **[OBRIGATÓRIO]** | Limites não negociáveis: não inventar, não revelar dados, não executar sem confirmação etc. |
| Política de incerteza | **[OBRIGATÓRIO]** | O que fazer quando informação, intenção ou retorno de sistema for insuficiente. |
| Política de adaptação | [OPCIONAL] | Como adaptar linguagem, profundidade e ritmo ao cliente e ao canal. |

## 3. Cliente, persona e contexto inicial

| Campo | Prioridade | O que registrar |
|---|---|---|
| Persona ou segmento | **[OBRIGATÓRIO]** | Tipo de cliente relevante para o cenário. |
| Job ou objetivo do cliente | **[OBRIGATÓRIO]** | O que o cliente está tentando conseguir. |
| Estado inicial | **[OBRIGATÓRIO]** | Autenticação, produto contratado, etapa da jornada e outras condições iniciais. |
| Estado emocional ou urgência | [CONDICIONAL] | Frustração, ansiedade, risco, emergência ou vulnerabilidade. |
| Necessidades de acessibilidade | [CONDICIONAL] | Leitor de tela, linguagem simples, tempo adicional, alternativa ao áudio etc. |
| Histórico relevante | [OPCIONAL] | Contatos anteriores, tentativas, preferências ou eventos recentes. |
| Locale e idioma | [CONDICIONAL] | Idioma, região, timezone e regras locais. |

## 4. Cenário ou Playbook Canvas

> Repita este bloco para cada intenção ou objetivo relevante do cliente.

| Campo | Prioridade | O que registrar |
|---|---|---|
| ID e nome do cenário | **[OBRIGATÓRIO]** | Nome literal e identificador único. Ex.: `CRT-012 — Bloquear cartão perdido`. |
| Tipo de tratamento | **[OBRIGATÓRIO]** | Informativo, playbook agentivo, workflow determinístico, híbrido ou handoff direto. |
| Problema ou job | **[OBRIGATÓRIO]** | Necessidade específica atendida pelo cenário. |
| Exemplos de triggers | **[OBRIGATÓRIO]** | Diferentes formas de o cliente expressar a intenção. |
| Quando usar | **[OBRIGATÓRIO]** | Condições que tornam este cenário apropriado. |
| Quando não usar | **[OBRIGATÓRIO]** | Intenções semelhantes que devem seguir outro caminho. |
| Resultado esperado | **[OBRIGATÓRIO]** | Resultado observável para o cliente. |
| Critérios de sucesso | **[OBRIGATÓRIO]** | Evidências que confirmam a conclusão correta. |
| Nível de risco | **[OBRIGATÓRIO]** | `R0 — Informativo`, `R1 — Assistido`, `R2 — Sensível` ou `R3 — Crítico`. |
| Pré-condições | **[OBRIGATÓRIO]** | Condições que devem ser verdadeiras antes de iniciar. Use `Nenhuma` quando não houver. |
| Variáveis obrigatórias | [CONDICIONAL] | Dados que precisam existir antes ou durante a execução. |
| Conhecimento necessário | [CONDICIONAL] | Fontes usadas para responder ou orientar. |
| Ferramentas permitidas | [CONDICIONAL] | APIs, funções, integrações ou MCPs disponíveis. |
| Ações proibidas | **[OBRIGATÓRIO]** | O que o agente nunca pode fazer neste cenário. |
| Condições de saída | **[OBRIGATÓRIO]** | Resolvido, encaminhado, cancelado, abandonado, fora de escopo etc. |
| Motivos de handoff | **[OBRIGATÓRIO]** | Situações que exigem atendimento humano. Use `Não aplicável` somente com justificativa. |
| Owner do cenário | **[OBRIGATÓRIO]** | Responsável pela regra de negócio e manutenção. |

## 5. Relacionamentos e cadeia de eventos

Os wikilinks identificam os cartões; o nome da propriedade informa o significado da relação. Toda conexão de execução deve ter um verbo. Evite usar apenas `related_to`.

### 5.1 Relações do cartão

| Campo | Prioridade | O que registrar |
|---|---|---|
| `triggered_by` | **[OBRIGATÓRIO]** para playbook, workflow e tool | Evento ou condição que inicia o cartão. |
| `triggers` | [CONDICIONAL] | Cartão iniciado diretamente por este elemento. |
| `routes_to` | [CONDICIONAL] | Destino selecionado por uma decisão de roteamento. |
| `emits` | [CONDICIONAL] | Eventos produzidos quando algo relevante acontece. |
| `on_success` | **[OBRIGATÓRIO]** para elementos executáveis | Próximo evento ou cartão após sucesso. |
| `on_error` | **[OBRIGATÓRIO]** para elementos executáveis | Próximo evento ou cartão após falha. |
| `on_timeout` | [CONDICIONAL] | Próximo evento ou cartão quando não houver resposta no prazo. |
| `on_cancel` | [CONDICIONAL] | Destino quando o cliente ou sistema cancelar. |
| `requires` | [CONDICIONAL] | Pré-condições, permissões ou elementos obrigatórios. |
| `uses_tool` | [CONDICIONAL] | APIs, integrações, funções ou MCPs utilizados. |
| `queries_kb` | [CONDICIONAL] | Fontes de conhecimento consultadas. |
| `reads` | [CONDICIONAL] | Variáveis lidas. |
| `writes` | [CONDICIONAL] | Variáveis criadas ou atualizadas. |
| `governed_by` | **[OBRIGATÓRIO]** em R2 e R3 | Riscos, guardrails, políticas ou decisões que governam o cartão. |
| `escalates_to` | [CONDICIONAL] | Handoff acionado pelo cartão. |
| `tested_by` | **[OBRIGATÓRIO]** antes da implementação | Testes que verificam o comportamento. |
| `evaluated_by` | **[OBRIGATÓRIO]** em produção | Avaliações aplicadas às conversas. |
| `measured_by` | **[OBRIGATÓRIO]** em produção | Métricas associadas. |
| `correlates` | [CONDICIONAL] | Eventos agrupados pela mesma `correlation_key`. |
| `prevents_duplicate` | [CONDICIONAL] | Ação protegida por uma `idempotency_key`. |
| `improves` | [CONDICIONAL] | Elemento alterado a partir de uma avaliação ou aprendizagem. |
| `replaces` | [CONDICIONAL] | Cartão ou versão substituída. |

### 5.2 Cartão de evento

Um evento descreve algo que aconteceu e deve ser nomeado no passado: `Cartão selecionado`, `Bloqueio confirmado`, `Timeout ocorrido`. A ação correspondente usa verbo no infinitivo: `Selecionar cartão`, `Bloquear cartão`, `Consultar status`.

| Campo | Prioridade | O que registrar |
|---|---|---|
| ID e nome do evento | **[OBRIGATÓRIO]** | Ex.: `EVT-003 — Bloqueio confirmado`. |
| `emitted_by` | **[OBRIGATÓRIO]** | Cartão, sistema ou ferramenta que produziu o evento. |
| `caused_by` | **[OBRIGATÓRIO]** | Evento ou ação anterior que causou este evento. Use `Evento inicial` quando aplicável. |
| `consumed_by` | **[OBRIGATÓRIO]** | Playbooks, workflows, avaliações ou sistemas que reagem ao evento. |
| `payload` | **[OBRIGATÓRIO]** | Dados carregados pelo evento ou `Nenhum`. |
| Estado anterior | [CONDICIONAL] | Situação antes do evento. |
| Estado posterior | [CONDICIONAL] | Situação produzida pelo evento. |
| `correlation_key` | [CONDICIONAL] | Identificador usado para agrupar eventos da mesma jornada. |
| `idempotency_key` | [CONDICIONAL] | Identificador usado para impedir execução duplicada. |
| Retenção e auditoria | [CONDICIONAL] | Registro, prazo e acesso ao evento. |
| Owner | **[OBRIGATÓRIO]** | Domínio responsável pela definição do evento. |

### 5.3 Modelo de propriedades e wikilinks

```yaml
---
id: PB-012
card_type: playbook
title: Entender ocorrência de cartão
status: validating
owner: Produtos Cartões

relations:
  triggered_by:
    - "[[EVT-001-perda-reportada|Perda reportada]]"
  emits:
    - "[[EVT-002-cartao-selecionado|Cartão selecionado]]"
  queries_kb:
    - "[[KB-003-politica-cartoes|Política de cartões]]"
  reads:
    - "[[VAR-001-is-authenticated|Cliente autenticado]]"
    - "[[VAR-021-active-cards|Cartões ativos]]"
  routes_to:
    - "[[WF-004-bloquear-cartao|Bloquear cartão]]"
  escalates_to:
    - "[[HO-003-cartoes-fraude|Cartões e Fraude]]"
  tested_by:
    - "[[TEST-034-multiplos-cartoes|Cliente com múltiplos cartões]]"
  evaluated_by:
    - "[[EVAL-006-resolucao|Resolução]]"
  measured_by:
    - "[[METRIC-011-tempo-protecao|Tempo até proteção]]"
---
```

No FigJam, mantenha os links tipados dentro do cartão como fonte da relação. Use conectores visuais apenas nas perspectivas em que a relação ajuda: cadeia principal, erros, dados, ferramentas, riscos ou qualidade.

## 6. Regras de roteamento

| Campo | Prioridade | O que registrar |
|---|---|---|
| Mensagem ou evento de entrada | **[OBRIGATÓRIO]** | O que dispara a decisão de roteamento. |
| Sinais considerados | **[OBRIGATÓRIO]** | Intenção, autenticação, produto, urgência, sentimento, risco, canal e contexto. |
| Destino | **[OBRIGATÓRIO]** | Playbook, workflow, base de conhecimento, ferramenta, humano ou recusa. |
| Regra de seleção | **[OBRIGATÓRIO]** | Explicação clara de quando escolher o destino. |
| Prioridade ou precedência | [CONDICIONAL] | Qual regra vence quando mais de uma rota for possível. |
| Confiança mínima | [CONDICIONAL] | Limite ou condição para agir sem pedir esclarecimento. |
| Desambiguação | **[OBRIGATÓRIO]** | Pergunta ou estratégia quando houver mais de uma interpretação. |
| Fallback | **[OBRIGATÓRIO]** | Comportamento quando nenhuma rota segura for encontrada. |

## 7. Mapa da interação

> Use um item por momento relevante da conversa. Em trechos agentivos, mapeie responsabilidades e decisões; não tente antecipar todas as frases possíveis.

| Campo | Prioridade | O que registrar |
|---|---|---|
| ID do momento | **[OBRIGATÓRIO]** | Identificador do turno, etapa ou responsabilidade conversacional. |
| Ator | **[OBRIGATÓRIO]** | Cliente, agente, sistema ou atendente humano. |
| Objetivo do momento | **[OBRIGATÓRIO]** | O que precisa ser alcançado nesse ponto. |
| Entrada ou contexto | **[OBRIGATÓRIO]** | Mensagem, evento, variável ou retorno disponível. |
| Comportamento esperado | **[OBRIGATÓRIO]** | O que o agente deve fazer, sem fixar desnecessariamente o texto final. |
| Informação coletada | [CONDICIONAL] | Dado solicitado ou inferido nesse momento. |
| Estado atualizado | [CONDICIONAL] | Variável, propriedade ou status alterado. |
| Decisão | [CONDICIONAL] | Condição avaliada e opções de saída. |
| Exemplo de mensagem | [OPCIONAL] | Exemplo de conteúdo ou microcopy. |
| Recuperação | **[OBRIGATÓRIO]** | Como reparar silêncio, ambiguidade, erro ou resposta inesperada. |
| Próximo passo | **[OBRIGATÓRIO]** | Próximo momento, rota ou condição de encerramento. |

## 8. Workflow determinístico

> Preencha quando o cenário envolver autenticação, confirmação, transação, obrigação regulatória ou outra sequência que não possa ficar sob livre decisão do modelo.

| Campo | Prioridade | O que registrar |
|---|---|---|
| ID e nome do workflow | [CONDICIONAL] | Identificador único e nome literal. |
| Gatilho | [CONDICIONAL] | Quando o workflow deve iniciar. |
| Pré-condições | [CONDICIONAL] | Autenticação, consentimento, variável ou permissão necessária. |
| Sequência de etapas | [CONDICIONAL] | Ordem obrigatória de mensagens, validações, decisões e ferramentas. |
| Pontos de confirmação | [CONDICIONAL] | Onde o cliente precisa confirmar explicitamente uma ação. |
| Regras de negócio | [CONDICIONAL] | Condições determinísticas e alçadas. |
| Saída de sucesso | [CONDICIONAL] | Resultado verificável e evidência produzida. |
| Saídas de erro | [CONDICIONAL] | Falhas previstas, mensagens e recuperação. |
| Cancelamento | [CONDICIONAL] | Como interromper com segurança e preservar estado. |
| Idempotência e repetição | [CONDICIONAL] | Como evitar duplicidade ao tentar novamente. |
| Auditoria | [CONDICIONAL] | Eventos, protocolos e evidências que devem ser registrados. |

## 9. Conhecimento

> Repita para cada fonte usada pelo agente.

| Campo | Prioridade | O que registrar |
|---|---|---|
| ID e nome da fonte | [CONDICIONAL] | Identificador e nome reconhecível. |
| Fonte autoritativa | [CONDICIONAL] | Documento, sistema ou repositório oficial. |
| Temas cobertos | [CONDICIONAL] | Perguntas que a fonte pode responder. |
| Segmentos e canais | [CONDICIONAL] | Públicos e experiências em que a fonte é válida. |
| Metadados de filtragem | [CONDICIONAL] | Produto, segmento, idioma, região, versão, vigência etc. |
| Owner do conteúdo | [CONDICIONAL] | Responsável pela precisão e atualização. |
| Última revisão | [CONDICIONAL] | Data em que a fonte foi validada. |
| Frequência ou SLA de atualização | [CONDICIONAL] | Periodicidade ou prazo máximo de atualização. |
| Conflitos e precedência | [CONDICIONAL] | Qual fonte prevalece quando houver divergência. |
| Política sem resposta | [CONDICIONAL] | O que fazer quando a recuperação não produzir evidência suficiente. |

## 10. Dados e variáveis

> Repita para cada variável ou dado manipulado.

| Campo | Prioridade | O que registrar |
|---|---|---|
| Nome da variável | [CONDICIONAL] | Nome padronizado. Ex.: `is_authenticated`. |
| Descrição | [CONDICIONAL] | Significado e uso. |
| Tipo e formato | [CONDICIONAL] | Booleano, texto, enum, número, objeto, data etc. |
| Fonte | [CONDICIONAL] | Cliente, canal, API, inferência, sistema ou valor calculado. |
| Obrigatoriedade | [CONDICIONAL] | Em que momento o valor precisa existir. |
| Classificação | [CONDICIONAL] | Público, interno, confidencial, pessoal, financeiro, autenticação etc. |
| Persistência | [CONDICIONAL] | Apenas no turno, sessão, múltiplas sessões ou registro permanente. |
| Mascaramento | [CONDICIONAL] | Forma segura de exibição e armazenamento. |
| Retenção e descarte | [CONDICIONAL] | Prazo e regra para exclusão. |
| Quem pode acessar | [CONDICIONAL] | Agente, ferramenta, atendente, analytics ou áreas específicas. |
| Valor padrão ou ausência | [CONDICIONAL] | Comportamento quando o valor não estiver disponível. |

## 11. Ferramentas e integrações

> Repita para cada API, função, integração ou MCP.

| Campo | Prioridade | O que registrar |
|---|---|---|
| ID e nome literal | [CONDICIONAL] | Nome curto que descreva a ação. Ex.: `Bloquear cartão`. |
| O que faz | [CONDICIONAL] | Capacidade exposta ao agente. |
| Quando usar | [CONDICIONAL] | Trigger específico da chamada. |
| Quando não usar | [CONDICIONAL] | Restrições e rotas alternativas. |
| Sistema e owner | [CONDICIONAL] | Serviço responsável e contato técnico. |
| Entradas | [CONDICIONAL] | Parâmetros e variáveis enviadas. |
| Saídas | [CONDICIONAL] | Dados retornados e interpretação de cada status. |
| Autorização | [CONDICIONAL] | Identidade, permissão, consentimento ou segredo necessário. |
| Efeito da ação | [CONDICIONAL] | Consulta, alteração reversível, alteração irreversível ou transação. |
| Confirmação necessária | [CONDICIONAL] | O que o cliente precisa confirmar antes da chamada. |
| Critério de sucesso | [CONDICIONAL] | Evidência real de que a ação foi concluída. |
| Erros e timeout | [CONDICIONAL] | Códigos, indisponibilidade, mensagens e próximos passos. |
| Repetição segura | [CONDICIONAL] | Como evitar execução duplicada. |
| Dados proibidos na resposta | [CONDICIONAL] | Informações internas ou sensíveis que nunca devem ser exibidas. |
| Observabilidade | [CONDICIONAL] | Eventos, logs, latência e falhas que devem ser monitorados. |

## 12. Risco, privacidade e compliance

| Campo | Prioridade | O que registrar |
|---|---|---|
| Nível de risco | **[OBRIGATÓRIO]** | R0, R1, R2 ou R3, com justificativa. |
| Riscos principais | **[OBRIGATÓRIO]** | Dano possível ao cliente, negócio ou organização. |
| Dados sensíveis envolvidos | **[OBRIGATÓRIO]** | Liste os dados ou declare `Nenhum`. |
| Autenticação necessária | **[OBRIGATÓRIO]** | Nível e momento da verificação de identidade. |
| Consentimento ou confirmação | **[OBRIGATÓRIO]** | Ações que exigem manifestação explícita do cliente. |
| Controles preventivos | **[OBRIGATÓRIO]** | Guardrails, validações, limites, alçadas e bloqueios. |
| Detecção de fraude ou abuso | [CONDICIONAL] | Sinais, comportamento e rota de escalonamento. |
| Conteúdo regulado | [CONDICIONAL] | Avisos, textos obrigatórios ou proibições. |
| Auditoria necessária | [CONDICIONAL] | O que precisa ser rastreável e por quanto tempo. |
| Owner de aprovação | **[OBRIGATÓRIO]** | Área ou papel que aprova o risco residual. |
| Risco residual | **[OBRIGATÓRIO]** | Risco que permanece após os controles e se ele é aceitável. |

## 13. Handoff humano

> Preencha quando houver qualquer possibilidade de transferência.

| Campo | Prioridade | O que registrar |
|---|---|---|
| Gatilhos de handoff | [CONDICIONAL] | Situações que exigem transferência. |
| Destino | [CONDICIONAL] | Fila, equipe, especialista ou canal. |
| Horário e disponibilidade | [CONDICIONAL] | Janela de atendimento e comportamento fora do horário. |
| SLA ou expectativa | [CONDICIONAL] | Prazo informado ao cliente. |
| Mensagem ao cliente | [CONDICIONAL] | Como explicar motivo, destino e próximos passos. |
| Context packet | [CONDICIONAL] | Intenção, resumo, dados verificados, tentativas, erros, urgência e protocolo. |
| Consentimento para transferência | [CONDICIONAL] | Quando e como solicitar. |
| Falha de transferência | [CONDICIONAL] | Alternativa quando a fila ou integração estiver indisponível. |
| Retomada pelo agente | [CONDICIONAL] | Quando e como o agente pode reassumir. |
| Critério de sucesso | [CONDICIONAL] | Evidência de que o cliente foi encaminhado corretamente. |

## 14. Testes, avaliações e métricas

### 14.1 Cenários de teste

| Campo | Prioridade | O que registrar |
|---|---|---|
| ID e nome do teste | **[OBRIGATÓRIO]** | Identificador e comportamento avaliado. |
| Persona e estado inicial | **[OBRIGATÓRIO]** | Perfil, variáveis e pré-condições. |
| Mensagem ou evento inicial | **[OBRIGATÓRIO]** | Entrada que inicia o teste. |
| Variações linguísticas | **[OBRIGATÓRIO]** | Formas alternativas, erros, ambiguidades e linguagem informal. |
| Rota esperada | **[OBRIGATÓRIO]** | Playbook, workflow, conhecimento ou handoff correto. |
| Ferramentas esperadas | [CONDICIONAL] | Chamadas e ordem esperadas. |
| Resposta ou comportamento esperado | **[OBRIGATÓRIO]** | Critério verificável, não apenas uma frase exata. |
| Comportamentos proibidos | **[OBRIGATÓRIO]** | O que deve causar falha no teste. |
| Critério de aprovação | **[OBRIGATÓRIO]** | Condição objetiva de passagem. |
| Severidade da falha | **[OBRIGATÓRIO]** | Baixa, média, alta ou bloqueante. |

### 14.2 Avaliações da conversa

| Campo | Prioridade | O que registrar |
|---|---|---|
| Nome da avaliação | **[OBRIGATÓRIO]** | Resolução, precisão, segurança, clareza, satisfação etc. |
| Pergunta ou critério | **[OBRIGATÓRIO]** | Instrução específica usada para avaliar a conversa completa. |
| Tipo de resultado | **[OBRIGATÓRIO]** | Binário, nota, categorias ou texto. |
| Escala ou opções | **[OBRIGATÓRIO]** | Valores possíveis e significado. |
| Limite de aprovação | **[OBRIGATÓRIO]** | Resultado mínimo aceitável. |
| Evidência necessária | **[OBRIGATÓRIO]** | Elementos da conversa que sustentam a avaliação. |
| Frequência | **[OBRIGATÓRIO]** | Todas as conversas, amostra, por release ou sob gatilho. |
| Owner da métrica | **[OBRIGATÓRIO]** | Responsável por acompanhar e agir. |

### 14.3 Métricas operacionais

| Métrica | Prioridade | Definição a registrar |
|---|---|---|
| Resolução | **[OBRIGATÓRIO]** | O que conta como problema efetivamente resolvido. |
| Handoff | **[OBRIGATÓRIO]** | Transferências esperadas, evitáveis e bem-sucedidas. |
| Abandono | **[OBRIGATÓRIO]** | Em que ponto e condição a conversa é considerada abandonada. |
| Reincidência | **[OBRIGATÓRIO]** | Novo contato pelo mesmo motivo dentro da janela definida. |
| Segurança | **[OBRIGATÓRIO]** | Violações de guardrail, exposição de dados ou ações indevidas. |
| Precisão | **[OBRIGATÓRIO]** | Respostas e ações sustentadas por conhecimento ou retorno real. |
| Satisfação | [OPCIONAL] | CSAT explícito ou avaliação inferida com critério documentado. |
| Latência | [CONDICIONAL] | Tempo de resposta e espera por ferramenta. |
| Custo | [CONDICIONAL] | Custo por conversa, interação ou resolução. |
| Uso de conhecimento e ferramentas | [CONDICIONAL] | Frequência, sucesso, erro e contribuição para a resolução. |

## 15. Governança, release e aprendizagem

| Campo | Prioridade | O que registrar |
|---|---|---|
| Owners por disciplina | **[OBRIGATÓRIO]** | Negócio, conteúdo, tecnologia, dados, risco e operação. |
| Aprovações necessárias | **[OBRIGATÓRIO]** | Quem precisa validar antes da publicação. |
| Ambiente atual | **[OBRIGATÓRIO]** | Descoberta, desenvolvimento, teste, homologação, piloto ou produção. |
| Critérios de entrada em produção | **[OBRIGATÓRIO]** | Testes, aprovações, métricas e contingências mínimas. |
| Estratégia de rollout | **[OBRIGATÓRIO]** | Piloto, público restrito, percentual de tráfego ou lançamento total. |
| Plano de rollback | **[OBRIGATÓRIO]** | Condições e procedimento para reverter ou desativar. |
| Cadência de revisão | **[OBRIGATÓRIO]** | Frequência de revisão de transcrições, métricas, conteúdo e ferramentas. |
| Fontes de aprendizagem | **[OBRIGATÓRIO]** | Transcrições, reclamações, analytics, atendimento humano e incidentes. |
| Backlog de melhoria | **[OBRIGATÓRIO]** | Local, priorização e owner das mudanças. |
| Histórico de decisões | [OPCIONAL] | Decisões relevantes, alternativas descartadas e justificativas. |

## 16. Checklist mínimo obrigatório

Um cenário não deve avançar para implementação sem que estes itens estejam definidos:

- [ ] ID, nome, owner, status e versão.
- [ ] Problema, público, canal, escopo e fora de escopo.
- [ ] Papel, objetivo, tom, guardrails e política de incerteza.
- [ ] Job do cliente e estado inicial.
- [ ] Trigger, quando usar, quando não usar e rota esperada.
- [ ] IDs estáveis e tipos de cartão selecionados a partir do catálogo.
- [ ] Entradas, saídas, `on_success`, `on_error` e `on_timeout` relacionados por wikilinks tipados.
- [ ] Eventos críticos possuem `emitted_by`, `caused_by`, `consumed_by` e `payload`.
- [ ] Resultado esperado e critério de sucesso.
- [ ] Nível de risco, dados sensíveis, autenticação e confirmações.
- [ ] Ações proibidas, recuperação de erro e fallback.
- [ ] Motivos de handoff e destino, quando aplicável.
- [ ] Variáveis, conhecimento e ferramentas, quando aplicáveis.
- [ ] Variáveis selecionadas do catálogo têm origem, classificação, persistência, mascaramento e retenção definidos.
- [ ] Pelo menos um happy path, um caso ambíguo e um caso de falha crítica testados.
- [ ] Métricas de resolução, reincidência, segurança e precisão definidas.
- [ ] Critérios de publicação, monitoramento e rollback aprovados.

---

# Bloco 2 — Dica e exemplo de preenchimento

## Dica geral

Comece pelo **resultado do cliente**, pelo **nível de risco** e pelas **evidências de sucesso**. Só depois detalhe mensagens, ferramentas e caminhos. Isso evita produzir um fluxo conversacional elegante que não consegue concluir a tarefa ou provar que a ação realmente aconteceu.

Em partes agentivas, descreva **responsabilidades e limites**, não todas as frases possíveis. Em partes sensíveis ou transacionais, descreva a sequência determinística, as confirmações e os retornos reais dos sistemas.

## Exemplo — Jornada “cartão perdido”

### 0. Identificação

- **ID:** `AGT-CARTOES-01`
- **Nome:** Assistente de proteção de cartões
- **Objetivo do documento:** alinhar negócio, atendimento, conteúdo, tecnologia e risco para implementar o cenário de perda ou roubo de cartão.
- **Owner:** Produtos Cartões — Atendimento Digital
- **Áreas participantes:** Cartões, Atendimento, Conversation Design, Engenharia, Segurança, Prevenção a Fraudes, Jurídico e Acessibilidade.
- **Status:** em validação
- **Versão e data:** `v0.3 — 2026-08-04`

### 1. Brief

- **Problema do cliente:** o cliente perdeu o cartão, foi roubado ou não sabe onde ele está e precisa reduzir rapidamente o risco de uso indevido.
- **Público-alvo:** clientes pessoa física com cartão ativo.
- **Canais:** app autenticado e chat web autenticado.
- **Produtos:** cartão físico de crédito e débito.
- **Escopo:** identificar o cartão, orientar, bloquear, gerar protocolo e informar próximos passos.
- **Fora de escopo:** contestar transações, desbloquear cartão encontrado, alterar limite ou fornecer aconselhamento jurídico.
- **Resultado primário:** cartão correto bloqueado e cliente informado com evidência verificável.
- **Valor para o negócio:** reduzir fraude, tempo de atendimento e reincidência de contato.

### 2. Agent Charter

- **Papel:** especialista digital em segurança de cartões.
- **Objetivo global:** proteger o cliente rapidamente, mantendo controle, clareza e confirmação explícita sobre ações sensíveis.
- **Tom:** calmo, direto e acolhedor; respostas curtas durante a emergência.
- **Princípios:** reconhecer a urgência, fazer uma pergunta por vez e explicar consequências antes de executar.
- **Guardrails:** nunca revelar o número completo; nunca bloquear sem autenticação e confirmação; nunca afirmar sucesso sem retorno positivo da API; nunca inventar prazo ou protocolo.
- **Política de incerteza:** desambiguar antes de agir; se a API não confirmar a ação, informar a falha e oferecer nova tentativa ou atendimento humano.

### 3. Cliente e contexto

- **Persona:** cliente autenticado com dois cartões ativos.
- **Job:** impedir que outra pessoa utilize o cartão perdido.
- **Estado inicial:** `is_authenticated=true`; dois cartões ativos; nenhum bloqueio iniciado.
- **Estado emocional:** ansioso e com senso de urgência.
- **Acessibilidade:** opções identificadas por nome e final mascarado, não apenas por posição ou cor.
- **Histórico:** nenhuma tentativa de bloqueio na sessão atual.

### 4. Cenário ou playbook

- **ID e nome:** `CRT-012 — Cartão perdido ou roubado`
- **Tipo:** híbrido — playbook agentivo para compreender e orientar; workflow determinístico para bloquear.
- **Problema:** proteger rapidamente um cartão que não está sob controle do cliente.
- **Triggers:** “perdi meu cartão”, “fui roubado”, “não encontro o cartão”, “quero bloquear meu cartão”.
- **Quando usar:** perda, roubo ou cartão temporariamente fora de posse.
- **Quando não usar:** transação não reconhecida sem perda do cartão, desbloqueio ou cartão retido em caixa eletrônico.
- **Resultado esperado:** cartão selecionado bloqueado, protocolo exibido e próximos passos apresentados.
- **Critérios de sucesso:** retorno `blocked=true`, cartão correto identificado, protocolo recebido e cliente informado.
- **Nível de risco:** `R2 — Sensível`; elevar para `R3 — Crítico` diante de coerção, fraude ativa ou vulnerabilidade.
- **Pré-condições:** cliente autenticado e pelo menos um cartão elegível.
- **Variáveis obrigatórias:** `is_authenticated`, `selected_card_id`, `incident_type`, `customer_confirmation`, `block_result` e `protocol_id`.
- **Conhecimento:** política de bloqueio, segunda via, cartão digital e prazos vigentes.
- **Ferramentas:** listar cartões e bloquear cartão.
- **Ações proibidas:** selecionar cartão por suposição, expor número completo ou afirmar bloqueio antes da confirmação do sistema.
- **Condições de saída:** bloqueado, encaminhado, cancelado pelo cliente ou falha técnica registrada.
- **Motivos de handoff:** API indisponível após nova tentativa; fraude ativa; coerção; cliente não consegue autenticar; cartão não localizado.
- **Owner:** Produtos Cartões — Atendimento Digital.

### 5. Relações e cadeia de eventos

#### Propriedades do playbook

```yaml
---
id: PB-012
card_type: playbook
title: Entender ocorrência de cartão
status: validating
owner: Produtos Cartões

relations:
  triggered_by:
    - "[[EVT-001-perda-reportada|Perda reportada]]"
  emits:
    - "[[EVT-002-cartao-selecionado|Cartão selecionado]]"
  routes_to:
    - "[[WF-004-bloquear-cartao|Bloquear cartão]]"
  queries_kb:
    - "[[KB-003-politica-cartoes|Política de cartões]]"
  reads:
    - "[[VAR-001-is-authenticated|Cliente autenticado]]"
    - "[[VAR-021-active-cards|Cartões ativos]]"
  governed_by:
    - "[[RISK-008-bloqueio-cartao-incorreto|Bloqueio do cartão incorreto]]"
  escalates_to:
    - "[[HO-003-cartoes-fraude|Cartões e Fraude]]"
  tested_by:
    - "[[TEST-034-multiplos-cartoes|Cliente com múltiplos cartões]]"
  evaluated_by:
    - "[[EVAL-006-resolucao-segura|Resolução segura]]"
  measured_by:
    - "[[METRIC-011-tempo-protecao|Tempo até proteção]]"
---
```

#### Eventos principais

| Evento | Produzido por | Causado por | Consumido por | Payload principal |
|---|---|---|---|---|
| `EVT-001 — Perda reportada` | Canal de atendimento | Mensagem do cliente | `PB-012` | `conversation_id`, `last_user_utterance`, `channel` |
| `EVT-002 — Cartão selecionado` | `PB-012` | `EVT-001` | `WF-004` | `selected_card_id`, `customer_confirmation=false` |
| `EVT-003 — Bloqueio confirmado` | `TOOL-007` | `WF-004` | `PB-013`, `EVAL-006` | `selected_card_id`, `protocol_id`, `completed_at` |
| `EVT-004 — Bloqueio não confirmado` | `TOOL-007` | `WF-004` | `HO-003`, `EVAL-006` | `tool_status`, `error_code`, `retry_count` |
| `EVT-005 — Timeout ocorrido` | `TOOL-007` | `WF-004` | `WF-005` ou `HO-003` | `correlation_id`, `idempotency_key`, `latency_ms` |

#### Cadeia principal

```text
[[EVT-001-perda-reportada|Perda reportada]]
  → triggers → [[PB-012-entender-ocorrencia|Entender ocorrência]]
  → emits → [[EVT-002-cartao-selecionado|Cartão selecionado]]
  → triggers → [[WF-004-bloquear-cartao|Bloquear cartão]]
  → uses_tool → [[TOOL-007-api-bloqueio|API de bloqueio]]
  → on_success → [[EVT-003-bloqueio-confirmado|Bloqueio confirmado]]
  → on_error → [[EVT-004-bloqueio-nao-confirmado|Bloqueio não confirmado]]
  → on_timeout → [[EVT-005-timeout-bloqueio|Timeout ocorrido]]
```

### 6. Roteamento

- **Entrada:** mensagem do cliente e contexto autenticado da sessão.
- **Sinais:** termos de perda/roubo, número de cartões, autenticação, suspeita de fraude e urgência.
- **Destino principal:** playbook `Entender ocorrência de cartão`.
- **Regra:** usar o playbook quando o cliente indicar perda, roubo ou ausência de posse; iniciar workflow de bloqueio somente após identificar intenção e cartão.
- **Precedência:** suspeita de fraude ou coerção tem prioridade sobre o bloqueio padrão.
- **Desambiguação:** “Você perdeu o cartão físico ou percebeu uma compra que não reconhece?”
- **Fallback:** explicar as capacidades disponíveis e oferecer atendimento humano de cartões.

### 7. Mapa da interação

| ID | Ator | Objetivo | Entrada/contexto | Comportamento esperado | Recuperação | Próximo passo |
|---|---|---|---|---|---|---|
| `M01` | Agente | Compreender a ocorrência | “Perdi meu cartão” | Reconhecer a urgência e confirmar se houve perda, roubo ou fraude | Oferecer opções claras se a resposta for ambígua | `M02` |
| `M02` | Sistema | Listar cartões elegíveis | Cliente autenticado | Consultar cartões e retornar apenas marca e final mascarado | Repetir uma vez; depois oferecer handoff | `M03` |
| `M03` | Agente | Identificar o cartão | Lista mascarada | Apresentar opções e pedir seleção explícita | Confirmar produto e final quando houver dúvida | `M04` |
| `M04` | Agente | Obter confirmação | Cartão selecionado | Explicar que o bloqueio impede novas compras e pedir confirmação | Se o cliente hesitar, responder dúvidas sem executar | `M05` ou cancelamento |
| `M05` | Sistema | Executar bloqueio | Confirmação explícita | Chamar API e aguardar retorno verificável | Não declarar sucesso; repetir ou encaminhar | `M06` ou handoff |
| `M06` | Agente | Comunicar resultado | `blocked=true` e protocolo | Confirmar bloqueio, mostrar protocolo e próximos passos | Se faltar protocolo, informar limitação e registrar ocorrência | Encerramento |

### 8. Workflow determinístico

1. Validar `is_authenticated=true`.
2. Consultar cartões elegíveis.
3. Coletar `selected_card_id` por escolha explícita.
4. Exibir consequências do bloqueio.
5. Coletar `customer_confirmation=true`.
6. Chamar `Bloquear cartão` com identificador interno.
7. Validar `block_result.blocked=true`.
8. Salvar `protocol_id`.
9. Informar resultado e próximos passos.

**Saída de erro:** se houver timeout, consultar o status antes de repetir a operação. Se o estado continuar desconhecido, não repetir cegamente; encaminhar para atendimento humano com a tentativa registrada.

### 9. Conhecimento

- **Fonte:** Política operacional de bloqueio e reemissão de cartões.
- **Autoridade:** Produtos Cartões e Jurídico.
- **Temas:** efeitos do bloqueio, segunda via, cartão digital, prazos e tarifas.
- **Metadados:** `produto`, `segmento`, `bandeira`, `canal`, `idioma`, `vigencia`.
- **Owner:** Gestão de Conteúdo de Cartões.
- **Última revisão:** `2026-07-15`.
- **SLA:** revisar em até um dia útil após mudança de política.
- **Sem resposta:** não inferir; informar que a condição precisa ser confirmada e encaminhar quando necessário.

### 10. Dados e variáveis

| Variável | Tipo | Fonte | Classificação | Persistência | Mascaramento |
|---|---|---|---|---|---|
| `is_authenticated` | booleano | sessão | autenticação | sessão | não exibida |
| `authentication_level` | enum | sessão | autenticação | sessão | não exibida |
| `conversation_id` | texto | canal | interno | registro da conversa | não expor ao cliente |
| `correlation_id` | texto | orquestrador | interno | sessão + observabilidade | não expor ao cliente |
| `selected_card_id` | texto | API + escolha | financeiro/confidencial | sessão | mostrar somente marca e quatro últimos dígitos |
| `incident_type` | enum | cliente | interno | sessão | não aplicável |
| `customer_confirmation` | booleano | cliente | auditoria | sessão + log da ação | registrar evento, não texto sensível |
| `idempotency_key` | texto | workflow | interno | até concluir a ação | não expor ao cliente |
| `tool_status` | enum | API | interno | sessão + observabilidade | traduzir para linguagem do cliente |
| `error_code` | texto | API | interno | observabilidade | nunca exibir código bruto |
| `retry_count` | inteiro | workflow | interno | sessão | não exibida |
| `block_result` | objeto | API | interno | sessão + observabilidade | não expor detalhes técnicos |
| `protocol_id` | texto | API | interno/cliente | conforme política de atendimento | exibir apenas ao cliente autenticado |
| `handoff_required` | booleano | orquestrador | interno | sessão | não exibida |
| `handoff_reason` | enum | agente/workflow | interno | transcrição | apresentar motivo em linguagem simples |
| `handoff_status` | enum | plataforma de atendimento | interno | sessão + observabilidade | informar apenas status útil |
| `resolution_outcome` | enum | avaliação/workflow | interno | analytics | não exibida |
| `started_at` | data/hora | sistema | interno | observabilidade | não exibida |
| `completed_at` | data/hora | sistema | interno | observabilidade | não exibida |
| `latency_ms` | inteiro | observabilidade | interno | analytics | não exibida |

As variáveis `is_authenticated`, `authentication_level`, `conversation_id`, `correlation_id`, `customer_confirmation`, `idempotency_key`, `tool_status`, `retry_count`, `handoff_status`, `resolution_outcome`, `started_at`, `completed_at` e `latency_ms` foram selecionadas diretamente da biblioteca predefinida. `selected_card_id`, `incident_type` e `block_result` são extensões específicas do domínio de cartões e devem entrar no catálogo corporativo apenas se forem reutilizadas por outras jornadas.

### 11. Ferramenta

- **Nome:** `Bloquear cartão`
- **O que faz:** bloqueia permanentemente o cartão físico selecionado.
- **Quando usar:** após autenticação, seleção do cartão e confirmação explícita.
- **Quando não usar:** cartão temporariamente congelado, pedido ambíguo ou ausência de confirmação.
- **Sistema:** plataforma de cartões.
- **Entradas:** `customer_id`, `selected_card_id`, `incident_type`, `confirmation_event_id`.
- **Saídas:** `blocked`, `status`, `protocol_id`, `timestamp`.
- **Efeito:** alteração sensível; reversão não disponível pelo mesmo fluxo.
- **Sucesso:** somente `blocked=true` com protocolo válido.
- **Timeout:** consultar status antes de uma nova tentativa.
- **Dados proibidos:** credenciais, número completo, detalhes internos da autorização e mensagens técnicas brutas.
- **Observabilidade:** sucesso, erro, timeout, latência e chamadas duplicadas.

### 12. Risco e compliance

- **Nível:** `R2 — Sensível`.
- **Riscos:** bloquear o cartão errado, expor dados, deixar de bloquear após afirmar sucesso ou duplicar ações.
- **Dados sensíveis:** identificador do cliente, cartões e protocolo.
- **Autenticação:** sessão forte antes de listar ou alterar cartões.
- **Confirmação:** escolha do cartão e confirmação explícita imediatamente antes da execução.
- **Controles:** mascaramento, workflow determinístico, consulta de status após timeout, logs e handoff.
- **Owner de aprovação:** Segurança, Produtos Cartões e Risco Operacional.
- **Risco residual:** indisponibilidade simultânea da API e do atendimento; aceitação condicionada à contingência operacional.

### 13. Handoff

- **Gatilhos:** indisponibilidade persistente, fraude ativa, coerção, falha de autenticação ou cartão não localizado.
- **Destino:** fila especializada de Cartões/Fraude.
- **Mensagem:** “Não consegui confirmar o bloqueio pelo sistema. Vou encaminhar você para a equipe de cartões com o contexto desta tentativa.”
- **Context packet:** intenção, autenticação, cartão mascarado, tipo de ocorrência, confirmações, chamadas realizadas, erro, horário e urgência.
- **Falha de transferência:** fornecer canal emergencial alternativo e registrar protocolo de contingência.
- **Sucesso:** atendimento recebe o pacote e o cliente recebe confirmação do encaminhamento.

### 14. Testes e avaliações

#### Testes mínimos

1. Cliente autenticado com um cartão — bloqueio concluído.
2. Cliente autenticado com múltiplos cartões — seleção explícita obrigatória.
3. Pedido ambíguo — desambiguação antes de executar.
4. Cliente muda de ideia — nenhuma chamada de bloqueio.
5. Timeout — consulta de status antes de nova tentativa.
6. API retorna falha — agente não afirma sucesso.
7. Cliente não autenticado — nenhuma informação sensível exibida.
8. Suspeita de fraude ou coerção — rota prioritária para especialista.

#### Avaliações

- **Resolução:** o cartão correto foi efetivamente bloqueado ou o cliente recebeu encaminhamento acionável?
- **Segurança:** houve exposição de dado, afirmação sem evidência ou ação sem confirmação?
- **Clareza:** o cliente entendeu qual cartão foi afetado e o que acontece em seguida?
- **Qualidade do handoff:** o atendente recebeu contexto suficiente para não repetir toda a investigação?

#### Métricas

- Taxa de bloqueio confirmado.
- Tempo até proteção do cartão.
- Handoffs bem-sucedidos e handoffs evitáveis.
- Reincidência pelo mesmo motivo em 24 horas.
- Falhas e timeout da API.
- Bloqueios duplicados ou do cartão incorreto.
- Violações de guardrail.
- Clareza e satisfação percebida.

### 15. Governança e release

- **Aprovações:** Produto, Atendimento, Segurança, Risco Operacional, Jurídico, Engenharia e Acessibilidade.
- **Ambiente:** homologação.
- **Entrada em produção:** testes críticos aprovados; contingência validada; monitoramento e atendimento humano disponíveis.
- **Rollout:** piloto com pequena parcela de clientes autenticados, seguido de expansão condicionada às métricas de segurança e resolução.
- **Rollback:** desabilitar ferramenta de bloqueio e manter orientação + handoff humano.
- **Cadência:** revisão diária na primeira semana; semanal no primeiro mês; mensal após estabilização.
- **Aprendizagem:** transcrições redigidas, falhas técnicas, reincidência, reclamações e feedback dos atendentes.

---

## Referências conceituais

- Voiceflow — Introduction: <https://docs.voiceflow.com/documentation/introduction>
- Voiceflow — Choosing a framework: <https://docs.voiceflow.com/documentation/build/framework/choosing-a-framework>
- Voiceflow — Global prompt: <https://docs.voiceflow.com/documentation/build/global-prompt>
- Voiceflow — Instructions: <https://docs.voiceflow.com/documentation/build/instructions>
- Voiceflow — Playbooks: <https://docs.voiceflow.com/documentation/build/playbooks>
- Voiceflow — Workflows: <https://docs.voiceflow.com/documentation/build/workflows>
- Voiceflow — Variables: <https://docs.voiceflow.com/documentation/build/data/variables>
- Voiceflow — Tests: <https://docs.voiceflow.com/documentation/measure/tests>
- Voiceflow — Evaluations: <https://docs.voiceflow.com/documentation/measure/evaluations>
- Voiceflow — Analytics: <https://docs.voiceflow.com/documentation/measure/analytics>
