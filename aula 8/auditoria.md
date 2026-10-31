# Exercício 8.3 — Auditoria de código

## 1. SQL Injection — A05: Injection

**Falha:** a consulta SQL utiliza concatenação direta do nome informado pelo usuário.

Isso permite que uma entrada maliciosa altere a lógica da consulta e acesse informações indevidas.

**Correção:** utilizar consultas parametrizadas com `%s`, mantendo a entrada do usuário separada do comando SQL.

## 2. Cross-Site Scripting (XSS) — A05: Injection

**Falha:** o nome informado pelo usuário é inserido diretamente no HTML, sem tratamento.

Isso pode permitir a execução de JavaScript malicioso no navegador.

**Correção:** utilizar `escape()` ou templates Jinja2 com escape automático para exibir os dados de maneira segura.

## 3. Security Misconfiguration — A02

**Falha:** a aplicação utiliza `debug=True` e está configurada para aceitar conexões em todas as interfaces de rede.

Essa configuração pode expor informações internas e recursos de depuração.

**Correção:** desativar o debug em produção e utilizar um servidor web configurado adequadamente.

## 4. Senha exposta no código — A02: Security Misconfiguration

**Falha:** a senha do banco de dados está escrita diretamente no código (`SENHA_DB = "123456"`).

Caso o arquivo seja compartilhado, a credencial poderá ser exposta.

**Correção:** utilizar uma senha forte armazenada em variável de ambiente ou gerenciador de segredos, sem publicá-la no GitHub.

## 5. Ausência de logs — A09: Security Logging & Alerting Failures

**Falha:** a aplicação não registra acessos, erros ou tentativas suspeitas.

Isso dificulta a identificação de ataques e a investigação de incidentes.

**Correção:** implementar registros de acesso e de erros utilizando o módulo `logging` do Python, evitando registrar senhas e informações sensíveis.

## Conclusão

A análise identificou cinco vulnerabilidades relacionadas à manipulação de dados, configuração da aplicação e monitoramento de segurança. A aplicação de consultas parametrizadas, escape de saída, proteção de credenciais e registros de eventos ajuda a reduzir esses riscos.