import sqlite3

# 1 - Abrindo o banco de dados
if __name__ == "__main__":
    conn = sqlite3.connect("clientes.db") # Conectando ao banco de dados
    cursor = conn.cursor()

# 2 - Criando a tabela dos Alunos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Email TEXT,
            Ativo INTEGER
        );
""")

    conn.commit()

    opcao = int(input(" 1 - Inserir Cliente, 2 - Listar Clientes , 3 - Remover os Inativos: "))

    match opcao:
        case 1:
            nome_cliente = input("Nome do Cliente: ")
            email_cliente = input("Email do Cliente: ")

            j=0
            while j==0:
                status = int(input("Ativo = 1 , Inativo = 0: "))
                if status != 0 and status != 1:
                    print("Status Inválido!!!!")
                    continue
                else:
                    j=1

            cursor.execute("""
                INSERT INTO Clientes(Nome, Email, Ativo) VALUES (?,?,?)
            """,(nome_cliente, email_cliente, status))

            conn.commit()

        case 2:
            cursor.execute("""
                SELECT * FROM Clientes
        """)
            print("Clientes: ")
            clientes = cursor.fetchall()
            for cliente in clientes:
                print(f"ID : {cliente[0]} | Cliente : {cliente[1]} | Email : {cliente[2]} | Ativo : {cliente[3]}")

            conn.commit()

        case 3:
            cursor.execute(f"""
                DELETE FROM Clientes WHERE Ativo = {0}
        """)
            
            conn.commit()

        case _:
            print("Opção Inválida")