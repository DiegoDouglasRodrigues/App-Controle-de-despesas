import sqlite3 as lite

con = lite.connect('dados.bd')

#criando a tabela categoria
with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE Categoria (id INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT)")


#criando a tabela receitas
with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE Receitas (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, entrada DATE, valor DECIMAL )")


#criando a tabela gastos
with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE Gastos (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, saida DATE, quantidade DECIMAL, Obervacao TEXT )")