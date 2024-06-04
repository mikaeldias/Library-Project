
from tkinter .ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
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
co12 = '#4169e1' 
co13 = '#000000'
co14 = '#daa520'

# criando janela
janela = Tk()
janela.title('')
janela.geometry('770x330')
janela.configure(bg = co1)
janela.resizable(width= FALSE, height= FALSE)

style = Style(janela)
style.theme_use('clam')

# Frames
frameCima = Frame(janela, width = 770, height = 50, bg = co13, relief = 'flat' )
frameCima.grid(row = 0, column = 0, columnspan = 2, sticky = NSEW )

frameEsquerda = Frame(janela, width = 150, height = 265, bg = co14, relief = 'solid' )
frameEsquerda.grid(row = 1, column = 0, sticky = NSEW )

frameDireita = Frame(janela, width = 600, height = 265, bg = co1, relief = 'raised' )
frameDireita.grid(row = 1, column = 1, sticky = NSEW )

# LOGO
# abrindo a imagem
# app_img0 = Image.open('ROSACRUZ1.jpeg')
# app_img0 = app_img0.resize((50,40))
# app_img0 = ImageTk.PhotoImage(app_img0)

# app_img1 = Image.open('ROSA CRUZ 2.jpeg')
# app_img1 = app_img1.resize((90,50))
# app_img1 = ImageTk.PhotoImage(app_img1)

app_logo = Label(frameCima, width= 1000, compound= LEFT, padx= 5, anchor= NW, bg= co13, fg= co1)
app_logo.place(x=0, y=5) # imagem canto superior esquerdo

app_logo = Label(frameCima, width= 1000, compound= LEFT, padx= 5, anchor= NW, bg= co13, fg= co1)
app_logo.place(x=695, y=5) # imagem canto superior esquerdo

app_logo = Label(frameCima, text= 'Sistema de Gerenciamento de Livros',compound= LEFT, padx= 5, anchor= NW, font= ('Verdana 15 bold'),bg=co13, fg= co1)
app_logo.place(x= 170, y=7) # texto 

app_linha = Label(frameCima, width= 770, height= 1 , padx= 5, anchor= NW, font= ('Verdana 15 bold'),bg=co13, fg= co14)
app_linha.place(x= 0, y=47) # linha azul abaixo do texto

