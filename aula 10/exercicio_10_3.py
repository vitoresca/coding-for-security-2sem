
import requests
import ipaddress
import time
from pathlib import Path

ips = [
    "8.8.8.8",
    "1.1.1.1",
    "185.220.101.1",
    "192.168.1.10",
    "8.8.8.8"
]


ips_suspeitos = {"185.220.101.1"}


cache = {}
consultas_http = 0
cache_hits = 0
internos = 0


redes_internas = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16")
]



def consultar_api(ip):
    global consultas_http

    url = f"https://ipinfo.io/{ip}/json"

    for tentativa in range(3):
        try:
            consultas_http += 1

            resposta = requests.get(url, timeout=10)

            if resposta.status_code == 429:
                if tentativa < 2:
                    espera = 2 ** tentativa
                    print(f"Rate limit: aguardando {espera}s...")
                    time.sleep(espera)
                    continue

                print("Limite de requisicoes atingido.")
                return None

            resposta.raise_for_status()
            return resposta.json()

        except requests.exceptions.Timeout:
            print(f"Timeout ao consultar {ip}")
            return None

        except requests.exceptions.RequestException:
            print(f"Erro ao consultar {ip}")
            return None

        except ValueError:
            print(f"Resposta JSON invalida para {ip}")
            return None

    return None



def enriquecer_ip(ip):
    global cache_hits, internos

    try:
        endereco = ipaddress.ip_address(ip)
    except ValueError:
        return f"{ip} -> IP invalido"

    
    if ip in cache:
        cache_hits += 1
        return f"{ip} -> [CACHE] {cache[ip]}"

   
    if any(endereco in rede for rede in redes_internas):
        internos += 1
        return f"{ip} -> Rede Interna (nao consultado)"

    
    if not endereco.is_global:
        return f"{ip} -> Endereco nao publico (nao consultado)"

    
    dados = consultar_api(ip)

    if dados is None:
        return f"{ip} -> Nao foi possivel obter informacoes"

    cidade = dados.get("city") or "Cidade nao informada"
    pais = dados.get("country") or "Pais nao informado"
    organizacao = dados.get("org") or "Organizacao nao informada"

    classificacao = "EXTERNO"

    if ip in ips_suspeitos:
        classificacao += ", suspeito (lista local)"

    informacoes = (
        f"{cidade} / {pais} / {organizacao} "
        f"({classificacao})"
    )

   
    cache[ip] = informacoes

    return f"{ip} -> {informacoes}"



linhas = []

print("=== Enriquecimento de IPs ===")

for ip in ips:
    linha = enriquecer_ip(ip)
    print(linha)
    linhas.append(linha)

resumo = (
    f"Consultas HTTP: {consultas_http} | "
    f"Cache hits: {cache_hits} | "
    f"Internos: {internos}"
)

print("\n=== Resumo ===")
print(resumo)

arquivo = Path(__file__).resolve().parent / "relatorio_10_3.txt"

with open(arquivo, "w", encoding="utf-8") as relatorio:
    relatorio.write("=== Enriquecimento de IPs ===\n")
    relatorio.write("\n".join(linhas))
    relatorio.write("\n\n=== Resumo ===\n")
    relatorio.write(resumo)

print("\nRelatorio salvo em:", arquivo.name)
