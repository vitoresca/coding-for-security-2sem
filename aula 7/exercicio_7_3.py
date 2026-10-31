from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error, IntegrityError
from getpass import getpass
from functools import wraps

app = Flask(__name__)


senha_mysql = getpass("Senha do MySQL: ")



def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=senha_mysql,
        database="seguranca",
        connection_timeout=5
    )



def tratar_banco(funcao):
    @wraps(funcao)
    def executar(*args, **kwargs):
        conexao = None

        try:
            conexao = get_db()
            return funcao(conexao, *args, **kwargs)

        except Error:
            if conexao is not None and conexao.is_connected():
                conexao.rollback()

            return jsonify({"erro": "serviço indisponível"}), 500

        finally:
            if conexao is not None and conexao.is_connected():
                conexao.close()

    return executar


@app.route("/api/usuarios", methods=["GET"])
@tratar_banco
def listar(conexao):
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, nome, email, nivel_acesso FROM usuarios"
    )

    usuarios = cursor.fetchall()
    cursor.close()

    return jsonify(usuarios), 200



@app.route("/api/usuarios/<int:id>", methods=["GET"])
@tratar_banco
def buscar(conexao, id):
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, nome, email, nivel_acesso FROM usuarios WHERE id = %s",
        (id,)
    )

    usuario = cursor.fetchone()
    cursor.close()

    if usuario is None:
        return jsonify({"erro": "usuário não encontrado"}), 404

    return jsonify(usuario), 200



@app.route("/api/usuarios", methods=["POST"])
@tratar_banco
def cadastrar(conexao):
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "corpo inválido"}), 400

    nome = dados.get("nome")
    email = dados.get("email")
    nivel = dados.get("nivel_acesso", 1)

    if not isinstance(nome, str) or not nome.strip():
        return jsonify({"erro": "nome obrigatório"}), 400

    if not isinstance(email, str) or not email.strip():
        return jsonify({"erro": "email obrigatório"}), 400

    if type(nivel) is not int or not 1 <= nivel <= 5:
        return jsonify({"erro": "nível inválido"}), 400

    cursor = conexao.cursor()

    try:
        cursor.execute(
            """INSERT INTO usuarios (nome, email, nivel_acesso)
               VALUES (%s, %s, %s)""",
            (nome, email, nivel)
        )

        conexao.commit()
        return jsonify({"id": cursor.lastrowid}), 201

    except IntegrityError:
        conexao.rollback()
        return jsonify({"erro": "email já cadastrado"}), 409

    finally:
        cursor.close()



@app.route("/api/usuarios/<int:id>", methods=["PUT"])
@tratar_banco
def atualizar(conexao, id):
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "corpo inválido"}), 400

    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM usuarios WHERE id = %s",
            (id,)
        )

        usuario = cursor.fetchone()

        if usuario is None:
            return jsonify({"erro": "usuário não encontrado"}), 404

        nome = dados.get("nome", usuario["nome"])
        email = dados.get("email", usuario["email"])
        nivel = dados.get("nivel_acesso", usuario["nivel_acesso"])

        if not isinstance(nome, str) or not nome.strip():
            return jsonify({"erro": "nome inválido"}), 400

        if not isinstance(email, str) or not email.strip():
            return jsonify({"erro": "email inválido"}), 400

        if type(nivel) is not int or not 1 <= nivel <= 5:
            return jsonify({"erro": "nível inválido"}), 400

        try:
            cursor.execute(
                """UPDATE usuarios
                   SET nome = %s, email = %s, nivel_acesso = %s
                   WHERE id = %s""",
                (nome, email, nivel, id)
            )

            conexao.commit()

        except IntegrityError:
            conexao.rollback()
            return jsonify({"erro": "email já cadastrado"}), 409

        return jsonify({"mensagem": "Usuário atualizado"}), 200

    finally:
        cursor.close()



@app.route("/api/usuarios/<int:id>", methods=["DELETE"])
@tratar_banco
def remover(conexao, id):
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "DELETE FROM usuarios WHERE id = %s",
            (id,)
        )

        quantidade = cursor.rowcount

        if quantidade == 0:
            conexao.rollback()
            return jsonify({"erro": "usuário não encontrado"}), 404

        conexao.commit()
        return jsonify({"mensagem": "Removido"}), 200

    finally:
        cursor.close()


if __name__ == "__main__":
    app.run(port=5000, debug=False)
