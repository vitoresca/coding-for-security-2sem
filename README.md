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

### Exercício 2.1 — CRUD de inventário de ativos

Desenvolvi um sistema em Python utilizando PyMongo para cadastrar, listar, buscar, atualizar e remover ativos no MongoDB. Também utilizei um índice único para impedir o cadastro de IPs duplicados.

![Resultado do exercício 2.1](Aula%202/resultado_2_1.png)

### Exercício 2.2 — Ingestão de logs no MongoDB

Utilizei Python e PyMongo para ler os 23 registros do arquivo auth.log e armazená-los no MongoDB. Depois, utilizei um pipeline de agregação para identificar os IPs com mais falhas de autenticação.

![Resultado do exercício 2.2](Aula%202/resultado_2_2.png)

### Exercício 2.3 — Consultas com filtros avançados

Implementei uma função em Python para consultar eventos no MongoDB usando filtros opcionais por fonte, tipo, IP e data. Os filtros são montados dinamicamente e os resultados são ordenados pela data do evento, do mais recente para o mais antigo.

![Resultado do exercício 2.3](Aula%202/resultado_2_3.png)

### Exercício 3.1 — CRUD de usuários e permissões

Sistema desenvolvido em Python com conexão ao MySQL para cadastrar, listar, buscar, atualizar e remover usuários. Foram utilizadas consultas parametrizadas para prevenir SQL Injection e validação dos níveis de acesso de 1 a 5.

![Resultado do exercício 3.1](Aula%203/resultado_3_1.png)

### Exercício 3.2 — SQL Injection

Foi realizada uma comparação entre uma consulta SQL
com concatenação de strings e uma consulta parametrizada.

A consulta insegura retornou os 3 usuários cadastrados
ao receber a entrada maliciosa. Já a consulta segura
retornou 0 usuários, comprovando a proteção contra
SQL Injection por meio da parametrização.

![Resultado do exercício 3.2](Aula%203/resultado_3_2.png)

### Exercício 3.3 — Relatório de alertas

Desenvolvi um script em Python integrado ao MySQL para cadastrar 10 alertas de segurança e gerar relatórios por severidade, tipo e IP de origem.

Utilizei consultas com GROUP BY, COUNT(*) e ORDER BY para agrupar os registros e identificar os IPs com maior número de alertas.

![Resultado do exercício 3.3](Aula%203/resultado_3_3.png)

### Exercício 4.1 — Classificador de phishing

Desenvolvi um classificador de e-mails utilizando Random Forest com scikit-learn. Separei os dados em treinamento e teste, avaliei o modelo com acurácia, precisão, recall e F1-score e realizei a classificação de um novo e-mail.

![Resultado do exercício 4.1](Aula%204/resultado_4_1.png)

### Exercício 4.2 — Detecção de acessos anômalos

Utilizei o algoritmo Isolation Forest para analisar registros de acesso considerando horário, tentativas de login e quantidade de bytes baixados.

O modelo identificou duas anomalias: acessos realizados de madrugada, com muitas tentativas de login e downloads elevados.

![Resultado do exercício 4.2](Aula%204/resultado_4_2.png)

### Exercício 4.3 — Matriz de confusão e métricas

Calculei a matriz de confusão e as métricas de um modelo de detecção de ataques. O resultado apresentou 90% de acurácia, mas apenas 50% de recall, mostrando que o modelo deixou passar metade dos ataques reais.

![Resultado do exercício 4.3](Aula%204/resultado_4_3.png)

### Exercício 6.1 — API CRUD de usuários

Desenvolvi uma API com Flask para cadastrar, listar, buscar, atualizar e remover usuários armazenados em memória.

Implementei validações para impedir e-mails duplicados e níveis de acesso fora do intervalo de 1 a 5. Testei as rotas com a biblioteca requests, verificando os códigos HTTP 200, 201, 400 e 404.

![Resultado do exercício 6.1](Aula%206/resultado_6_1.png)

### Exercício 6.2 — Endpoint de análise de senha

Desenvolvi uma API Flask para analisar senhas com base em cinco critérios: tamanho mínimo, letras maiúsculas, letras minúsculas, números e caracteres especiais.

A rota retorna a classificação da senha e uma checklist em JSON. Também foram implementadas validações para retornar o código HTTP 400 quando os dados enviados são inválidos.

![Resultado do exercício 6.2](Aula%206/resultado_6_2.png)

### Exercício 6.3 — API de verificação de IP em blacklist

Desenvolvi uma API Flask para verificar se um endereço IPv4 está em uma blacklist e identificar se pertence a uma rede privada ou pública.

Utilizei a biblioteca ipaddress para validar os endereços e implementei respostas HTTP 200 para consultas válidas e 400 para IPs inválidos.

![Resultado do exercício 6.3](Aula%206/resultado_6_3.png)

### Exercício 7.1 — API de incidentes com MongoDB

Desenvolvi uma API Flask integrada ao MongoDB para cadastrar, listar, buscar, atualizar e remover incidentes de segurança.

Implementei a validação dos campos obrigatórios, conversão do ObjectId para JSON e tratamento de identificadores inválidos. As rotas foram testadas com a biblioteca requests.

![Resultado do exercício 7.1](Aula%207/resultado_7_1.png) 
