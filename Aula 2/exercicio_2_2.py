
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
client.admin.command("ping")

db = client["seguranca"]
eventos = db["eventos"]

documentos = []

with open("auth.log", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        partes = linha.strip().split()

        data = partes[0]
        hora = partes[1]
        tipo = partes[2]
        usuario = partes[3].split("=")[1]
        ip = partes[4].split("=")[1]

        evento = {
            "timestamp": datetime.strptime(
                data + " " + hora, "%Y-%m-%d %H:%M:%S"
            ),
            "tipo": tipo,
            "usuario": usuario,
            "ip": ip
        }

        documentos.append(evento)

resultado = eventos.insert_many(documentos)

pipeline = [
    {"$match": {"tipo": "FAIL"}},
    {"$group": {"_id": "$ip", "total": {"$sum": 1}}},
    {"$sort": {"total": -1}},
    {"$limit": 5}
]

print("=== Top IPs por falhas de login ===")

for linha in eventos.aggregate(pipeline):
    print(f"{linha['_id']} -> {linha['total']} falhas")

print("Total de eventos inseridos:", len(resultado.inserted_ids))

client.close()
