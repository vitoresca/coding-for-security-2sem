from pymongo import MongoClient
from datetime import datetime, timedelta, timezone

client = MongoClient("mongodb://localhost:27017/")
incidentes = client["seguranca"]["incidentes"]

dados = [
    ("Brute force SSH", "critica", "aberto"),
    ("Scan de portas", "alta", "aberto"),
    ("Phishing", "media", "resolvido"),
    ("SQL Injection", "critica", "aberto"),
    ("Login suspeito", "baixa", "resolvido"),
    ("Malware", "alta", "aberto"),
    ("Acesso indevido", "critica", "resolvido"),
    ("XSS", "media", "aberto"),
    ("Falhas de login", "alta", "aberto"),
    ("Trafego incomum", "baixa", "resolvido"),
    ("Ransomware", "critica", "aberto"),
    ("Varredura de rede", "media", "resolvido"),
    ("Tentativa de invasao", "alta", "aberto"),
    ("Download suspeito", "alta", "resolvido"),
    ("Ataque de credenciais", "critica", "aberto")
]

# Remove apenas os registros anteriores deste teste
incidentes.delete_many({"lote_teste": "7.2"})

documentos = []
agora = datetime.now(timezone.utc)

for i, (titulo, severidade, status) in enumerate(dados):
    documentos.append({
        "titulo": titulo,
        "severidade": severidade,
        "status": status,
        "ip_origem": f"192.168.1.{i + 10}",
        "criado_em": agora - timedelta(minutes=15 - i),
        "lote_teste": "7.2"
    })

resultado = incidentes.insert_many(documentos)

print("Incidentes cadastrados:", len(resultado.inserted_ids))

client.close()