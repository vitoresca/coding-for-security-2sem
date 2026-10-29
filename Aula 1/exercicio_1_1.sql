
-- Exercicio 1.1 - Modelagem de banco de vulnerabilidades

CREATE DATABASE IF NOT EXISTS seguranca;
USE seguranca;


CREATE TABLE ativos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ip VARCHAR(45),
    tipo VARCHAR(50),
    criticidade VARCHAR(20)
);


CREATE TABLE vulnerabilidades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cve_id VARCHAR(30) NOT NULL,
    descricao TEXT,
    severidade ENUM('Baixa', 'Media', 'Alta', 'Critica'),
    cvss DECIMAL(3,1)
);

CREATE TABLE ativo_vulnerabilidade (
    ativo_id INT NOT NULL,
    vuln_id INT NOT NULL,
    status VARCHAR(20) DEFAULT 'aberta',
    detectada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (ativo_id, vuln_id),
    FOREIGN KEY (ativo_id) REFERENCES ativos(id),
    FOREIGN KEY (vuln_id) REFERENCES vulnerabilidades(id)
);


INSERT INTO ativos (nome, ip, tipo, criticidade)
VALUES ('SRV-WEB01', '192.168.1.10', 'servidor', 'Alta');


INSERT INTO vulnerabilidades (cve_id, descricao, severidade, cvss)
VALUES ('CVE-2024-001', 'Vulnerabilidade de teste', 'Alta', 8.5);


SELECT * FROM ativos;
SELECT * FROM vulnerabilidades;


INSERT INTO ativo_vulnerabilidade (ativo_id, vuln_id, status)
VALUES (1, 1, 'aberta');

SELECT * FROM ativo_vulnerabilidade;
