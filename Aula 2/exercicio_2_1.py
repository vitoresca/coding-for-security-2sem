
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
client.admin.command("ping")

db = client["seguranca"]
colecao = db["ativos"]

colecao.create_index("ip", unique=True)

ativos = [
    {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
    {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45", "status": "ativo"},
    {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1", "status": "inativo"}
]

if colecao.count_documents({}) == 0:
    colecao.insert_many(ativos)

while True:
    print("\n--- INVENTARIO DE ATIVOS ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar por IP")
    print("4 - Atualizar status")
    print("5 - Remover")
    print("6 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome: ")
        tipo = input("Tipo: ")
        ip = input("IP: ")
        status = input("Status: ")

        novo_ativo = {
            "nome": nome,
            "tipo": tipo,
            "ip": ip,
            "status": status
        }

        try:
            colecao.insert_one(novo_ativo)
            print("Ativo cadastrado!")
        except DuplicateKeyError:
            print("Erro: IP ja cadastrado!")

    elif opcao == "2":
        for ativo in colecao.find():
            print(ativo["nome"], ativo["ip"], ativo["tipo"], ativo["status"])

    elif opcao == "3":
        ip = input("Digite o IP: ")
        ativo = colecao.find_one({"ip": ip})

        if ativo:
            print(ativo)
        else:
            print("Ativo nao encontrado!")

    elif opcao == "4":
        ip = input("IP do ativo: ")
        novo_status = input("Novo status: ")

        resultado = colecao.update_one(
            {"ip": ip},
            {"$set": {"status": novo_status}}
        )

        if resultado.matched_count > 0:
            print("Status atualizado!")
        else:
            print("Ativo nao encontrado!")

    elif opcao == "5":
        ip = input("IP do ativo que deseja remover: ")
        resultado = colecao.delete_one({"ip": ip})

        if resultado.deleted_count > 0:
            print("Ativo removido!")
        else:
            print("Ativo nao encontrado!")

    elif opcao == "6":
        print("Encerrando programa...")
        break

    else:
        print("Opcao invalida!")

client.close()
