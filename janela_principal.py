from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
from tkinter import messagebox
from funcoes import inserir_categoria, inserir_receita, porcentagem_total, inserir_gastos, deletar_categoria, deletar_gastos, ver_categoria, ver_gastos, ver_receitas, ver_categoria
from funcoes import deletar_receitas
import babel.numbers


#importanto barra de progessp do tkinter
from tkinter.ttk import Progressbar
from tkcalendar import Calendar, DateEntry
from datetime import date

#importando matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

#definindo as cores..

cor0 = '#000000' #preto
cor1 = '#ffffff' #branco
cor2 = '#91b7bf' #azul framde de cima
cor3 = '#cadce0' # azul frame debaixo
cor4 = '#4e8a96' # azul faixa
cor5 = '#04d43c' #verde botao
cor6 = '#f04646' #vermelho botao
cor7 = '#d993ca' #rosa
cores = ['#4cb9d8', '#a31826', '#1e8a40', '#4e8a96', '#28c953', '#b5c959']
cor8 = '#d9d9d9' #cinza bg letras abas


janela = Tk()
janela.geometry("1500x1000")
janela.title('Controle de despesas')
janela.configure(bg=cor7)



logo = tk.PhotoImage(file="logo.png")
logo = logo.subsample(8, 8)

#criando frames
frame_cima = Frame(janela, height=100, width=2000, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, height=350, width=2000, bg=cor3, relief='raised', pady=10,)
frame_meio.grid(row=1, column=0, sticky=NSEW)

frame_debaixo = Frame(janela, height=580, width=2000, bg=cor2)
frame_debaixo.grid(row=2, column=0)

l_titulo = Label(frame_cima, text='Controle de despesas',font=('verdana 20 bold'), bg=cor2)
l_titulo.place(x=100, y=45)


#labels
l_logo = Label(frame_cima, image=logo)
l_logo.place(x=25, y=30)


#criando funcao inserir ---------------------------------
def nova_categoria_funcao():
    new_categoria = e_nova_categoria.get()
    lista_categoria = [new_categoria]


    for i in lista_categoria:
        if i == "":
            messagebox.showerror('Erro', 'Campo categoria esta vazio, verifique!')

        return

    inserir_categoria(lista_categoria)
    messagebox.showinfo('Sucesso', 'Nova categoria criada')

    e_nova_categoria.delete(0,'end')

    #atualizando lista combobox
    categorias_funcao = ver_categoria()

    categoria = []
    for i in categorias_funcao:
        categoria.append(i[1])

    #atualizando lista de categorias
    combo_categoria_despesa['values'] = categoria


def inserir_receitas_b():
    nome = 'RECEITA'
    entrada = e_data2.get()
    valor = e_valor.get()

    lista_receitas = [nome, entrada, valor]

    for i in lista_receitas:
        if i == "":
            messagebox.showerror('Erro', 'Existem campos vazios, verifique!')
            e_data2.delete(0, 'end')
            return

    inserir_receita(lista_receitas)

    messagebox.showinfo('Sucesso', 'Nova receita criada')

    e_data2.delete(0,'end')
    e_valor.delete(0,'end')

    #atualizando dados
    porcentagem()  #
    grafico_bar()  #
    resumo()  #
    grafico_pizza()  #
    tabela()



def inserir_despesas_b():
    categoria = combo_categoria_despesa.get()
    saida = e_data1.get()
    quantidade = e_valor1.get()
    obervacao = e_observacao.get()
    xxx = obervacao
    maisculo = xxx.upper()
    obervacao = maisculo

    lista_categorias = [categoria, saida, quantidade, obervacao]

    for i in lista_categorias:
        if i == "":
            messagebox.showerror('Erro', 'Existem campos vazios, verifique!')
            e_data2.delete(0, 'end')
            return
    inserir_gastos(lista_categorias)
    messagebox.showinfo('Sucesso', 'Nova despesa criada')

    combo_categoria_despesa.delete(0,'end')
    e_data1.delete(0,'end')
    e_valor1.delete(0,'end')
    e_observacao.delete(0,'end')

    #atualizando dados
    ver_categoria()
    grafico_pizza()  #
    tabela()
    porcentagem()  #
    grafico_bar()  #
    resumo()




