import sqlite3
import time

# Conectar ao banco de dados 
def connect():
    con = sqlite3.connect('dados.db')
    return con

# função para inserir um novo livro
def insert_ebook(titulo, autor, editora, ano_publicacao, isbn):
    con = connect()
    try:
        con.execute("INSERT INTO livro(titulo, autor, editora, ano_publicacao, isbn) VALUES(? ,? ,? ,? ,?)", (titulo, autor, editora, ano_publicacao, isbn))
        con.commit()
    except sqlite3.OperationalError as e:
        # Se ocorrer um erro de bloqueio do banco de dados, tentar novamente após 1 segundo
        if "database is locked" in str(e):
            print("Erro: O banco de dados está bloqueado. Tentando novamente após 1 segundo.")
            time.sleep(1)
            insert_ebook(titulo, autor, editora, ano_publicacao, isbn)
        else:
            print("Erro ao inserir o livro:", e)
    finally:
        con.close()
    

# Funcao para inserir usuários
def insert_user(nome, sobrenome, endereco, email, telefone):
    con = connect()
    con.execute("INSERT INTO usuario(nome, sobrenome, endereco, email, telefone)\
                 VALUES(? ,? ,? ,? ,?)", (nome, sobrenome, endereco, email, telefone))
    
    con.commit()
    con.close()
# exemplo de funcoes
# insert_ebook('Dom Quixote', 'Miquel', 'Editora 1', 1605, '123456')
# insert_user('Mikael', 'Dias', 'Angola/Portugal', 'mikaelsd1010@icloud.com', '84555555222')

# funcao para exibir usuarios
def get_users():
    con = connect()
    c = con.cursor()
    c.execute('SELECT * FROM usuarios')
    users = c.fetchall()
    con.close()
    print(users)
    return users



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
    result = con.execute('SELECT livro.titulo, usuario.nome, usuario.sobrenome, emprestimo.id, emprestimo.data_emprestimo, emprestimo.data_devolucao\
                         FROM livro\
                         INNER JOIN emprestimo ON livro.id = emprestimo.id_livro\
                         INNER JOIN  usuario ON usuario.id = emprestimo.id_usuario\
                         WHERE emprestimo.data_devolucao IS NULL').fetchall()
    con.close()
    return result


# funçao para atualizar a data de devolução de emprestimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    con = connect()
    try:
        con.execute('UPDATE emprestimo SET data_devolucao = ? WHERE id = ?', (data_devolucao, id_emprestimo))
        con.commit()
    except sqlite3.OperationalError as e:
        # Se ocorrer um erro de bloqueio do banco de dados, tentar novamente após 1 segundo
        if "database is locked" in str(e):
            print("Erro: O banco de dados está bloqueado. Tentando novamente após 1 segundo.")
            time.sleep(1)
            update_loan_return_date(id_emprestimo, data_devolucao)
        else:
            print("Erro ao atualizar a data de devolução do empréstimo:", e)
    finally:
        con.close()
insert_loan(1, 1, '2022-08-13', None)
livros_emprestados = get_books_on_loan()
# print(livros_emprestados)
'''insert_ebook('Dom Quixote', 'Miguel de Cervantes', 'Editora X', 1605, '9781234567890')'''
# update_loan_return_date(1, '2022-09-21')

# exibir_livros()
