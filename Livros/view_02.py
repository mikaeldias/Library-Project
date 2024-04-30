import sqlite3
import time

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
    
    con.commit()
    con.close()
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

# funcao para realizar emprestimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    con = sqlite3.connect('dados.db')
    try:
        con.execute('INSERT INTO emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao) \
                     VALUES (?, ?, ?, ?)', (id_livro, id_usuario, data_emprestimo, data_devolucao))
        con.commit()
    except sqlite3.OperationalError as e:
        # Se ocorrer um erro de bloqueio do banco de dados, tentar novamente após 1 segundo
        if "database is locked" in str(e):
            print("Erro: O banco de dados está bloqueado. Tentando novamente após 1 segundo.")
            time.sleep(1)
            insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao)
        else:
            print("Erro ao inserir empréstimo:", e)
    finally:
        con.close()

#funcao para exibir todos os livros emprestados no momento
def get_books_on_loan():    
    con = connect()
    result = con.execute('SELECT livro.titulo, usuario.nome, usuario.sobrenome, emprestimo.data_emprestimo, emprestimo.data_devolucao\
                         FROM livros\
                         INNER JOIN emprestimo ON livro.id = emprestimo.id_livro\
                         INNER JOIN  usuario ON usuario.id = emprestimo.id_usuario\
                         WHERE emprestimo.data_devolucao IS NULL').fetchall()
    con.close()
    return result

insert_loan(1, 1, '2024/04/30', None)






exibir_livros()