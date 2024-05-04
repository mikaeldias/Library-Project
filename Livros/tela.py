
from tkinter .ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from tkinter import messagebox

# importando as funcoes da view
from view_02 import *


co0 = '#2e2d2b' # preta
co1 = '#feffff' # branca
co2 = '#4fa882' # verde
co3 = '#38576b' # valor
co4 = '#403d3d' # letra
co5 = '#e06636' # profit
co6 = '#E9A178' # 
co7 = '#3fbfb9' # verde
co8 = '#263238' # + verde
co9 = '#e9edf5' # + verde
co10 = '6e8faf' # 
co11 = '#f2f4f2' 

# criando janela
janela = Tk()
janela.title('')
janela.geometry('770x330')
janela.configure(bg = co1)
janela.resizable(width= FALSE, height= FALSE)

style = Style(janela)
style.theme_use('clam')

# Frames
frameCima = Frame(janela, width = 770, height = 50, bg = co6, relief = 'flat' )
frameCima.grid(row = 0, column = 0, columnspan = 2, sticky = NSEW )

frameEsquerda = Frame(janela, width = 150, height = 265, bg = co4, relief = 'solid' )
frameEsquerda.grid(row = 1, column = 0, sticky = NSEW )

frameDireita = Frame(janela, width = 600, height = 265, bg = co1, relief = 'raised' )
frameDireita.grid(row = 1, column = 1, sticky = NSEW )

