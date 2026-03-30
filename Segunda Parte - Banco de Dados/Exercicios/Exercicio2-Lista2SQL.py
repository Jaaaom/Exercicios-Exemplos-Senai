import sqlite3

# 1 - Abrindo o banco de dados
if __name__ == "__main__":
    conn = sqlite3.connect("loja.db") # Conectando ao banco de dados
    cursor = conn.cursor()

# 2 - Criando a tabela dos Alunos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Produto TEXT NOT NULL,
            Preco DECIMAL
        );
""")

    conn.commit()

    opcao = int(input(" 1 - Inserir Produtos , 2 - Alterar Preço , 3 - Consulta dos Produtos: "))

    match opcao:
        case 1:
            produto = input("Insira o nome do Produto: ")
            preco = float(input("Qual o valor do Produto? "))
            cursor.execute("""
                INSERT INTO Produtos(Produto,Preco)
                VALUES(?,?)   
            """, (produto, preco))

            conn.commit()

        case 2:
            produto = input("Qual o produto que quer atualizar o preço? ")
            novo_preco = float(input("Insira o valor atualizado do Produto"))
            cursor.execute("""
                UPDATE Produtos SET Preco = ? WHERE Produto == ?
        """, (novo_preco, produto))
            
            conn.commit()

        case 3:
            cursor.execute("""
                SELECT * FROM Produtos
        """)
            print("Produtos: ")
            prods = cursor.fetchall()
            for produto in prods:
                print(f"ID : {produto[0]} | Produto : {produto[1]} | Preço : R${produto[2]}")
            conn.commit()

        case _:
            print("Opção Inválida")

        