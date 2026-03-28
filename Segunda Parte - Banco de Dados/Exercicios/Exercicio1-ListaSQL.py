import sqlite3

# 1 - Abrindo o banco de dados
if __name__ == "__main__":
    conn = sqlite3.connect("escola.db") # Conectando ao banco de dados
    cursor = conn.cursor()

# 2 - Criando a tabela dos Alunos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alunos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Idade INTEGER,
            Curso TEXT 
        );
""")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Notas(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            AlunoID INTEGER NOT NULL,
            Notas INTEGER,
            Disciplina TEXT 
        );
""")
    
    conn.commit()

    decisao = int(input("Adicionar - 1, Consulta - 2, Alunos por Curso - 3, Atualizar Idade - 4, Remover Aluno - 5 " \
            ",Alunos com idade Maior que 20 - 6 , Alunos que comecem com a Letra A - 7 , Três alunos mais jovens - 8" \
            " Alunos em ordem decrescente pelo nome - 9 , Inserir Notas - 10, Consulta Completa (Aluno, Disciplina e Nota) - 11:  "))

    match decisao:
        case 1:
#                                       3 - Criando Registros para a Tabela
            chave_do_aluno = int(input("Insira o ID do Aluno: "))
            nome_do_aluno = input("Insira o nome do Aluno: ")
            idade_do_aluno = int(input("Insira a idade do Aluno: "))
            curso_do_aluno = input("Insira o curso do Aluno: ")
            cursor.execute("""
                INSERT INTO Alunos(ID,Nome,Idade,Curso)
                VALUES(?,?,?,?)   
            """, (chave_do_aluno, nome_do_aluno, idade_do_aluno, curso_do_aluno))

            conn.commit()

        case 2:
#                                         Recuperando os dados da Tabela
            cursor.execute("""
                SELECT * FROM Alunos
        """)
            print("Nome dos Alunos: ")
            alunos = cursor.fetchall()
            for aluno in alunos:
                print(f"Nome {aluno[1]} | Idade : {aluno[2]} | Curso : {aluno[3]}")
            conn.commit()

        case 3:
#                                        Recupera todos os alunos de Engenharia Civil
            cursor.execute("""
                SELECT Nome FROM Alunos WHERE Curso == 'Engenharia Civil' ORDER BY Nome;

        """)
            print("Nome dos Alunos que fazem Engenharia Civil ")
            filtro = cursor.fetchall()
            print(filtro)
            conn.commit()

        case 4:
#                                        Atualizando as idades
            chave_do_aluno = int(input("Insira o ID do Aluno que deseja atualizar a idade: "))
            idade_do_aluno = int(input("Insira a idade do Aluno: "))
            cursor.execute("""
                UPDATE Alunos SET Idade = ? WHERE ID == ?
        """, (idade_do_aluno, chave_do_aluno))
            
            conn.commit()

        case 5:
#                                         Removendo alunos por ID            
            chave_do_aluno = int(input("Insira o ID do Aluno que deseja deletar: "))
            cursor.execute(f"""
                DELETE FROM Alunos WHERE ID = {chave_do_aluno}
        """)
            
            conn.commit()

        case 6:
#                                        Listando Alunos com idade maior que 20
            cursor.execute("""
                SELECT Nome FROM Alunos WHERE Idade > 20 ORDER BY Nome
        """)
            print("Nome dos Alunos com idade maior que 20 ")
            filtro = cursor.fetchall()
            print(filtro)
            conn.commit()

        case 7:
#                                       Alunos que começam com a Letra A
            cursor.execute("""
                SELECT Nome FROM Alunos WHERE Nome LIKE 'A%' ORDER BY Nome
        """)
            print("Nome dos Alunos com o nome começando com a Letra A")
            filtro = cursor.fetchall()
            print(filtro)
            conn.commit() 
        case 8:
#                                       Três alunos mais jovens
            cursor.execute("""
                SELECT Nome, Idade FROM Alunos ORDER BY Idade LIMIT 3
        """)
            print("Nome dos Alunos com o nome começando com a Letra A")
            filtro = cursor.fetchall()
            print(filtro)
            conn.commit() 
        case 9:
#                                       Listando Alunos em ordem alfabética decrescente
            cursor.execute("""
                SELECT Nome, Idade FROM Alunos ORDER BY Nome DESC
        """)
            print("Nome dos Alunos com o nome começando com a Letra A")
            filtro = cursor.fetchall()
            print(filtro)
            conn.commit()
            
        case 10:
#                                       Inserindo as notas
            alunoid = input("Aluno ID: ")
            nota = int(input("Nota: "))
            disciplina = input("Disciplina: ")
            cursor.execute("""
                INSERT INTO Notas (AlunoID, Nota, Disciplina) VALUES (?,?,?)
        """, (alunoid, nota, disciplina))
            conn.commit()

        case 11:
#                                       Consulta Completa
            cursor.execute("""
                SELECT Alunos.Nome, Notas.Disciplina, Notas.Nota
                FROM Alunos
                INNER JOIN Notas ON Alunos.ID == Notas.AlunoID
        """)
            
            alunos = cursor.fetchall()

            for aluno in alunos:
                print(f"Nome: {aluno[0]} | Nota: {aluno[2]} | Disciplina {aluno[1]}")
        case _:
            print(" Opção Inválida!!!!!")