# Função para registrar um novo usuário
# novo usuario
def novo_usuario():
        
    global img_salvar

    def adf():
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

                  

    app_ = Label(frameDireita, text= 'Inserir um novo usuário', width= 50, compound= LEFT, padx= 5, pady= 10, font= 'Verdana 12', bg= co1, fg= co13)
    app_.grid(row= 0, column= 0, columnspan= 5, sticky= NSEW)

    app_linha = Label(frameDireita, width= 505, height= 1 , anchor= NW, font= ('Verdana 1'),bg=co1, fg= co1)
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
    b_salvar = Button(frameDireita, command= adf, image= img_salvar, compound= LEFT, width= 100,  anchor= NW, text= '  Salvar', bg= co1, fg= co4, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
    b_salvar.grid(row= 7, column= 1, pady= 5, sticky= NSEW)



def ver_usuarios():
    app_ = Label(frameDireita, text='Ver usuário', width=50, compound=LEFT, padx=5, pady=10, font='Verdana 12', bg=co1, fg=co13)
    app_.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    app_linha = Label(frameDireita, width=505, height=1, anchor=NW, font=('Verdana 1'), bg=co1, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_users()

    # creating a treeview with dual scrollbars
    list_header = ['ID', 'Nome', 'Sobrenome', 'Endereço', 'Email', 'Telefone']

    global tree

    tree = ttk.Treeview(frameDireita, selectmode='extended', columns=list_header, show='headings')

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient='vertical', command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'nw']
    h = [20, 80, 80, 120, 76, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # Move the loop for inserting items outside of the loop for setting column headers
    for item in dados:
        tree.insert('', 'end', values=item)



def novo_livro():
    global img_salvar

    def adb():
        title = e_titulo.get()
        author = e_autor.get()
        publish = e_editora.get()
        year = e_ano.get()
        isbn = e_isbn.get()

        lista = [title, author, publish, year, isbn]

        # verificando caso algum campo esteja vazio
        for i in lista:
            if i == '':
                messagebox.showerror('Erro:', 'Preencha todos os campos')
                return
                  
        # inserindo os dados no banco de dados
        insert_ebook(title, author, publish, year, isbn)

        messagebox.showinfo('Sucesso', 'Livro registrado com sucesso')

        # limpados os campos de entrada
        e_titulo.delete(0, END)
        e_editora.delete(0, END)
        e_ano.delete(0, END)
        e_autor.delete(0, END)
        e_isbn.delete(0, END)



    app_ = Label(frameDireita, text= 'Inserir um novo livro', width= 50, compound= LEFT, padx= 5, pady= 10, font= 'Verdana 12', bg= co1, fg= co13)
    app_.grid(row= 0, column= 0, columnspan= 3, sticky= NSEW)

    app_linha = Label(frameDireita, width= 505, height= 1 , anchor= NW, font= ('Verdana 1'),bg=co1, fg= co1)
    app_linha.grid(row= 1, column= 0, columnspan= 3, sticky= NSEW)

    # label primeiro nome e entrada primeiro nome
    l_livro = Label(frameDireita, text= 'Titulo do livro*', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
    l_livro.grid(row= 2, column= 0, padx= 5, pady= 5, sticky= NSEW)
    e_titulo = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
    e_titulo.grid(row= 2, column= 1, padx= 5, pady= 5, sticky= NSEW)

    # label sobrenome e entrada sobrenome
    l_autor = Label(frameDireita, text= 'Autor do livro*', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
    l_autor.grid(row= 3, column= 0, padx= 5, pady= 5, sticky= NSEW)
    e_autor = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
    e_autor.grid(row= 3, column= 1, padx= 5, pady= 5, sticky= NSEW)

    # label e entrada endereco
    l_editora = Label(frameDireita, text= 'Editora do livro*', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
    l_editora.grid(row= 4, column= 0, padx= 5, pady= 5, sticky= NSEW)
    e_editora = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
    e_editora.grid(row= 4, column= 1, padx= 5, pady= 5, sticky= NSEW)

    # label e entrada email
    l_ano = Label(frameDireita, text= 'Ano de publicação do livro', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
    l_ano.grid(row= 5, column= 0, padx= 5, pady= 5, sticky= NSEW)
    e_ano = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
    e_ano.grid(row= 5, column= 1, padx= 5, pady= 5, sticky= NSEW)

    # label e entrada numero
    l_isbn = Label(frameDireita, text= 'ISBN do livro', padx= 5, anchor= NW, font= 'Ivy 10', bg= co1, fg= co4)
    l_isbn.grid(row= 6, column= 0, padx= 5, pady= 5, sticky= NSEW)
    e_isbn = Entry(frameDireita, width= 25, justify= 'left', relief= 'solid')
    e_isbn.grid(row= 6, column= 1, padx= 5, pady= 5, sticky= NSEW)

    # botao salvar
    img_salvar = Image.open('salvar.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command= adb, image= img_salvar, compound= LEFT, width= 100,  anchor= NW, text= '  Salvar', bg= co1, fg= co4, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
    b_salvar.grid(row= 7, column= 1, pady= 5, sticky= NSEW)
    

# funcao ver livros

        

def ver_livros():
    app_ = Label(frameDireita, text='Todos os livros', width=50, compound=LEFT, padx=5, pady=10, font='Verdana 12', bg=co1, fg=co13)
    app_.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    app_linha = Label(frameDireita, width=505, height=1 , anchor=NW, font=('Verdana 1'), bg=co1, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = exibir_livros()
    
    # Remova a árvore de visualização antiga se ela já existir
    if hasattr(frameDireita, 'tree'):
        frameDireita.tree.destroy()

    # Criando uma nova árvore de visualização
    list_header = ['ID', 'Título', 'Autor', 'Editora', 'Ano', 'ISBN']
    tree = ttk.Treeview(frameDireita, selectmode='extended', columns=list_header, show='headings')

    vsb = ttk.Scrollbar(frameDireita, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'nw']
    h = [20, 165, 110, 100, 50, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)

    # Atualize o atributo tree do frameDireita
    frameDireita.tree = tree

    # emprestimos
def emprestimo():
    global img_salvar

    def ade():
        book_id = e_id_livro.get() 
        user_id = e_id_usuario.get()  # Corrigido para 'e_id_usuario'
        dev_id = e_data_devolucao.get()
        dt_id = e_data_emprestimo.get()

        lista = [book_id, user_id, dt_id, dev_id]

        # verificando se algum campo está vazio
        for i in lista:
            if i == '':
                messagebox.showerror('Erro:', 'Preencha todos os campos')
                return

        # inserindo os dados no banco de dados
        insert_loan(book_id, user_id, dt_id, dev_id)

        messagebox.showinfo('Sucesso', 'Empréstimo registrado com sucesso')

        # limpando os campos de entrada
        e_id_livro.delete(0, END)
        e_id_usuario.delete(0, END)
        e_data_devolucao.delete(0, END)
        e_data_emprestimo.delete(0, END)

    app_ = Label(frameDireita, text='Empréstimo', width=50, compound=LEFT, padx=5, pady=10, font='Verdana 12', bg=co1, fg=co13)
    app_.grid(row=0, column=0, columnspan=5, sticky=NSEW)

    app_linha = Label(frameDireita, width=505, height=1, anchor=NW, font=('Verdana 1'), bg=co1, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    # label primeiro nome e entrada primeiro nome
    livro = Label(frameDireita, text='ID Livro*', padx=5, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
    livro.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_livro = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_livro.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    # label sobrenome e entrada sobrenome
    usuario = Label(frameDireita, text='ID Usuário*', padx=5, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
    usuario.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_usuario = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_usuario.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    # label sobrenome e entrada sobrenome
    dev = Label(frameDireita, text='Data de emprestimo*', padx=5, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
    dev.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_data_devolucao = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_data_devolucao.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    # label sobrenome e entrada sobrenome
    dt = Label(frameDireita, text='Data de devolução*', padx=5, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
    dt.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_data_emprestimo = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_data_emprestimo.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

   
    # botao salvar
    img_salvar = Image.open('salvar.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=ade, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)


    # Função para exibir todos os livros emprestados
def livros_emprestimo():

    # Configurar título e linha divisória
    app_ = Label(frameDireita, text='Todos os livros emprestados no momento', width=50, compound=LEFT, padx=5, pady=10, font='Verdana 12', bg=co1, fg=co13)
    app_.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    app_linha = Label(frameDireita, width=505, height=1, anchor=NW, font=('Verdana 1'), bg=co1, fg='white')
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = []
    
    # Obter livros emprestados
    books_on_loan = get_books_on_loan()

    # Processar dados dos livros emprestados
    for book in books_on_loan:
        dado = [f'{book[0]}', f'{book[1]}', f'{book[2]} {book[3]}', f'{book[4]}', f'{book[5]}']
        dados.append(dado)

    # Configurar cabeçalhos e colunas da Treeview
    list_header = ['ID', 'Titulo', 'Nome do usuário', 'D. empréstimo', 'D. devolução']
    tree = ttk.Treeview(frameDireita, selectmode='extended', columns=list_header, show='headings')

    vsb = ttk.Scrollbar(frameDireita, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient='horizontal', command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ['nw', 'nw', 'nw', 'nw', 'ne']
    h = [20, 175, 120, 90, 90]
    n = 0

    for col, width in zip(list_header, h):
        tree.column(col, width=width, anchor=hd[n])
        tree.heading(col, text=col, anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)


    
# Devolucao de um emprestimo
def devolucao_emprestimo():
    global img_salvar

    def adc():
        # Obtendo os valores inseridos nos campos de entrada
        loan_id_str = e_id_emprestimo.get()
        return_date = e_data_retorno.get()

        # Verificando se algum campo está vazio
        if loan_id_str.strip() == '' or return_date.strip() == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

        try:
            # Convertendo o ID do empréstimo para inteiro
            loan_id = int(loan_id_str)
        except ValueError:
            messagebox.showerror('Erro', 'ID do empréstimo deve ser um número inteiro válido')
            return

        # Inserindo os dados no banco de dados (essa função precisa ser definida)
        update_loan_return_date(loan_id, return_date)

        # Exibindo uma mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Livro retornado com sucesso')

        # Limpando os campos de entrada
        e_id_emprestimo.delete(0, END)
        e_data_retorno.delete(0, END)

    app_ = Label(frameDireita, text='Atualizar a data de devolução do empréstimo', width=50, compound=LEFT, padx=5, pady=10, font='Verdana 12', bg=co1, fg=co13)
    app_.grid(row=0, column=0, columnspan=5, sticky=NSEW)

    app_linha = Label(frameDireita, width=505, height=1, anchor=NW, font=('Verdana 1'), bg=co1, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    # Label e entrada para o ID do empréstimo
    j_id_emprestimo = Label(frameDireita, text='ID do empréstimo*', padx=5, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
    j_id_emprestimo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_emprestimo = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    # Label e entrada para a nova data de devolução
    l_data_retorno = Label(frameDireita, text='Nova data de devolução*', padx=5, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
    l_data_retorno.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_data_retorno = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_data_retorno.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    # botao salvar
    img_salvar = Image.open('salvar.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=adc, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

    app_ = Label(frameDireita, text='Atualizar a data de devolução do empréstimo', width=50, compound=LEFT, padx=5, pady=10, font='Verdana 12', bg=co1, fg=co13)
    app_.grid(row=0, column=0, columnspan=5, sticky=NSEW)

    app_linha = Label(frameDireita, width=505, height=1, anchor=NW, font=('Verdana 1'), bg=co1, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    # Label e entrada para o ID do empréstimo
    j_id_emprestimo = Label(frameDireita, text='ID do empréstimo*', padx=5, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
    j_id_emprestimo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_emprestimo = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    # Label e entrada para a nova data de devolução
    l_data_retorno = Label(frameDireita, text='Nova data de devolução*', padx=5, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
    l_data_retorno.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_data_retorno = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_data_retorno.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    # Botão salvar
    img_salvar = Image.open('salvar.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=adc, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)





# Função para controlar o menu
def control(i):      
    
    # novo usuario
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a funcao novo usuario
        novo_usuario()
           
    
    # ver usuario
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a funcao novo usuario
        ver_usuarios()

    # novo livro
    if i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a funcao novo livro
        novo_livro()
    
    # ver livro
    if i == 'ver_livros':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a funcao ver livro
        ver_livros()

        # realizar emprestimo
    if i == 'emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a funcao ver livro
        emprestimo()

    if i == 'livros_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a funcao ver livro
        livros_emprestimo()

    if i == 'retorno':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a funcao devolucao emprestimo
        devolucao_emprestimo()
 
#  Menu

# Novo usuario
img_usuario = Image.open('novo_usuario.png')
img_usuario = img_usuario.resize((18,18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, command= lambda: control('novo_usuario') ,image= img_usuario, compound= LEFT, anchor= NW, text= '  Novo usuário', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_usuario.grid(row= 0, column= 0, sticky= NSEW, padx= 5, pady= 6)

# Novo livro
img_novo_livro = Image.open('novo_usuario.png')
img_novo_livro = img_novo_livro.resize((18,18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda, command= lambda:control('novo_livro'), image= img_novo_livro, compound= LEFT, anchor= NW, text= '  Novo livro', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_novo_livro.grid(row= 1, column= 0, sticky= NSEW, padx= 5, pady= 6)

# ver livros
img_ver_livro = Image.open('logo_livros.png')
img_ver_livro = img_ver_livro.resize((18,18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
b_ver_livro = Button(frameEsquerda, command=lambda:control('ver_livros'), image= img_ver_livro, compound= LEFT, anchor= NW, text= '  Exibir todos os livros', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_ver_livro.grid(row= 2, column= 0, sticky= NSEW, padx= 5, pady= 6)

# ver usuarios
img_ver_usuario = Image.open('logo_usuarios.png')
img_ver_usuario= img_ver_usuario.resize((18,18))
img_ver_usuario= ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda, command=lambda: control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text='  Exibir todos os usuários', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row= 3, column= 0, sticky= NSEW, padx= 5, pady= 6)

# realizar um emprestimo
img_emprestimo = Image.open('novo_usuario.png')
img_emprestimo = img_emprestimo.resize((18,18))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
b_emprestimo = Button(frameEsquerda, command=lambda: control('emprestimo'), image= img_emprestimo, compound= LEFT, anchor= NW, text= '  Realizar um emprestimo', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_emprestimo.grid(row= 4, column= 0, sticky= NSEW, padx= 5, pady= 6)

# devolução de um emprestimo
img_devolucao = Image.open('usuario_livro_emprestimo.png')
img_devolucao = img_devolucao.resize((22,22))
img_devolucao = ImageTk.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda, command=lambda: control('retorno'), image= img_devolucao, compound= LEFT, anchor= NW, text= '  Devolução de um emprestimo', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_devolucao.grid(row= 5, column= 0, sticky= NSEW, padx= 5, pady= 6)

# livros emprestados no momento
img_livros_emprestados = Image.open('logo_emprestimos.png')
img_livros_emprestados = img_livros_emprestados.resize((18,18))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_livros_emprestados = Button(frameEsquerda, command=lambda: control('livros_emprestimo'), image= img_livros_emprestados, compound= LEFT, anchor= NW, text= '  Livros emprestados no momento', bg= co4, fg= co1, font= ('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
b_livros_emprestados.grid(row= 6, column= 0, sticky= NSEW, padx= 5, pady= 6)

janela.mainloop()

input()