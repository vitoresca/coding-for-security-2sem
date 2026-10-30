import requests

url = "http://127.0.0.1:5000/api/analisar-senha"


r = requests.post(url, json={"senha": "Cyber@2024"})
print("=== Teste 1 - Senha forte ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.post(url, json={})
print("\n=== Teste 2 - Campo ausente ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.post(url, json={"senha": "abc"})
print("\n=== Teste 3 - Senha fraca ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.post(url, json={"senha": 12345})
print("\n=== Teste 4 - Tipo invalido ===")
print("Status:", r.status_code)
print("Resposta:", r.json())
