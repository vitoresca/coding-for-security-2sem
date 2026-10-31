
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from mysql.connector import Error
import mysql.connector
from getpass import getpass
import time

app = Flask(__name__)

senha_mysql = getpass("Senha do MySQL: ")

tentativas = {}
LIMITE = 5
BLOQUEIO_SEGUNDOS = 60


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=senha_mysql,
        database="seguranca",
        connection_timeout=5
    )



def preparar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios_login (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(100) NOT NULL UNIQUE,
                senha_hash VARCHAR(255) NOT NULL
            )
        """)

        usuarios_iniciais = {
            "admin": "Cyber@2024",
            "analista": "S3gur4nca!"
        }

        for usuario, senha in usuarios_iniciais.items():
            cursor.execute(
                """INSERT IGNORE INTO usuarios_login
                   (usuario, senha_hash) VALUES (%s, %s)""",
                (usuario, generate_password_hash(senha))
            )

        conexao.commit()
        print("Tabela de login preparada!")

    finally:
        cursor.close()
        conexao.close()


@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "Corpo inválido"}), 400

    usuario = dados.get("usuario")
    senha = dados.get("senha")

    if (not isinstance(usuario, str) or not usuario.strip()
            or not isinstance(senha, str) or not senha):
        return jsonify({"erro": "Usuário e senha obrigatórios"}), 400

    ip = request.remote_addr
    agora = time.monotonic()

    historico = tentativas.get(ip, [])
    historico = [
        instante for instante in historico
        if agora - instante < BLOQUEIO_SEGUNDOS
    ]
    tentativas[ip] = historico

    if len(historico) >= LIMITE:
        return jsonify({
            "erro": "Muitas tentativas. Tente novamente mais tarde."
        }), 429

    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        
        cursor.execute(
            "SELECT senha_hash FROM usuarios_login WHERE usuario = %s",
            (usuario,)
        )

        registro = cursor.fetchone()

        if registro and check_password_hash(
            registro["senha_hash"], senha
        ):
            tentativas.pop(ip, None)
            return jsonify({"mensagem": "Login OK"}), 200

        
        tentativas[ip].append(agora)

        return jsonify({"erro": "Credenciais inválidas"}), 401

    except Error:
        return jsonify({"erro": "Serviço indisponível"}), 500

    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None and conexao.is_connected():
            conexao.close()


if __name__ == "__main__":
    preparar_banco()
    app.run(port=5000, debug=False)
