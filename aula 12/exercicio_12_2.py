
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV, StratifiedKFold


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


cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


modelos = {
    "RandomForest": Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(random_state=42))
    ]),

    "SVM": Pipeline([
        ("scaler", StandardScaler()),
        ("clf", SVC())
    ]),

    "KNN": Pipeline([
        ("scaler", StandardScaler()),
        ("clf", KNeighborsClassifier())
    ])
}

resultados = {}

print("=== Torneio de Algoritmos ===")


for nome, modelo in modelos.items():
    scores = cross_val_score(
        modelo, X, y, cv=cv, scoring="accuracy"
    )

    media = scores.mean()
    resultados[nome] = media

    print(f"{nome}: {media:.2f}")


maior_acuracia = max(resultados.values())

empatados = [
    nome for nome, media in resultados.items()
    if abs(media - maior_acuracia) < 0.000001
]

vencedor = empatados[0]

if len(empatados) > 1:
    print("\nEmpate entre:", ", ".join(empatados))
    print("Criterio de desempate: ordem dos modelos.")

print("\nVencedor:", vencedor)


grades = {
    "RandomForest": {
        "clf__n_estimators": [50, 100, 200],
        "clf__max_depth": [None, 5, 10]
    },

    "SVM": {
        "clf__C": [0.1, 1, 10],
        "clf__kernel": ["linear", "rbf"]
    },

    "KNN": {
        "clf__n_neighbors": [1, 3, 5]
    }
}


busca = GridSearchCV(
    modelos[vencedor],
    grades[vencedor],
    cv=cv,
    scoring="accuracy"
)

busca.fit(X, y)

print("\n=== GridSearchCV ===")
print("Modelo otimizado:", vencedor)
print("Melhores parametros:", busca.best_params_)
print(f"Melhor acuracia media: {busca.best_score_:.2f}")
