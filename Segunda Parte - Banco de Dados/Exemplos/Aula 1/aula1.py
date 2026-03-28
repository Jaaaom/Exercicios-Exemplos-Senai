import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("banco.db") # Conectando ao banco de dados
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Idade INTEGER
);

""")
    
    conn.commit()
    conn.close()