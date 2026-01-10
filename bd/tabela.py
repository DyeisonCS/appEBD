import sqlite3

conexao = sqlite3.connect('EBD.db')
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE Alunos(
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            DATA_NASC TEXT NOT NULL,
            CLASSE TEXT NOT NULL
        );
    """
)
cursor.close()
