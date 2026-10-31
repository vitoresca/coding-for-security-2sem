
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId
from datetime import datetime, timezone

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/")
db = client["seguranca"]
incidentes = db["incidentes"]



def serializar(documento):
    documento["_id"] = str(documento["_id"])
    documento["criado_em"] = documento["criado_em"].isoformat()
    return documento



@app.route("/api/incidentes", methods=["GET"])
def listar():
    try:
        pagina = int(request.args.get("pagina", 1))
        tamanho = int(request.args.get("tamanho", 10))
    except ValueError:
        return jsonify({"erro": "Pagina e tamanho devem ser numeros"}), 400

    if pagina < 1 or tamanho < 1:
        return jsonify({"erro": "Pagina e tamanho devem ser maiores que zero"}), 400

    filtro = {}

    severidade = request.args.get("severidade")
    status = request.args.get("status")

    if severidade is not None:
        filtro["severidade"] = severidade

    if status is not None:
        filtro["status"] = status

    resultado = (
        incidentes.find(filtro)
        .sort([("criado_em", -1), ("_id", -1)])
        .skip((pagina - 1) * tamanho)
        .limit(tamanho)
    )

    return jsonify([serializar(doc) for doc in resultado]), 200



@app.route("/api/incidentes/<id>", methods=["GET"])
def buscar(id):
    try:
        identificador = ObjectId(id)
    except InvalidId:
        return jsonify({"erro": "id inválido"}), 400

    documento = incidentes.find_one({"_id": identificador})

    if documento is None:
        return jsonify({"erro": "Incidente não encontrado"}), 404

    return jsonify(serializar(documento)), 200



@app.route("/api/incidentes", methods=["POST"])
def cadastrar():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido"}), 400

    for campo in ("titulo", "severidade", "ip_origem"):
        if not isinstance(dados.get(campo), str) or not dados[campo].strip():
            return jsonify({"erro": f"Campo '{campo}' obrigatório"}), 400

    incidente = {
        "titulo": dados["titulo"],
        "severidade": dados["severidade"],
        "ip_origem": dados["ip_origem"],
        "status": "aberto",
        "criado_em": datetime.now(timezone.utc)
    }

    resultado = incidentes.insert_one(incidente)

    return jsonify({"id": str(resultado.inserted_id)}), 201



@app.route("/api/incidentes/<id>", methods=["PUT"])
def atualizar(id):
    try:
        identificador = ObjectId(id)
    except InvalidId:
        return jsonify({"erro": "id inválido"}), 400

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido"}), 400

    alteracoes = {}

    for campo in ("titulo", "severidade", "status", "ip_origem"):
        if campo in dados:
            if not isinstance(dados[campo], str) or not dados[campo].strip():
                return jsonify({"erro": f"Campo '{campo}' inválido"}), 400
            alteracoes[campo] = dados[campo]

    if not alteracoes:
        return jsonify({"erro": "Nenhum campo para atualizar"}), 400

    resultado = incidentes.update_one(
        {"_id": identificador},
        {"$set": alteracoes}
    )

    if resultado.matched_count == 0:
        return jsonify({"erro": "Incidente não encontrado"}), 404

    documento = incidentes.find_one({"_id": identificador})
    return jsonify(serializar(documento)), 200


@app.route("/api/incidentes/<id>", methods=["DELETE"])
def remover(id):
    try:
        identificador = ObjectId(id)
    except InvalidId:
        return jsonify({"erro": "id inválido"}), 400

    resultado = incidentes.delete_one({"_id": identificador})

    if resultado.deleted_count == 0:
        return jsonify({"erro": "Incidente não encontrado"}), 404

    return jsonify({"mensagem": "Removido"}), 200


if __name__ == "__main__":
    client.admin.command("ping")
    app.run(port=5000, debug=False)
