import requests

url = "http://127.0.0.1:5000/api/incidentes"


r = requests.post(url, json={
    "titulo": "Brute force SSH",
    "severidade": "alta",
    "ip_origem": "185.220.101.1"
})

print("=== Cadastrar incidente ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


id_incidente = r.json()["id"]


r = requests.get(url)
print("\n=== Listar incidentes ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.get(url + "/" + id_incidente)
print("\n=== Buscar incidente ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.get(url + "/id_ruim")
print("\n=== ID invalido ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.put(
    url + "/" + id_incidente,
    json={"status": "resolvido"}
)
print("\n=== Atualizar incidente ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.delete(url + "/" + id_incidente)
print("\n=== Remover incidente ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.post(url, json={"titulo": "Teste"})
print("\n=== Cadastro invalido ===")
print("Status:", r.status_code)
print("Resposta:", r.json())
