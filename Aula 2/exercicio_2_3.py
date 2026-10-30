
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
client.admin.command("ping")

db = client["seguranca"]
eventos = db["eventos"]

eventos.update_many(
    {"fonte": {"$exists": False}},
    {"$set": {"fonte": "auth"}}
)

def consultar(fonte=None, tipo=None, ip=None, desde=None):
    filtro = {}

    if fonte is not None:
        filtro["fonte"] = fonte

    if tipo is not None:
        filtro["tipo"] = tipo

    if ip is not None:
        filtro["ip"] = ip

    if desde is not None:
        filtro["timestamp"] = {"$gte": desde}

    resultados = list(
        eventos.find(filtro).sort("timestamp", -1)
    )

    return resultados



print("=== Falhas do IP 185.220.101.1 ===")

resultado1 = consultar(tipo="FAIL", ip="185.220.101.1")

for evento in resultado1:
    print(evento)


print("\n=== Eventos da fonte auth ===")

resultado2 = consultar(fonte="auth")

for evento in resultado2:
    print(evento)


print("\n=== Eventos a partir de 20/02/2025 ===")

data = datetime(2025, 2, 20)

resultado3 = consultar(desde=data)

for evento in resultado3:
    print(evento)

client.close()
