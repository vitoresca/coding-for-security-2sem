
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


X = np.array([
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [2, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [8, 1, 1, 1, 5],
    [12, 0, 1, 1, 8],
    [6, 1, 1, 1, 3],
    [10, 1, 1, 1, 6],
    [0, 0, 0, 0, 0],
    [15, 1, 1, 1, 9]
])


y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 1])


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

modelo.fit(X_train, y_train)


previsoes = modelo.predict(X_test)


print("=== Avaliacao do classificador ===")

print(f"Acuracia: {accuracy_score(y_test, previsoes):.2f}")
print(f"Precisao: {precision_score(y_test, previsoes, zero_division=0):.2f}")
print(f"Recall: {recall_score(y_test, previsoes, zero_division=0):.2f}")
print(f"F1-score: {f1_score(y_test, previsoes, zero_division=0):.2f}")

print("\n=== Relatorio de classificacao ===")
print(classification_report(y_test, previsoes, zero_division=0))


novo_email = np.array([[11, 1, 1, 1, 7]])

resultado = modelo.predict(novo_email)[0]

print("=== Teste de novo email ===")
print("Caracteristicas:", novo_email[0])

if resultado == 1:
    print("Resultado: Phishing")
else:
    print("Resultado: Legitimo")