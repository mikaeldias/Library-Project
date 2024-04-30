import sqlite3

# Conectar ao banco de dados 
def connect():
    con = sqlite3.connect('dados.db')
    return con

# função para inserir um novo livro
def insert_ebook(titulo, autor, editora, ano_publicacao, isbn):
    con = connect()
    con.execute("INSERT INTO livro(titulo, autor, editora, ano_publicacao, isbn)\
                 VALUES(?,?,?,?,?)",(titulo, autor, editora, ano_publicacao, isbn))
    

# Funcao para inserir usuários
def insert_user(nome, sobrenome, endereco, email, telefone):
    con = connect()
    con.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                 VALUES(?,?,?,?,?)", (nome, sobrenome, endereco, email, telefone))
    

# exemplo de funcoes
insert_ebook('DoM quixote','miquel', 'editora_10,', 1605, '12346')    

# insert_user('Mikael', 'Dias', 'Angola/Portugal', 'mikaelsd1010@icloud.com', '84555555222')

# Funcao para exibir os livros
def exibir_livros():
    con = connect()
    livros = con.execute('SELECT * FROM livro').fetchall()
    con.close()
    
    if not livros:
        print('Nenhum livro encontrado na biblioteca.')
        return 
    print('Livros na biblioteca:')
    for livro in livros:
        print(f'ID: {livro[0]}')
        print(f'Titulo: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Editora: {livro[3]}')
        print(f'Ano de Publicacao: {livro[4]}')
        print(f'ISBN: {livro[5]}')
        print('\n')

# Funcao para realizar emprestimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    con = connect()
    con.execute('INSERT INTO emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                VALUES(?,?,?,?)',(id_livro, id_usuario, data_emprestimo, data_devolucao)) 
    con.commit()
    con.close()  
# Funcao para exibir todos os livros emprestado no momento   
def get_books_on_loan():
    con = connect()
    result = con.execute('SELECT livro.titulo, usuario.nome, usuario.sobrenome, emprestimo.data_emprestimo, emprestimo.data_devolucao\
                         FROM livro\
                         INNER JOIN emprestimo ON livro.id = emprestimo.id_livro\
                         INNER JOIN usuario ON usuario.id = emprestimo.id_usuario\
                         WHERE emprestimo.data_devolucao IS NULL').fetchall()
    con.close()    
    return result
#insert_loan(1,1,'2024-04-24', None)
insert_loan(1, 1, "2022-09-20", None)
print(get_books_on_loan())

#exibir_livros()
