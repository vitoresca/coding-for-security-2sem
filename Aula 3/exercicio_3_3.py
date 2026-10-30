
import mysql.connector
from mysql.connector import Error
from getpass import getpass

conexao = None
cursor = None

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Senha do MySQL: "),
        database="seguranca"
    )

    cursor = conexao.cursor(dictionary=True)

   
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alertas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tipo VARCHAR(50),
            descricao TEXT,
            ip_origem VARCHAR(45),
            severidade ENUM('baixa', 'media', 'alta', 'critica')
        )
    """)

  
    cursor.execute("SHOW COLUMNS FROM alertas LIKE 'descricao'")
    if cursor.fetchone() is None:
        cursor.execute("ALTER TABLE alertas ADD COLUMN descricao TEXT")

    cursor.execute("SHOW COLUMNS FROM alertas LIKE 'ip_origem'")
    if cursor.fetchone() is None:
        cursor.execute(
            "ALTER TABLE alertas ADD COLUMN ip_origem VARCHAR(45)"
        )

   
    alertas = [
        ("BRUTE_FORCE", "EX3.3 - Falhas de login", "185.220.101.1", "critica"),
        ("BRUTE_FORCE", "EX3.3 - Tentativas de acesso", "185.220.101.1", "alta"),
        ("BRUTE_FORCE", "EX3.3 - Ataque de senha", "45.33.32.156", "critica"),
        ("BRUTE_FORCE", "EX3.3 - Falhas repetidas", "192.168.1.50", "media"),
        ("PORT_SCAN", "EX3.3 - Varredura de portas", "185.220.101.1", "alta"),
        ("PORT_SCAN", "EX3.3 - Scan detectado", "45.33.32.156", "alta"),
        ("PORT_SCAN", "EX3.3 - Scan interno", "192.168.1.50", "media"),
        ("XSS", "EX3.3 - Script malicioso", "185.220.101.1", "critica"),
        ("XSS", "EX3.3 - Tentativa de XSS", "45.33.32.156", "baixa"),
        ("SQLI", "EX3.3 - Tentativa de SQL Injection", "10.0.0.5", "alta")
    ]

    
    cursor.execute(
        "DELETE FROM alertas WHERE descricao LIKE %s",
        ("EX3.3 - %",)
    )

  
    cursor.executemany(
        """INSERT INTO alertas
           (tipo, descricao, ip_origem, severidade)
           VALUES (%s, %s, %s, %s)""",
        alertas
    )

    conexao.commit()
    print("10 alertas cadastrados!")

   
    print("\n=== Por severidade ===")

    cursor.execute("""
        SELECT severidade, COUNT(*) AS total
        FROM alertas
        WHERE descricao LIKE %s
        GROUP BY severidade
        ORDER BY FIELD(severidade, 'critica', 'alta', 'media', 'baixa')
    """, ("EX3.3 - %",))

    for linha in cursor.fetchall():
        print(f"{linha['severidade']}: {linha['total']}")

    print("\n=== Por tipo ===")

    cursor.execute("""
        SELECT tipo, COUNT(*) AS total
        FROM alertas
        WHERE descricao LIKE %s
        GROUP BY tipo
        ORDER BY total DESC
    """, ("EX3.3 - %",))

    for linha in cursor.fetchall():
        print(f"{linha['tipo']}: {linha['total']}")

   
    print("\n=== Top IPs de origem ===")

    cursor.execute("""
        SELECT ip_origem, COUNT(*) AS total
        FROM alertas
        WHERE descricao LIKE %s
        GROUP BY ip_origem
        ORDER BY total DESC
        LIMIT 5
    """, ("EX3.3 - %",))

    for linha in cursor.fetchall():
        print(f"{linha['ip_origem']} -> {linha['total']} alertas")

except Error as erro:
    if conexao and conexao.is_connected():
        conexao.rollback()
    print("Erro no MySQL:", erro)

finally:
    if cursor is not None:
        cursor.close()
    if conexao and conexao.is_connected():
        conexao.close()
