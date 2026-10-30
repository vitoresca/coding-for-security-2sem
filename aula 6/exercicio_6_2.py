from flask import Flask, jsonify, request

app = Flask(__name__)



def verificar_senha(senha):
    criterios = {
        "tamanho_min": len(senha) >= 8,
        "maiuscula": any(letra.isupper() for letra in senha),
        "minuscula": any(letra.islower() for letra in senha),
        "numero": any(letra.isdigit() for letra in senha),
        "especial": any(not letra.isalnum() for letra in senha)
    }

    total = sum(criterios.values())

    if total == 5:
        forca = "Muito forte"
    elif total == 4:
        forca = "Forte"
    elif total == 3:
        forca = "Media"
    else:
        forca = "Fraca"

    return forca, criterios



@app.route("/api/analisar-senha", methods=["POST"])
def analisar_senha():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict) or "senha" not in dados:
        return jsonify({"erro": "campo 'senha' obrigatório"}), 400

    senha = dados["senha"]

    if not isinstance(senha, str) or not senha:
        return jsonify({"erro": "senha inválida"}), 400

    forca, criterios = verificar_senha(senha)

    return jsonify({
        "forca": forca,
        "criterios": criterios
    }), 200


if __name__ == "__main__":
    app.run(port=5000, debug=False)
