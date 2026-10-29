USE seguranca;

CREATE TABLE alertas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    ip_origem VARCHAR(45),
    severidade ENUM('baixa', 'media', 'alta', 'critica'),
    status VARCHAR(20) DEFAULT 'aberto',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO alertas (tipo, ip_origem, severidade)
VALUES
('BRUTE_FORCE', '185.220.101.1', 'critica'),
('PORT_SCAN', '192.168.1.50', 'alta'),
('SQL_INJECTION', '45.33.32.156', 'alta');

SELECT * FROM alertas
WHERE severidade = 'alta';

UPDATE alertas
SET status = 'resolvido'
WHERE id = 1;

SELECT severidade, COUNT(*) AS total
FROM alertas
GROUP BY severidade;


SELECT * FROM alertas
WHERE criado_em < NOW() - INTERVAL 90 DAY;