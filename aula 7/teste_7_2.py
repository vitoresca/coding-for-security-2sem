import requests

url = "http://127.0.0.1:5000/api/incidentes"


def testar(nome, parametros):
    resposta = requests.get(url, params=parametros)

    print("\n===", nome, "===")
    print("Status:", resposta.status_code)

    dados = resposta.json()

    if resposta.status_code == 200:
        print("Total retornado:", len(dados))

        for incidente in dados:
            print(
                incidente["titulo"],
                "|", incidente["severidade"],
                "|", incidente["status"],
                "|", incidente["criado_em"]
            )
    else:
        print("Resposta:", dados)


testar("Pagina 1 - tamanho 5", {
    "pagina": 1,
    "tamanho": 5
})

testar("Somente criticos", {
    "severidade": "critica"
})

testar("Tres abertos mais recentes", {
    "status": "aberto",
    "tamanho": 3
})

testar("Criticos e abertos", {
    "severidade": "critica",
    "status": "aberto"
})

testar("Pagina invalida", {
    "pagina": 0
})
