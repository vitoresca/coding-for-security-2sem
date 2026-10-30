from flask import Flask, jsonify, request

app = Flask(__name__)


usuarios = []
proximo_id = 1



@app.route("/api/usuarios", methods=["GET"])
def listar():
    return jsonify(usuarios), 200


@app.route("/api/usuarios/<int:id>", methods=["GET"])
def buscar(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)

    if usuario is None:
        return jsonify({"erro": "Usuario nao encontrado"}), 404

    return jsonify(usuario), 200



@app.route("/api/usuarios", methods=["POST"])
def cadastrar():
    global proximo_id

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "Dados invalidos"}), 400

    nome = dados.get("nome")
    email = dados.get("email")
    nivel = dados.get("nivel")

    if not isinstance(nome, str) or not nome.strip():
        return jsonify({"erro": "Nome invalido"}), 400

    if not isinstance(email, str) or not email.strip():
        return jsonify({"erro": "Email invalido"}), 400

    if type(nivel) is not int or not 1 <= nivel <= 5:
        return jsonify({"erro": "Nivel invalido"}), 400

    if any(u["email"] == email for u in usuarios):
        return jsonify({"erro": "Email ja existe"}), 400

    usuario = {
        "id": proximo_id,
        "nome": nome,
        "email": email,
        "nivel": nivel
    }

    usuarios.append(usuario)
    proximo_id += 1

    return jsonify(usuario), 201



@app.route("/api/usuarios/<int:id>", methods=["PUT"])
def atualizar(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)

    if usuario is None:
        return jsonify({"erro": "Usuario nao encontrado"}), 404

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "Dados invalidos"}), 400

    nome = dados.get("nome", usuario["nome"])
    email = dados.get("email", usuario["email"])
    nivel = dados.get("nivel", usuario["nivel"])

    if not isinstance(nome, str) or not nome.strip():
        return jsonify({"erro": "Nome invalido"}), 400

    if not isinstance(email, str) or not email.strip():
        return jsonify({"erro": "Email invalido"}), 400

    if type(nivel) is not int or not 1 <= nivel <= 5:
        return jsonify({"erro": "Nivel invalido"}), 400

    if any(u["email"] == email and u["id"] != id for u in usuarios):
        return jsonify({"erro": "Email ja existe"}), 400

    usuario["nome"] = nome
    usuario["email"] = email
    usuario["nivel"] = nivel

    return jsonify(usuario), 200



@app.route("/api/usuarios/<int:id>", methods=["DELETE"])
def remover(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)

    if usuario is None:
        return jsonify({"erro": "Usuario nao encontrado"}), 404

    usuarios.remove(usuario)
    return jsonify({"mensagem": "Removido"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=False)


