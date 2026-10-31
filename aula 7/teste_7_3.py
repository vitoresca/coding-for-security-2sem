import requests

url = "http://127.0.0.1:5000/api/usuarios"


r = requests.get(url)
print("=== Listar usuarios ===")
print("Status:", r.status_code)
print("Resposta:", r.json())



r = requests.post(url, json={
    "nome": "Outro Carlos",
    "email": "carlos@empresa.com",
    "nivel_acesso": 3
})
print("\n=== Email duplicado ===")
print("Status:", r.status_code)
print("Resposta:", r.json())



r = requests.get(url + "/999")
print("\n=== Usuario inexistente ===")
print("Status:", r.status_code)
print("Resposta:", r.json())



r = requests.post(url, json={
    "nome": "Bia",
    "nivel_acesso": 2
})
print("\n=== Email ausente ===")
print("Status:", r.status_code)
print("Resposta:", r.json())



r = requests.post(url, json={
    "nome": "Usuario Teste",
    "email": "teste73@empresa.com",
    "nivel_acesso": 2
})
print("\n=== Cadastrar usuario ===")
print("Status:", r.status_code)
print("Resposta:", r.json())

if r.status_code == 201:
    id_usuario = r.json()["id"]

   
    r = requests.put(
        url + "/" + str(id_usuario),
        json={"nivel_acesso": 4}
    )
    print("\n=== Atualizar usuario ===")
    print("Status:", r.status_code)
    print("Resposta:", r.json())


    r = requests.delete(url + "/" + str(id_usuario))
    print("\n=== Remover usuario ===")
    print("Status:", r.status_code)
    print("Resposta:", r.json())
