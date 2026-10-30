import requests

url = "http://127.0.0.1:5000/api/usuarios"


r = requests.post(
    url,
    json={"nome": "Ana", "email": "ana@x.com", "nivel": 5}
)
print("Cadastrar Ana:", r.status_code, r.json())


r = requests.post(
    url,
    json={"nome": "Bia", "email": "ana@x.com", "nivel": 2}
)
print("Email duplicado:", r.status_code, r.json())


r = requests.post(
    url,
    json={"nome": "Cid", "email": "cid@x.com", "nivel": 9}
)
print("Nivel invalido:", r.status_code, r.json())

r = requests.get(url + "/1")
print("Buscar usuario 1:", r.status_code, r.json())


r = requests.get(url + "/99")
print("Buscar usuario 99:", r.status_code, r.json())


r = requests.put(url + "/1", json={"nivel": 4})
print("Atualizar Ana:", r.status_code, r.json())


r = requests.get(url)
print("Listar usuarios:", r.status_code, r.json())


r = requests.delete(url + "/1")
print("Remover Ana:", r.status_code, r.json())
