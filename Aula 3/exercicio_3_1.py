
import mysql.connector
from mysql.connector import Error, IntegrityError
from getpass import getpass

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Senha do MySQL: "),
        database="seguranca"
    )

    cursor = conexao.cursor(dictionary=True)

   
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(150) NOT NULL UNIQUE,
            nivel_acesso INT NOT NULL,
            CHECK (nivel_acesso BETWEEN 1 AND 5)
        )
    """)

    usuarios = [
        ("Carlos Silva", "carlos@empresa.com", 3),
        ("Ana Costa", "ana@empresa.com", 5),
        ("Bruno Lima", "bruno@empresa.com", 1)
    ]

   
    cursor.executemany(
        """INSERT IGNORE INTO usuarios
           (nome, email, nivel_acesso)
           VALUES (%s, %s, %s)""",
        usuarios
    )
    conexao.commit()

    while True:
        print("\n--- GERENCIAMENTO DE USUARIOS ---")
        print("1 - Cadastrar usuario")
        print("2 - Listar usuarios")
        print("3 - Buscar por email")
        print("4 - Alterar nivel de acesso")
        print("5 - Remover usuario")
        print("6 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")

            try:
                nivel = int(input("Nivel de acesso (1 a 5): "))

                if nivel < 1 or nivel > 5:
                    print("Erro: nivel deve ser entre 1 e 5!")
                    continue

                cursor.execute(
                    """INSERT INTO usuarios
                       (nome, email, nivel_acesso)
                       VALUES (%s, %s, %s)""",
                    (nome, email, nivel)
                )
                conexao.commit()
                print("Usuario cadastrado!")

            except ValueError:
                print("Erro: digite um numero de 1 a 5!")

            except IntegrityError:
                conexao.rollback()
                print("Erro: email ja existe!")

        elif opcao == "2":
            cursor.execute(
                "SELECT nome, email, nivel_acesso FROM usuarios ORDER BY id"
            )

            for usuario in cursor.fetchall():
                print(
                    f"{usuario['nome']} | "
                    f"{usuario['email']} | "
                    f"nivel {usuario['nivel_acesso']}"
                )

        elif opcao == "3":
            email = input("Email para buscar: ")

            cursor.execute(
                "SELECT * FROM usuarios WHERE email = %s",
                (email,)
            )

            usuario = cursor.fetchone()

            if usuario:
                print(
                    f"{usuario['nome']} | "
                    f"{usuario['email']} | "
                    f"nivel {usuario['nivel_acesso']}"
                )
            else:
                print("Usuario nao encontrado!")

        elif opcao == "4":
            email = input("Email do usuario: ")

            try:
                nivel = int(input("Novo nivel (1 a 5): "))

                if nivel < 1 or nivel > 5:
                    print("Erro: nivel deve ser entre 1 e 5!")
                    continue

                cursor.execute(
                    """UPDATE usuarios
                       SET nivel_acesso = %s
                       WHERE email = %s""",
                    (nivel, email)
                )
                conexao.commit()

                if cursor.rowcount > 0:
                    print("Nivel atualizado!")
                else:
                    print("Usuario nao encontrado ou nivel ja estava igual!")

            except ValueError:
                print("Erro: digite um numero de 1 a 5!")

        elif opcao == "5":
            email = input("Email do usuario para remover: ")

            cursor.execute(
                "DELETE FROM usuarios WHERE email = %s",
                (email,)
            )
            conexao.commit()

            if cursor.rowcount > 0:
                print("Usuario removido!")
            else:
                print("Usuario nao encontrado!")

        elif opcao == "6":
            print("Encerrando programa...")
            break

        else:
            print("Opcao invalida!")

except Error as erro:
    print(f"Erro no MySQL: {erro}")

finally:
    if "conexao" in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
