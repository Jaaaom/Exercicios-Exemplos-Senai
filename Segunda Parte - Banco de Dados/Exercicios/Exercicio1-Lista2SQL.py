import sqlite3

# 1 - Abrindo o banco de dados
if __name__ == "__main__":
    conn = sqlite3.connect("biblioteca.db") # Conectando ao banco de dados
    cursor = conn.cursor()

# 2 - Criando a tabela dos Alunos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Livros(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo TEXT NOT NULL,
            Autor TEXT,
            Ano_publicacao INTEGER 
        );
""")

    conn.commit()

    opcao = int(input(" 1 - Inserir Livros , 2 - Consultar Livros: "))

    match opcao:

        case 1:
            titulo_do_livro = input("Insira o Título do Livro: ")
            autor_do_livro = (input("Insira o autor do Livro: "))
            ano_publi = int(input("Insira o ano de publicação do Livro:  "))
            cursor.execute("""
                INSERT INTO Livros(Titulo,Autor,Ano_publicacao)
                VALUES(?,?,?)   
            """, (titulo_do_livro,autor_do_livro,ano_publi))

            conn.commit()

        case 2:
            cursor.execute("""
                SELECT * FROM Livros
        """)
            print("Livros: ")
            livros = cursor.fetchall()
            for livro in livros:
                print(f"Título : {livro[1]} | Autor : {livro[2]} | Ano de Publicação : {livro[3]}")
            conn.commit()

        case _:
            print("Opção Inválida")