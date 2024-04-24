import sqlite3

# Conectar ao banco de dados 
def connect():
    con = sqlite3.connect('dados.db')
    return con

# função para inserir um novo livro
def insert_ebook(titulo, autor, editora, ano_publicacao, isbn):
    con = connect()
    con.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn)\
                 VALUES(?,?,?,?,?)",(titulo, autor, editora, ano_publicacao, isbn))
    

# Funcao para inserir usuários
def insert_user(nome, sobrenome, endereco, email, telefone):
    con = connect()
    con.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                 VALUES(?,?,?,?,?)", (nome, sobrenome, endereco, email, telefone))
    

# exemplo de funcoes
# insert_ebook('DoM quixote','miquel', 'editora_10,', 1605, '12346')    

# insert_user('Mikael', 'Dias', 'Angola/Portugal', 'mikaelsd1010@icloud.com', '84555555222')

# Funcao para exibir os livros
def exibir_livros():
    conn = connect()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.close()
    
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

exibir_livros()