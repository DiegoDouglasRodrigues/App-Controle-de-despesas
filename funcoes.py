
import sqlite3 as lite
con = lite.connect('dados.bd')

# funcoes de inserir ----------------------------------------
def inserir_categoria(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cursor.execute(query, i)

def inserir_receita(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO Receitas (categoria, entrada, valor ) VALUES (?,?,?) "
        cursor.execute(query, i)

def inserir_gastos(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO Gastos (categoria, saida, quantidade, Obervacao ) VALUES (?,?,?,?) "
        cursor.execute(query, i)

#funcoes de deletar -----------------------------------------------

#deletar receitas
def deletar_categoria(i):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cursor.execute(query,i)


#deletar gastos
def deletar_gastos(i):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM gastos WHERE id=?"
        cursor.execute(query,i)

#deletar Receitas
def deletar_receitas(i):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cursor.execute(query,i)


#funcoes de mostrar -----------------------------------------------
    # Mostrar Categoria

def ver_categoria():
    lista_itens = []

    with con:
        cursor = con.cursor()
        cursor.execute ("SELECT * FROM Categoria")
        linhas = cursor.fetchall()
        for l in linhas:
            lista_itens.append(l)

    return lista_itens







# mostrar receitas
def ver_receitas():
    lista_itens = []

    with con:
        cursor = con.cursor()
        cursor.execute ("SELECT * FROM Receitas")
        linhas = cursor.fetchall()
        for l in linhas:
            lista_itens.append(l)

    return lista_itens


# mostrar Gastos
def ver_gastos():
    lista_itens = []

    with con:
        cursor = con.cursor()
        cursor.execute ("SELECT * FROM Gastos")
        linhas = cursor.fetchall()
        for l in linhas:
            lista_itens.append(l)

    return lista_itens



#porcentagem

def porcentagem_total():
    #receita total------------------------

    receitas = ver_receitas()
    receita_lista = []

    for i in ver_receitas():
        receita_lista.append(i[3])
    receita_total = sum(receita_lista)



    #despesa total-------------------------------
    despesa = ver_gastos()
    despesa_lista = []
    for i in ver_gastos():
        despesa_lista.append(i[3])
    despesa_total = sum(despesa_lista)


#porcentagem total
    total = ((receita_total - despesa_total) / receita_total) * 100

    return [total]