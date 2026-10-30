
from flask import Flask, jsonify
import ipaddress

app = Flask(__name__)


blacklist = {
    "185.220.101.1",
    "45.33.32.156",
    "91.240.118.172"
}


@app.route("/api/checar-ip/<ip>", methods=["GET"])
def checar_ip(ip):

   
    try:
        endereco = ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError:
        return jsonify({"erro": "IP inválido"}), 400

   
    na_blacklist = ip in blacklist

   
    redes_privadas = [
        ipaddress.IPv4Network("10.0.0.0/8"),
        ipaddress.IPv4Network("172.16.0.0/12"),
        ipaddress.IPv4Network("192.168.0.0/16")
    ]

    privado = any(endereco in rede for rede in redes_privadas)

    if privado:
        tipo = "privado"
    else:
        tipo = "publico"

    return jsonify({
        "ip": ip,
        "na_blacklist": na_blacklist,
        "tipo": tipo
    }), 200


if __name__ == "__main__":
    app.run(port=5000, debug=False)
