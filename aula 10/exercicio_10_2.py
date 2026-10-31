
import requests
import json
from urllib.parse import quote

URL = "https://api.github.com"
HEADERS = {"Accept": "application/vnd.github+json"}

usuario_atual = ""
resultados = {}



def consultar_api(endpoint, parametros=None):
    try:
        resposta = requests.get(
            URL + endpoint,
            headers=HEADERS,
            params=parametros,
            timeout=15
        )

        if resposta.status_code == 404:
            print("Usuario ou repositorio nao encontrado!")
            return None

        if resposta.status_code in (403, 429):
            print("Limite de requisicoes atingido ou acesso negado!")
            return None

        resposta.raise_for_status()
        return resposta.json()

    except requests.exceptions.Timeout:
        print("Erro: tempo limite da consulta excedido!")

    except requests.exceptions.RequestException:
        print("Erro de conexao com a API do GitHub!")

    except ValueError:
        print("Erro ao interpretar a resposta JSON!")

    return None



def buscar_usuario(usuario):
    dados = consultar_api("/users/" + quote(usuario, safe=""))

    if dados is None:
        return None

    print("\n=== Perfil:", usuario, "===")
    print("Nome:", dados.get("name") or usuario)
    print("Repos publicos:", dados.get("public_repos"))
    print("Seguidores:", dados.get("followers"))

    return dados



def listar_repositorios(usuario):
    repositorios = []
    pagina = 1

    while True:
        lote = consultar_api(
            "/users/" + quote(usuario, safe="") + "/repos",
            {"page": pagina, "per_page": 30}
        )

        if lote is None:
            return None

        if not lote:
            break

        repositorios.extend(lote)

        if len(lote) < 30:
            break

        pagina += 1

    print("\n=== Repositorios de", usuario, "===")

    for i, repo in enumerate(repositorios, 1):
        print(
            f"{i}. {repo['name']} "
            f"| Estrelas: {repo['stargazers_count']} "
            f"| Linguagem: {repo.get('language') or 'Nao informada'}"
        )

    print("Total:", len(repositorios))

    return repositorios



def detalhar_repositorio(usuario, nome_repo):
    endpoint = (
        "/repos/" + quote(usuario, safe="")
        + "/" + quote(nome_repo, safe="")
    )

    repo = consultar_api(endpoint)

    if repo is None:
        return None

    print("\n=== Detalhes do repositorio ===")
    print("Nome:", repo["name"])
    print("Descricao:", repo.get("description") or "Sem descricao")
    print("Linguagem:", repo.get("language") or "Nao informada")
    print("Estrelas:", repo["stargazers_count"])
    print("Forks:", repo["forks_count"])
    print("URL:", repo["html_url"])

    return repo



def salvar_json(usuario):
    if not resultados:
        print("Nenhum resultado para salvar!")
        return

    nome_arquivo = "github_" + usuario + ".json"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(resultados, arquivo, indent=4, ensure_ascii=False)

    print("Resultados salvos em", nome_arquivo)



while True:
    print("\n=== EXPLORADOR DA API DO GITHUB ===")
    print("1 - Buscar usuario")
    print("2 - Listar repositorios")
    print("3 - Detalhar repositorio")
    print("4 - Salvar resultados em JSON")
    print("5 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        usuario = input("Usuario do GitHub: ").strip()

        if not usuario:
            print("Informe um usuario!")
            continue

        perfil = buscar_usuario(usuario)

        if perfil is not None:
            usuario_atual = usuario
            resultados = {"perfil": perfil}

    elif opcao == "2":
        if not usuario_atual:
            print("Primeiro busque um usuario na opcao 1!")
            continue

        repos = listar_repositorios(usuario_atual)

        if repos is not None:
            resultados["repositorios"] = repos

    elif opcao == "3":
        if not usuario_atual:
            print("Primeiro busque um usuario na opcao 1!")
            continue

        nome_repo = input("Nome do repositorio: ").strip()

        if not nome_repo:
            print("Informe o repositorio!")
            continue

        repo = detalhar_repositorio(usuario_atual, nome_repo)

        if repo is not None:
            resultados["detalhes"] = repo

    elif opcao == "4":
        if usuario_atual:
            salvar_json(usuario_atual)
        else:
            print("Primeiro busque um usuario!")

    elif opcao == "5":
        print("Encerrando programa...")
        break

    else:
        print("Opcao invalida!")
