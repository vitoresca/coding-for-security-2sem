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

### Exercício 7.2 — Paginação e filtros

Implementei paginação e filtros por severidade e status na API de incidentes com Flask e MongoDB. Cadastrei 15 incidentes e testei consultas individuais e combinadas, ordenando os resultados pela data de criação.

Parâmetros aceitos na rota GET /api/incidentes:

- pagina: número da página (padrão: 1).
- tamanho: quantidade de registros por página (padrão: 10).
- severidade: filtra os incidentes pela severidade.
- status: filtra os incidentes pelo status.

Os filtros podem ser combinados e a API retorna HTTP 400 para valores inválidos de paginação.

![Resultado do exercício 7.2](Aula%207/resultado_7_2.png)

### Exercício 7.3 — API de usuários com MySQL

Desenvolvi uma API Flask integrada ao MySQL para cadastrar, listar, buscar, atualizar e remover usuários.

Utilizei consultas parametrizadas e implementei tratamento de erros para e-mails duplicados (409), usuários inexistentes (404), dados inválidos (400) e falhas de conexão com o banco (500).

![Resultado do exercício 7.3](Aula%207/resultado_7_3.png)

### Exercício 8.1 — Dashboard com proteção contra XSS

Criei um dashboard de alertas com Flask, utilizando um formulário HTML para cadastrar e visualizar alertas de segurança.

Testei a proteção contra XSS cadastrando a descrição `<script>alert('xss')</script>`. O conteúdo foi exibido como texto na tabela, sem executar o código JavaScript, utilizando o escape automático do Jinja2.

![Resultado do exercício 8.1](aula%208/resultado_8_1.png)

### Exercício 8.2 — Login seguro com MySQL

Desenvolvi uma API de login utilizando Flask e MySQL, com consultas parametrizadas e verificação de senhas por hash.

Implementei validação dos campos, mensagens genéricas para credenciais inválidas e limite de tentativas de login. Os testes retornaram os códigos HTTP 200, 400, 401 e 429 conforme o esperado.

![Resultado do exercício 8.2](aula%208/resultado_8_2.png)

### Exercício 8.3 — Auditoria de código

Identifiquei cinco vulnerabilidades em uma aplicação Flask, relacionando cada uma ao OWASP Top 10 e propondo medidas de correção.

[Visualizar relatório de auditoria](aula%208/auditoria.md)

### Exercício 10.1 — Consulta de CVEs no NVD

Desenvolvi um programa em Python para consultar a API pública do NVD e obter informações de vulnerabilidades, incluindo descrição, pontuação CVSS e severidade.

Utilizei a CVE-2021-44228 como teste, obtendo CVSS 10.0 e severidade crítica. Também implementei tratamento para CVEs inexistentes, falhas de requisição e timeout.

![Resultado do exercício 10.1](Aula%2010/resultado_10_1.png)

### Exercício 10.2 — Explorador da API do GitHub

Desenvolvi um programa em Python com menu para consultar perfis e repositórios públicos por meio da API REST do GitHub.

Implementei busca de usuários, listagem de repositórios com paginação, consulta detalhada e exportação dos resultados em JSON. Também adicionei tratamento para falhas de conexão, timeout e limites de requisições.

![Resultado do exercício 10.2](Aula%2010/resultado_10_2.png)

[Arquivo JSON gerado](Aula%2010/github_vitoresca.json)

### Exercício 10.3 — Enriquecimento de IPs com cache

Desenvolvi um programa em Python para consultar informações de IPs externos, identificar endereços de redes internas e evitar consultas repetidas por meio de cache.

Implementei tratamento de rate limit com backoff e geração de relatório. Nos testes, foram realizadas 3 consultas HTTP, com 1 resultado recuperado do cache e 1 IP interno identificado.

![Resultado do exercício 10.3](Aula%2010/resultado_10_3.png)

[Relatório gerado](Aula%2010/relatorio_10_3.txt)

### Exercício 12.1 — Pipeline de detecção com normalização

Desenvolvi um Pipeline utilizando StandardScaler e RandomForestClassifier para classificar tráfego de rede como normal ou malicioso.

Utilizei validação cruzada com 5 folds para avaliar o modelo, calculando a média da acurácia e o desvio padrão dos resultados.

![Resultado do exercício 12.1](Aula%2012/resultado_12_1.png)


### Exercício 12.2 — Torneio de algoritmos

Comparei Random Forest, SVM e KNN utilizando validação cruzada com 5 folds. Os três modelos obtiveram acurácia média de 1.00.

Como houve empate, selecionei o Random Forest pelo critério de desempate definido no programa. Depois utilizei GridSearchCV, que selecionou max_depth=None e n_estimators=50, mantendo a acurácia de 1.00.

![Resultado do exercício 12.2](Aula%2012/resultado_12_2.png)

### Exercício 12.3 — Persistência e integridade do modelo

Treinei um modelo Random Forest com os melhores parâmetros encontrados no exercício anterior e salvei o resultado utilizando joblib.

Calculei o hash SHA-256 do arquivo, armazenei o valor de referência e realizei uma nova verificação antes de carregar o modelo. Após confirmar a integridade, executei uma previsão de teste.

![Resultado do exercício 12.3](Aula%2012/resultado_12_3.png)

### Exercício 13.1 — Chatbot de Segurança

Desenvolvi um chatbot em Python para responder perguntas sobre segurança da informação, mantendo o histórico da conversa para utilizar o contexto das mensagens anteriores.

O programa permite encerrar a conversa com o comando `/sair` e possui tratamento de erros. Para os testes, utilizei o modo mock disponibilizado na apostila, simulando as respostas sem precisar de uma chave de API.

**Resultado da execução:**

![Resultado do exercício 13.1](Aula%2013/resultado_13_1.png)

### Exercício 13.2 — Classificador automático de logs em lote

Desenvolvi um classificador de logs de segurança em Python, com integração opcional à API da OpenAI e um sistema de fallback baseado em regras.

O programa identificou um acesso normal, uma possível tentativa de path traversal e um evento suspeito de força bruta. Também gerou um relatório com a quantidade de eventos por classificação.

**Resultado da execução:**

![Resultado do exercício 13.2](Aula%2013/resultado_13_2.png)

**Relatório gerado:**

[Visualizar relatório de classificação](Aula%2013/relatorio_13_2.txt)


### Exercício 13.3 — Demonstração de Prompt Injection

Realizei uma demonstração de prompt injection utilizando um log de falha de login contendo uma instrução maliciosa para forçar a classificação NORMAL.

No modo mock, o classificador sem proteção retornou NORMAL, enquanto a versão protegida identificou o evento como SUSPEITO.

Implementei delimitação da entrada, validação dos rótulos permitidos e fallback por regras. Também gerei um relatório com os resultados dos testes.

**Resultado da execução:**

![Resultado do exercício 13.3](Aula%2013/resultado_13_3.png)

**Relatório gerado:**

[Visualizar relatório do exercício 13.3](Aula%2013/relatorio_13_3.txt)
