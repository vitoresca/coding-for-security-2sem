
import requests

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def consultar_cve(cve_id):
    try:
        resposta = requests.get(
            url,
            params={"cveId": cve_id},
            timeout=30
        )

        
        if resposta.status_code == 404:
            print("CVE nao encontrada")
            return

       
        if resposta.status_code in (403, 429):
            print("API indisponivel ou limite de consultas atingido")
            return

        resposta.raise_for_status()

        dados = resposta.json()
        vulnerabilidades = dados.get("vulnerabilities", [])

        if not vulnerabilidades:
            print("CVE nao encontrada")
            return

        cve = vulnerabilidades[0]["cve"]

      
        descricao = "Descricao nao disponivel"

        for item in cve.get("descriptions", []):
            if item["lang"] == "en":
                descricao = item["value"]
                break

      
        metricas = cve.get("metrics", {})
        cvss = None

        for versao in (
            "cvssMetricV40",
            "cvssMetricV31",
            "cvssMetricV30",
            "cvssMetricV2"
        ):
            if metricas.get(versao):
                cvss = metricas[versao][0]
                break

        print("\n===", cve["id"], "===")

        if cvss:
            score = cvss["cvssData"]["baseScore"]
            severidade = cvss["cvssData"].get(
                "baseSeverity",
                cvss.get("baseSeverity", "Nao informada")
            )

            print(f"CVSS: {score} ({severidade})")
        else:
            print("CVSS: nao disponivel")

        print("Descricao:", descricao)

    except requests.exceptions.Timeout:
        print("Erro: tempo limite da consulta excedido")

    except requests.exceptions.RequestException:
        print("Erro ao consultar a API do NVD")

    except ValueError:
        print("Erro ao interpretar a resposta da API")



consultar_cve("CVE-2021-44228")


consultar_cve("CVE-2099-99999")
