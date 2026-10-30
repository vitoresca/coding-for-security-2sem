
import mysql.connector
from getpass import getpass

# Conexao com o MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("Senha do MySQL: "),
    database="seguranca"
)

cursor = conexao.cursor(dictionary=True)


def buscar_inseguro(nome):
    consulta = "SELECT * FROM usuarios WHERE nome = '" + nome + "'"
    cursor.execute(consulta)
    return cursor.fetchall()



def buscar_seguro(nome):
    consulta = "SELECT * FROM usuarios WHERE nome = %s"
    cursor.execute(consulta, (nome,))
    return cursor.fetchall()


entrada_maliciosa = "' OR '1'='1"


resultado_inseguro = buscar_inseguro(entrada_maliciosa)

print("[INSEGURO]")
print("Entrada:", entrada_maliciosa)
print("Usuarios retornados:", len(resultado_inseguro))

for usuario in resultado_inseguro:
    print(usuario["nome"], "|", usuario["email"])



resultado_seguro = buscar_seguro(entrada_maliciosa)

print("\n[SEGURO]")
print("Entrada:", entrada_maliciosa)
print("Usuarios retornados:", len(resultado_seguro))

print("\nConclusao:")
print("A consulta parametrizada tratou a entrada como texto literal.")

cursor.close()
conexao.close()
