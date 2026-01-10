import sqlite3

def conectaDB():
    conexao = sqlite3.connect('EBD.db')
    return conexao

def inseredados(nome, data_nasc, classe):
    conexao = conectaDB()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO ALUNOS(nome, data_nasc, classe) VALUES(?, ?, ?)", (nome, data_nasc, classe))
    conexao.commit()
    conexao.close()

def listardados():
    conexao = conectaDB()
    cursor = conexao.cursor()
    cursor.execute("select * from Alunos")
    dados = cursor.fetchall()
    cursor.close()
    return dados