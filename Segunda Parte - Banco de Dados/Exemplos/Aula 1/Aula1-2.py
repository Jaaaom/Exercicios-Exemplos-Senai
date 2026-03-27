import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("banco2.db") # Conectando ao banco de dados
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Cliente(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Email TEXT
        );
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produto(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL, /* Força o texto não ser nulo*/
            Preco DECIMAL
        );
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pedido(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ClienteID INTEGER,
            ProdutoID INTEGER,
            Quantidade INTEGER,
            Data DATE,
            FOREIGN KEY (ClienteID) REFERENCES Cliente(ID),
            FOREIGN KEY (ProdutoID) REFERENCES Produto(ID)
        );
""")
    
    conn.commit()
    try:
        cursor.execute("""
            ALTER TABLE Cliente ADD Telefone INTEGER(11)
    """)
    
        conn.commit()
    except:
        pass
    
    cursor.execute("""

        SELECT Nome FROM Cliente

""")
    filtro = cursor.fetchall()
    for i in filtro:
        for j in i:
            if type(j) == type(str):
                if "@email.com" in j:
                    if not j== "Joana":               # Pode usar j!="Joana"
                        cursor.execute("""
                            INSERT INTO Cliente(Nome,Email) 
                            VALUES (?,?)
                        """, ("Joana","Joana@email.com"))

    conn.commit()

    cursor.execute("""
        INSERT INTO Produto(Nome,Preco) 
        VALUES (?,?)
""", ("Café", 8.50))
    
    conn.commit()

    cursor.execute("""
        INSERT INTO Pedido(ClienteID, ProdutoID, Quantidade, Data) 
        VALUES (?,?,?,?)
""", (1,10, 3, "25/03/2026"))
    
    conn.commit()

    cursor.execute("""
        UPDATE Cliente SET Email = "joana.silva@email.com" WHERE ID = 1
""")
    
    conn.commit()

    cursor.execute("""
        DELETE FROM Pedido WHERE ID = 1
""")
    
    conn.commit()

    cursor.execute("""
        SELECT * FROM Cliente LIMIT 10
""")
    
    print(cursor.fetchall())

    cursor.execute("""
        SELECT Nome FROM Produto WHERE preco > 10 ORDER BY Nome
""")
    
    print(cursor.fetchall())

    cursor.execute("""
        SELECT Cliente.Nome, Pedido.Data
        From Cliente
        INNER JOIN Pedido ON Cliente.ID == Pedido.ClienteID
""")
    
    print(cursor.fetchall())
    cursor.execute("""
        SELECT Produto.Nome, SUM(Pedido.Quantidade)
        FROM Produto
        INNER JOIN Pedido ON Produto.ID == Pedido.ProdutoID
        GROUP BY Produto.Nome   
""")
    
    print(cursor.fetchall())

    cursor.execute("""
        SELECT Produto.Nome, Pedido.Quantidade 
        FROM Pedido
        INNER JOIN Produto ON Produto.ID != Pedido.ProdutoID
        GROUP BY Produto.Nome
""")
    print(cursor.fetchall())

    conn.close()
    