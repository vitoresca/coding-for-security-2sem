import requests

url = "http://127.0.0.1:5000/api/checar-ip/"

r = requests.get(url + "185.220.101.1")
print("=== Teste 1 - IP na blacklist ===")
print("Status:", r.status_code)
print("Resposta:", r.json())

r = requests.get(url + "192.168.1.10")
print("\n=== Teste 2 - IP privado ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.get(url + "999.999.1.1")
print("\n=== Teste 3 - IP invalido ===")
print("Status:", r.status_code)
print("Resposta:", r.json())


r = requests.get(url + "45.33.32.156")
print("\n=== Teste 4 - Outro IP da blacklist ===")
print("Status:", r.status_code)
print("Resposta:", r.json())

