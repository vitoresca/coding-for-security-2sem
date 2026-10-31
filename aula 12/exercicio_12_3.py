
import numpy as np
import joblib
import hashlib

from pathlib import Path
from sklearn.ensemble import RandomForestClassifier

X = np.array([
    [500, 80, 0.1],
    [1200, 80, 0.5],
    [64, 22, 0.02],
    [64000, 4444, 10.0],
    [45000, 8080, 15.0],
    [60000, 31337, 20.0],
    [800, 443, 0.3],
    [300, 53, 0.05],
    [55000, 9999, 18.0],
    [200, 25, 0.2],
    [700, 443, 0.2],
    [52000, 6666, 17.0],
    [150, 53, 0.03],
    [58000, 4444, 19.0],
    [900, 80, 0.4]
])


y = np.array([0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0])


pasta = Path(__file__).resolve().parent
arquivo_modelo = pasta / "modelo_seguranca.pkl"
arquivo_hash = pasta / "modelo_seguranca.sha256"


def calcular_hash(caminho):
    sha256 = hashlib.sha256()

    with open(caminho, "rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b""):
            sha256.update(bloco)

    return sha256.hexdigest()



modelo = RandomForestClassifier(
    n_estimators=50,
    max_depth=None,
    random_state=42
)

modelo.fit(X, y)


joblib.dump(modelo, arquivo_modelo)

print("Modelo salvo:", arquivo_modelo.name)


hash_original = calcular_hash(arquivo_modelo)

print("Hash SHA-256:", hash_original)

with open(arquivo_hash, "w", encoding="utf-8") as arquivo:
    arquivo.write(hash_original)

print("Hash salvo:", arquivo_hash.name)


print("\nRecarregando e verificando integridade...")

hash_atual = calcular_hash(arquivo_modelo)

with open(arquivo_hash, "r", encoding="utf-8") as arquivo:
    hash_esperado = arquivo.read().strip()

if hash_atual != hash_esperado:
    print("ALERTA: arquivo do modelo foi modificado!")
else:
    print("Hash confere: modelo integro.")

    
    modelo_carregado = joblib.load(arquivo_modelo)

  
    novo_trafego = np.array([[58000, 4444, 16.0]])

    previsao = modelo_carregado.predict(novo_trafego)

    print("Previsao de teste:", previsao)
