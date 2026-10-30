from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


y_verdadeiro = [0,0,0,0,0,0,0,0,1,1]
y_previsto = [0,0,0,0,0,0,0,0,0,1]


matriz = confusion_matrix(y_verdadeiro, y_previsto)


acuracia = accuracy_score(y_verdadeiro, y_previsto)
precisao = precision_score(y_verdadeiro, y_previsto)
recall = recall_score(y_verdadeiro, y_previsto)
f1 = f1_score(y_verdadeiro, y_previsto)

print("=== Matriz de confusao ===")
print(matriz)

print("\n=== Metricas do modelo ===")
print(f"Acuracia: {acuracia:.2f}")
print(f"Precisao: {precisao:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")

print("\n=== Interpretacao ===")
print("A acuracia de 90% parece boa, mas esconde um problema importante.")
print("O recall de 50% mostra que o modelo deixou passar metade dos ataques.")
print("Em um SOC, ataques nao identificados podem comprometer a seguranca.")