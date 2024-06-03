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
    c.execute('SELECT * FROM usuario')
    users = c.fetchall()
    con.close()
    return users



# Funcao para exibir os livros
def exibir_livros():
    con = connect()
    livros = con.execute('SELECT * FROM livro').fetchall()
    con.close()
    
    if not livros:
        print('Nenhum livro encontrado na biblioteca.')
        return 
    
    return(livros)



# funcao para realizar emprestimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                  VALUES (?,?,?,?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Função para obter os livros emprestados no momento
def get_books_on_loan():    
    conn = connect()
    try:
        # Tente executar a consulta SQL
        result = conn.execute('SELECT emprestimo.id, livro.titulo, usuario.nome, usuario.sobrenome, emprestimo.data_emprestimo, emprestimo.data_devolucao \
                                FROM livro \
                                INNER JOIN emprestimo ON livro.id = emprestimo.id_livro \
                                INNER JOIN usuario ON usuario.id = emprestimo.id_usuario \
                                WHERE emprestimo.data_devolucao').fetchall()
        conn.close()
        return result
    except sqlite3.OperationalError as e:
        # Se ocorrer um erro de tabela não existente, imprima uma mensagem e retorne uma lista vazia
        print("Erro ao buscar livros emprestados:", e)
        conn.close()
        return []

# Exemplo de uso
livros_emprestados = get_books_on_loan()
print(livros_emprestados)

# funçao para atualizar a data de devolução de emprestimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimo SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()

livros_emprestados = get_books_on_loan()
exibir_livros()