#funcao grafico de barra ---------------------------------
def grafico_bar():
    #receita total------------------------

    receita = ver_receitas()
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



    saldo_total = receita_total - despesa_total


    #return [receita_total, despesa_total, saldo_total]

    lista_categorias2 = ["receita", "despesa", "saldo"]
    lista_valores = receita_total, despesa_total,saldo_total

#Codigo usado para o grafico de barra:
# faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5.5, 3.5), dpi=60)
    ax = figura.add_subplot(111)
    ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias2, lista_valores,  color=cores, width=0.8)
    # create a list to collect the plt.patches data

    c = 0
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=12, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias2, fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_meio)
    canva.get_tk_widget().place(x=32, y=100)

    l_linha1 = Label(frame_meio, text=" ", width=40, height=1, anchor=NW, font=('verdana 12'), bg=cor2 )
    l_linha1.place(x=390, y=90)

    l_linha2 = Label(frame_meio, text=" ", width=40, height=1, anchor=NW, font=('verdana 12'), bg=cor2 )
    l_linha2.place(x=390, y=160)

    l_linha3 = Label(frame_meio, text=" ", width=40, height=1, anchor=NW, font=('verdana 12'), bg=cor2 )
    l_linha3.place(x=390, y=230)

grafico_bar()

def porcentagem():
    # receita total------------------------
    receita = ver_receitas()
    receita_lista = []

    for i in ver_receitas():
        receita_lista.append(i[3])
        # print(receita_lista)  # ok numeros RECEITAS
    receita_total = sum(receita_lista)
    # print(receita_total)

    # despesa total-------------------------------
    despesa = ver_gastos()
    despesa_lista = []

    for i in ver_gastos():
        despesa_lista.append(i[3])
        # print(despesa_lista) #ok numeros GASTOS

    despesa_total = sum(despesa_lista)
    # print(despesa_total) #ok 6704
    saldo_total = receita_total - despesa_total


    l_porcentagem = Label(frame_meio, text='Porcentagem da Receita disponivel', font=('verdana 15'), bg=cor3)
    l_porcentagem.place(x=15, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('black.Horizontal.TProgressbar', bg=5)
    style.configure('TProgressbar', thickness=30)

    barra_progresso = Progressbar(frame_meio, length=200, style='black.Horizontal.TProgressbar')
    barra_progresso.place(x=20, y=50)

    barra_progresso['value'] = porcentagem_total()[0]
    #print(receita_total)

    #calculo = (receita_total - despesa_total) / receita_total *100
    #print(calculo)
    valor = porcentagem_total()[0]

    l_porcentual = Label(frame_meio, text="{:.2f}%".format(valor), font=('verdana 15 bold'), bg=cor3)
    l_porcentual.place(x=245, y=45)






# funcao resumo
def resumo():
    # receita total------------------------
    receita = ver_receitas()
    receita_lista = []

    for i in ver_receitas():
        receita_lista.append(i[3])
        # print(receita_lista)  # ok numeros RECEITAS
    receita_total = sum(receita_lista)
    # print(receita_total)

    # despesa total-------------------------------
    despesa = ver_gastos()
    despesa_lista = []

    for i in ver_gastos():
        despesa_lista.append(i[3])
        # print(despesa_lista) #ok numeros GASTOS

    despesa_total = sum(despesa_lista)
    # print(despesa_total) #ok 6704

    saldo_total = receita_total - despesa_total
    valor = [receita_total, despesa_total, saldo_total]
    #receita_total, despesa_total, saldo_total

    l_renda = Label(frame_meio, text='Renda total mensal R$ {:,.2f}               '.format(valor[0]),
                    font=('verdana 14'), bg=cor3)
    l_renda.place(x=385, y=80)

    l_despesas = Label(frame_meio,
                       text='Total de despesas mensais R$ {:,.2f}           '.format(valor[1]),
                       font=('verdana 14'), bg=cor3)
    l_despesas.place(x=385, y=150)

    l_caixa = Label(frame_meio, text='Total Saldo em Caixa R$ {:,.2f}               '.format(valor[2]),
                    font=('verdana 14'), bg=cor3)
    l_caixa.place(x=385, y=220)
# funcao grafico pizza
frame_gra_pie = Frame(frame_meio, width=600, height=300, bg=cor2)
frame_gra_pie.place(x=920, y=5)


# funcao grafico pie
def grafico_pizza():
    #receita total------------------------
    receita = ver_receitas()
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

    saldo_total = receita_total - despesa_total


     # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90, )
    ax = figura.add_subplot(111)

    lista_valores = [receita_total, despesa_total,saldo_total ]
    lista_categorias = ["receita", "despesa", "saldo"]

    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = []

    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=.5), autopct='%1.1f%%', colors=cores, shadow=True, startangle=90)
    ax.legend(lista_categorias, title ="Demostrativo", loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


l_tabela = Label(frame_debaixo, text='Tabela receitas e despesas', font=('verdana 18'), bg=cor2)
l_tabela.place(x=30, y=15)


#criando frame da tabela
frame_tabela = Frame(frame_debaixo, height=500, width=600, bg=cor1)
frame_tabela.grid(row=0, column=0)
frame_tabela.place(x=10,y=20)

def tabela():
    tabela_cabecalho = ['Id', 'categoria' , 'data' , 'quantidade' , 'Observacao' ]

    lista_itens = ver_gastos()
    lista2 = ver_receitas()

    global tree


    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=tabela_cabecalho, show='headings', height=20,)


    #Scrollbar verticar / orizontal
    vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview,)
    hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')


    hd = ["center", "center", "center", "center","center"]
    h = [40,100,100,100,100]
    n = 0

    for col in tabela_cabecalho:
        tree.heading(col, text=col.title(), anchor='center')
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

    for item in lista2:
        tree.insert('', 'end', values=item)

