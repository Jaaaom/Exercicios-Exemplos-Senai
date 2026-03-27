import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("escola.db") # Conectando ao banco de dados
    cursor = conn.cursor()

    