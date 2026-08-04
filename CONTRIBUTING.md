# Contribuindo

## Antes de abrir uma mudança

1. Comece por um arquivo em `templates/` ou por um exemplo existente.
2. Escolha o tipo de cartão e um ID estável.
3. Declare todos os campos-base do [schema](docs/schema.md).
4. Use relações tipadas de primeiro nível com IDs estáveis e links Markdown relativos no corpo.
5. Para ações sensíveis, descreva autenticação, confirmação, idempotência, falhas e handoff.

## Critério de aceite

- Frontmatter válido e campos obrigatórios preenchidos.
- ID único e nome de arquivo iniciado pelo ID.
- Links Markdown relativos e IDs de relações resolvidos.
- Eventos com payload e chave de correlação.
- Testes, avaliação e métrica associados quando a jornada entra em produção.

## Fluxo de contribuição

Crie uma branch, mantenha uma mudança coesa por pull request e execute a validação automática antes da revisão.