#funcao deletar ------------------
def deletar_despesas():
    try:
        msg = messagebox.askquestion('Aviso', 'deseja deletar despesa?')
        print(msg)
        if msg == "no":
            ver_categoria()
            porcentagem()  #
            grafico_bar()  #
            resumo()  #
            grafico_pizza()  #
            tabela()

        else:
            treeview_dados = tree.focus()
            treeview_dicionario = tree.item(treeview_dados)
            treeview_lista = treeview_dicionario['values']
            valor = treeview_lista[0]
            deletar_gastos([valor])

            ver_categoria()
            porcentagem()  #
            grafico_bar()  #
            resumo()  #
            grafico_pizza()  #
            tabela()

    except:
       messagebox.showerror('Erro', 'selecione um item na lista')


def deletar_receitas_b():
    try:
        msg = messagebox.askquestion('Aviso', 'deseja deletar receita?')
        print(msg)
        if msg == "no":
            ver_categoria()
            porcentagem()  #
            grafico_bar()  #
            resumo()  #
            grafico_pizza()  #
            tabela()

        else:
            treeview_dados = tree.focus()
            treeview_dicionario = tree.item(treeview_dados)
            treeview_lista = treeview_dicionario['values']
            valor = treeview_lista[0]
            deletar_receitas([valor])

            ver_categoria()
            porcentagem()  #
            grafico_bar()  #
            resumo()  #
            grafico_pizza()  #
            tabela()

    except:
       messagebox.showerror('Erro', 'selecione um item na lista')


#criando frame dos comandos aba 1 e aba 2
frame_despesas = Frame(frame_debaixo, height=430, width=800, bg=cor7)
frame_despesas.grid(row=0, column=1)
frame_despesas.place(x=510, y=20)
color = '#d993ca'
sky_color = "sky blue"
gold_color = "gold"
color_tab = "#ccdee0"

#configurabdo abas
tab_control = ttk.Notebook(frame_despesas)



aba1 = ttk.Frame(tab_control)
aba2 = ttk.Frame(tab_control)


tab_control.add(aba1, text='Despesas')
tab_control.add(aba2, text='Receitas')
tab_control.place(height=430, width=800)

