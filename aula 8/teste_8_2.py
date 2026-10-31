
import requests

url = "http://127.0.0.1:5000/login"


def testar(nome, dados):
    resposta = requests.post(url, json=dados)
    print("\n===", nome, "===")
    print("Status:", resposta.status_code)
    print("Resposta:", resposta.json())


testar("Senha incorreta", {
    "usuario": "admin",
    "senha": "errada"
})


testar("Login correto", {
    "usuario": "admin",
    "senha": "Cyber@2024"
})


testar("Campos vazios", {
    "usuario": "",
    "senha": ""
})


testar("Usuario inexistente", {
    "usuario": "usuario_que_nao_existe",
    "senha": "qualquer"
})


print("\n=== Limite de tentativas ===")

for i in range(6):
    resposta = requests.post(url, json={
        "usuario": "admin",
        "senha": "senha_errada"
    })

    print(
        f"Tentativa {i + 1}:",
        resposta.status_code,
        resposta.json()
    )