# LOGO
# abrindo a imagem
app_img = Image.open('logo_livros_sistema.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image= app_img, width= 1000, compound= LEFT, padx= 5, anchor= NW, bg=co6, fg= co1)
app_logo.place(x= 5, y=0) # imagem canto superior esquerdo

app_logo = Label(frameCima, text= 'Sistema de Gerenciamento de Livros',compound= LEFT, padx= 5, anchor= NW, font= ('Verdana 15 bold'),bg=co6, fg= co1)
app_logo.place(x= 50, y=7) # texto 

app_linha = Label(frameCima, width= 770, height= 1 , padx= 5, anchor= NW, font= ('Verdana 15 bold'),bg=co3, fg= co1)
app_linha.place(x= 0, y=47) # linha azul abaixo do texto

# novo usuario
def novo_usuario():
        
        global img_salvar

        def add():
             first_name = e_p_nome.get()
             last_name = e_sobrenome.get()
             address = e_endereco.get()
             email = e_email.get()
             phone = e_numero.get()

             lista = [first_name, last_name, address, email, phone]

             # verificando caso algum campo esteja vazio
             for i in lista:
                  if i == '':
                        messagebox.showerror('Erro:', 'Preencha todos os campos')
                        return
                  
                  # inserindo os dados no banco de dados
                  insert_user(first_name, last_name, address, email, phone)

                  messagebox.showinfo('Sucesso', 'Usuário registrado com sucesso')

                  # limpados os campos de entrada
                  e_p_nome.delete(0, END)
                  e_sobrenome.delete(0, END)
                  e_endereco.delete(0, END)
                  e_email.delete(0, END)
                  e_numero.delete(0, END)

                  

        app_ = Label(frameDireita, text= 'Inserir um novo usuário', width= 50, compound= LEFT, padx= 5, pady= 10, font= 'Verdana 12', bg= co1, fg= co4)
        app_.grid(row= 0, column= 0, columnspan= 5, sticky= NSEW)

        app_linha = Label(frameDireita, width= 505, height= 1 , anchor= NW, font= ('Verdana 1'),bg=co3, fg= co1)
        app_linha.grid(row= 1, column= 0, columnspan= 4, sticky= NSEW)

        # label primeiro nome e entrada primeiro nome
        l_p_nome = Label(frameDireita, text= 'Primeiro nome*', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
        l_p_nome.grid(row= 2, column= 0, padx= 5, pady= 5, sticky= NSEW)
        e_p_nome = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
        e_p_nome.grid(row= 2, column= 1, padx= 5, pady= 5, sticky= NSEW)

        # label sobrenome e entrada sobrenome
        l_sobrenome = Label(frameDireita, text= 'Sobrenome*', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
        l_sobrenome.grid(row= 3, column= 0, padx= 5, pady= 5, sticky= NSEW)
        e_sobrenome = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
        e_sobrenome.grid(row= 3, column= 1, padx= 5, pady= 5, sticky= NSEW)
        
        # label e entrada endereco
        l_endereco = Label(frameDireita, text= 'Endereço do usuário*', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
        l_endereco.grid(row= 4, column= 0, padx= 5, pady= 5, sticky= NSEW)
        e_endereco = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
        e_endereco.grid(row= 4, column= 1, padx= 5, pady= 5, sticky= NSEW)

        # label e entrada email
        l_email = Label(frameDireita, text= 'Email do usuário', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
        l_email.grid(row= 5, column= 0, padx= 5, pady= 5, sticky= NSEW)
        e_email = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
        e_email.grid(row= 5, column= 1, padx= 5, pady= 5, sticky= NSEW)

        # label e entrada numero
        l_numero = Label(frameDireita, text= 'Número de telefone', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
        l_numero.grid(row= 6, column= 0, padx= 5, pady= 5, sticky= NSEW)
        e_numero = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
        e_numero.grid(row= 6, column= 1, padx= 5, pady= 5, sticky= NSEW)

        # botao salvar
        img_salvar = Image.open('salvar.png')
        img_salvar = img_salvar.resize((18,18))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command= add, image= img_salvar, compound= LEFT, width= 100,  anchor= NW, text= '  Salvar', bg= co1, fg= co4, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
        b_salvar.grid(row= 7, column= 1, pady= 5, sticky= NSEW)

def ver_usuarios():
        

        app_ = Label(frameDireita, text= 'Inserir um novo usuário', width= 50, compound= LEFT, padx= 5, pady= 10, font= 'Verdana 12', bg= co1, fg= co4)
        app_.grid(row= 0, column= 0, columnspan= 5, sticky= NSEW)
        app_linha = Label(frameDireita, width= 505, height= 1 , anchor= NW, font= ('Verdana 1'),bg=co3, fg= co1)
        app_linha.grid(row= 1, column= 0, columnspan= 4, sticky= NSEW)

        dados = get_users()
        
        # creating a treeview with dual scrollbars
        list_header = [ 'ID', 'Nome', 'Sobrenome', 'Endereço', 'Email', 'Telefone']

        global tree

        tree = ttk.Treeview(frameDireita, selectmode= 'extended', columns= list_header, show= 'headings')

        # vertical scrollbar
        vsb = ttk.Scrollbar(frameDireita, orient= 'vertical', command= tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(frameDireita, orient= 'horizontal', command= tree.xview)

        tree.configure(yscrollcommand= vsb.set, xscrollcommand= hsb.set)

        tree.grid(column= 0, row= 2, sticky= 'nsew')
        vsb.grid(column= 1, row= 2, sticky= 'ns')
        hsb.grid(column= 0, row= 3, sticky= 'ew')
        frameDireita.grid_rowconfigure(0, weight= 12)

        hd = ['nw', 'nw', 'nw','nw', 'nw', 'nw']
        h = [20 , 80, 80, 120, 76, 100]
        n = 0

        for col in list_header:
            tree.heading(col, text= col, anchor= 'nw')
            # adjust the column's width to the header string
            tree.column(col, width= h[n], anchor= hd[n])

            n+= 1
        
        for item in dados:
            tree.insert('', 'end', values= item)



# função para controlar o menu
def control(i):      
    # novo usuario
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        
        # chamando a funcao novo usuario
        novo_usuario()


    # ver usuarios
    if i == 'ver_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        
        # chamando a funcao novo usuario
        ver_usuarios()

#  Menu

# Novo usuario
img_usuario = Image.open('novo_usuario.png')
img_usuario = img_usuario.resize((18,18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, command= lambda: control ('novo_usuario') ,image= img_usuario, compound= LEFT, anchor= NW, text= '  Novo usuário', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_usuario.grid(row= 0, column= 0, sticky= NSEW, padx= 5, pady= 6)

# Novo livro
img_novo_livro = Image.open('novo_usuario.png')
img_novo_livro = img_novo_livro.resize((18,18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda, image= img_novo_livro, compound= LEFT, anchor= NW, text= '  Novo livro', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_novo_livro.grid(row= 1, column= 0, sticky= NSEW, padx= 5, pady= 6)

# ver livros
img_ver_livro = Image.open('logo_livros.png')
img_ver_livro = img_ver_livro.resize((18,18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
b_ver_livro = Button(frameEsquerda, image= img_ver_livro, compound= LEFT, anchor= NW, text= '  Exibir todos os livros', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_ver_livro.grid(row= 2, column= 0, sticky= NSEW, padx= 5, pady= 6)

# ver usuarios
img_ver_usuario = Image.open('logo_usuarios.png')
img_ver_usuario= img_ver_usuario.resize((18,18))
img_ver_usuario= ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda, command= lambda: control('ver_usuarios'), image= img_ver_usuario, compound= LEFT, anchor= NW, text= '  Exibir todos os usuários', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_ver_usuario.grid(row= 3, column= 0, sticky= NSEW, padx= 5, pady= 6)

# realizar um emprestimo
img_emprestimo = Image.open('novo_usuario.png')
img_emprestimo = img_emprestimo.resize((18,18))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
b_emprestimo = Button(frameEsquerda, image= img_emprestimo, compound= LEFT, anchor= NW, text= '  Realizar um emprestimo', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_emprestimo.grid(row= 4, column= 0, sticky= NSEW, padx= 5, pady= 6)

# devolução de um emprestimo
img_devolucao = Image.open('usuario_livro_emprestimo.png')
img_devolucao = img_devolucao.resize((22,22))
img_devolucao = ImageTk.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda, image= img_devolucao, compound= LEFT, anchor= NW, text= '  Devolução de um emprestimo', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_devolucao.grid(row= 5, column= 0, sticky= NSEW, padx= 5, pady= 6)

# livros emprestados no momento
img_livros_emprestados = Image.open('logo_emprestimos.png')
img_livros_emprestados = img_livros_emprestados.resize((18,18))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_livros_emprestados = Button(frameEsquerda, image= img_livros_emprestados, compound= LEFT, anchor= NW, text= '  Livros emprestados no momento', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_livros_emprestados.grid(row= 6, column= 0, sticky= NSEW, padx= 5, pady= 6)







janela.mainloop()