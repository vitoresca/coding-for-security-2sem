# coding-for-security-2sem
Exercícios da disciplina Coding for Security - FIAP
# Coding for Security — 2º Semestre

Repositório destinado aos exercícios práticos da disciplina **Coding for Security**, do curso de **Segurança Cibernética da FIAP**.

O objetivo é reunir as atividades desenvolvidas ao longo do semestre, aplicando conceitos de programação em Python voltados à segurança da informação.

## Conteúdos abordados

- **Banco de Dados:** SQL, NoSQL e Teorema CAP.
- **MongoDB:** operações CRUD, consultas e gerenciamento de dados.
- **MySQL:** integração com Python, consultas parametrizadas e prevenção de SQL Injection.
- **Machine Learning:** classificação de dados, detecção de anomalias e avaliação de modelos.
- **Flask:** desenvolvimento de APIs REST e integração com bancos de dados.
- **Segurança Web:** vulnerabilidades OWASP, XSS e boas práticas de desenvolvimento seguro.
- **APIs RESTful:** consumo de APIs externas, autenticação, paginação e tratamento de erros.
- **Machine Learning Avançado:** pipelines, validação cruzada e persistência de modelos.
- **LLMs:** integração de modelos de linguagem para análise de eventos de segurança.

## Organização

Os exercícios estão separados em pastas de acordo com as aulas da disciplina

## Aula 1 — Banco de Dados

### Exercício 1.1 — Modelagem de vulnerabilidades

Neste exercício, criei um banco de dados MySQL com três tabelas: ativos, vulnerabilidades e ativo_vulnerabilidade.

Utilizei chaves primárias e estrangeiras para relacionar os equipamentos às vulnerabilidades cadastradas.

Para testar, cadastrei o servidor SRV-WEB01 e a vulnerabilidade CVE-2024-001, com severidade Alta e CVSS 8.5.

### Resultado da execução

![Resultado do exercício 1.1](Aula%201/resultado_1_1.png) 


### Exercício 1.2 — CRUD SQL

Neste exercício, utilizei comandos SQL para cadastrar, consultar,
atualizar e excluir alertas de segurança.

Cadastrei três alertas e consultei os de severidade alta.
Também atualizei o status de um registro, contei os alertas
por severidade e apliquei um filtro para excluir os mais antigos
que 90 dias.

#### Resultado da execução

![Resultado do exercício 1.2](Aula%201/resultado_1_2.png)