#Aba 1 Despesas ------------------------------------------
l_despesas = Label(aba1, text= 'Inserir novas despesas', font=('verdana 14 '), bg=cor8)
l_despesas.place(x=15, y=10)

l_categoria = Label(aba1, text= 'Categoria:', font=('verdana 11 '), bg=cor8)
l_categoria.place(x=15, y=60)

l_categoria = Label(aba1, text= 'Data:', font=('verdana 11 '), bg=cor8)
l_categoria.place(x=15, y=90)

l_Valor = Label(aba1, text= 'Valor R$:', font=('verdana 11 '), bg=cor8)
l_Valor.place(x=15, y=120)
e_valor1 = Entry(aba1, width=22, justify='left', relief='solid')
e_valor1.place(x=115, y=120)

l_observacao = Label(aba1, text= 'Observacao:', font=('verdana 10'), bg=cor8)
l_observacao.place(x=15, y=160)


e_observacao = Entry(aba1, width=22, justify='left', relief='solid', font=('verdana 10 '))
e_observacao.place(x=115, y=160)




l_excluir = Label(aba1, text= 'Excluir lançamento:', font=('verdana 12 '), bg=cor8)
l_excluir.place(x=15, y=255)

bt1 = Button(aba1, text='Adicionar', command=inserir_despesas_b, font=('verdada 10 bold'), bg=cor5)
bt1.place(x=15, y=190)

bt2 = Button(aba1, text='Excluir', command=deletar_despesas, font=('verdada 10 bold'), bg=cor6)
bt2.place(x=180, y=255)




funcao_categoria = ver_categoria()

categoria = []

for i in funcao_categoria:
    categoria.append(i[1])

combo_categoria_despesa = ttk.Combobox(aba1, width=15, font=('verdana 10'))
combo_categoria_despesa['values'] = (categoria)
combo_categoria_despesa.place(x=115, y=60)



e_data1 = DateEntry(aba1,width=20, borderwith=2, locale='pt_br')
e_data1.place(x=115, y=90)

nova_categoria = Label(aba1, text= 'Nova categoria:', font=('verdana 10'), bg=cor2)
nova_categoria .place(x=15, y=300)
e_nova_categoria  = Entry(aba1, width=18, justify='left', relief='solid')
e_nova_categoria .place(x=135, y=300)




bt3 = Button(aba1, text='Adicionar', command=nova_categoria_funcao, font=('verdada 10 bold'), bg=cor5)
bt3.place(x=15, y=335)







def atualizar():
    ver_categoria()
    grafico_pizza()#
    tabela()
    porcentagem()  #
    grafico_bar()  #
    resumo()









#Aba 2  Receitas ------------------------------------------
l_despesas = Label(aba2, text= 'Inserir novas receitas', font=('verdana 14 '), bg=cor8)
l_despesas.place(x=15, y=10)

l_categoria = Label(aba2, text= 'Categoria:  Receitas', font=('verdana 11  bold'), bg=cor8)
l_categoria.place(x=15, y=60)

l_categoria = Label(aba2, text= 'Data:', font=('verdana 11 '), bg=cor8)
l_categoria.place(x=15, y=90)

l_Valor = Label(aba2, text= 'Valor R$:', font=('verdana 11 '), bg=cor8)
l_Valor.place(x=15, y=120)
e_valor = Entry(aba2, width=22, justify='left', relief='solid')
e_valor.place(x=115, y=120)


l_Valor = Label(aba2, text= 'Excluir lançamento:', font=('verdana 11 '), bg=cor8)
l_Valor.place(x=15, y=220)

bt1 = Button(aba2, text='Adicionar',  command=inserir_receitas_b, font=('verdada 10 bold'), bg=cor5)
bt1.place(x=15, y=160)

bt2 = Button(aba2, text='Excluir', command=deletar_receitas_b, font=('verdada 10 bold'), bg=cor6)
bt2.place(x=180, y=220)


e_data2 = DateEntry(aba2,width=20, borderwith=2, locale='pt_br')
e_data2.place(x=115, y=90)




ver_categoria()
grafico_pizza()#
tabela()
porcentagem() #
grafico_bar() #
resumo()











janela.mainloop()
