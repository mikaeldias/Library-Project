import sqlite3
import time
import os

# Função para conectar ao banco de dados 
def connect():
    db_path = os.path.abspath('dados.db')
    print(f"Conectando ao banco de dados: {db_path}")
    return sqlite3.connect(db_path)

# Função para criar as tabelas se não existirem
def create_tables():
    con = connect()
    try:
        cursor = con.cursor()
        
        # Criar a tabela livro se não existir
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='livro'")
        if cursor.fetchone() is None:
            print("Criando tabela 'livro'...")
            cursor.execute('''CREATE TABLE livro(
                                id INTEGER PRIMARY KEY,
                                titulo TEXT,
                                autor TEXT,
                                editora TEXT,
                                ano_publicacao INTEGER,
                                isbn TEXT)''')
        
        # Criar a tabela usuario se não existir
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuario(
                            id INTEGER PRIMARY KEY,
                            nome TEXT,
                            sobrenome TEXT,
                            endereco TEXT,
                            email TEXT,
                            telefone TEXT)''')
        
        # Criar a tabela emprestimo se não existir
        cursor.execute('''CREATE TABLE IF NOT EXISTS emprestimo(
                            id INTEGER PRIMARY KEY,
                            id_livro INTEGER,
                            id_usuario INTEGER,
                            data_emprestimo TEXT,
                            data_devolucao TEXT,
                            FOREIGN KEY(id_livro) REFERENCES livro(id),
                            FOREIGN KEY(id_usuario) REFERENCES usuario(id))''')
        
        con.commit()
        print("Tabelas criadas com sucesso (se necessário).")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabelas: {e}")
    finally:
        con.close()

# Função para inserir um novo livro
def insert_ebook(titulo, autor, editora, ano_publicacao, isbn):
    con = connect()
    try:
        con.execute("INSERT INTO livro(titulo, autor, editora, ano_publicacao, isbn) VALUES(? ,? ,? ,? ,?)", 
                    (titulo, autor, editora, ano_publicacao, isbn))
        con.commit()
    except sqlite3.OperationalError as e:
        if "database is locked" in str(e):
            print("Erro: O banco de dados está bloqueado. Tentando novamente após 1 segundo.")
            time.sleep(1)
            insert_ebook(titulo, autor, editora, ano_publicacao, isbn)
        else:
            print("Erro ao inserir o livro:", e)
    finally:
        con.close()

# Função para inserir usuários
def insert_user(nome, sobrenome, endereco, email, telefone):
    con = connect()
    try:
        con.execute("INSERT INTO usuario(nome, sobrenome, endereco, email, telefone) VALUES(? ,? ,? ,? ,?)", 
                    (nome, sobrenome, endereco, email, telefone))
        con.commit()
    except sqlite3.Error as e:
        print("Erro ao inserir o usuário:", e)
    finally:
        con.close()

# Função para exibir usuários
def get_users():
    con = connect()
    c = con.cursor()
    c.execute('SELECT * FROM usuario')
    users = c.fetchall()
    con.close()
    return users

# Função para exibir os livros
def exibir_livros():
    con = connect()
    try:
        livros = con.execute('SELECT * FROM livro').fetchall()
        if not livros:
            print('Nenhum livro encontrado na biblioteca.')
            return
        print("Livros encontrados:", livros)
        return livros
    except sqlite3.Error as e:
        print("Erro ao buscar livros:", e)
    finally:
        con.close()

# Função para realizar empréstimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    con = connect()
    try:
        con.execute("INSERT INTO emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)", 
                    (id_livro, id_usuario, data_emprestimo, data_devolucao))
        con.commit()
    except sqlite3.Error as e:
        print("Erro ao registrar o empréstimo:", e)
    finally:
        con.close()

# Função para obter os livros emprestados no momento
def get_books_on_loan():
    con = connect()
    try:
        result = con.execute('''SELECT emprestimo.id, livro.titulo, usuario.nome, usuario.sobrenome, 
                                emprestimo.data_emprestimo, emprestimo.data_devolucao 
                                FROM livro 
                                INNER JOIN emprestimo ON livro.id = emprestimo.id_livro 
                                INNER JOIN usuario ON usuario.id = emprestimo.id_usuario 
                                WHERE emprestimo.data_devolucao ''').fetchall()
        print("Livros emprestados encontrados:", result)
        return result
    except sqlite3.Error as e:
        print("Erro ao buscar livros emprestados:", e)
        return []
    finally:
        con.close()

# Função para atualizar a data de devolução de empréstimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    con = connect()
    try:
        con.execute("UPDATE emprestimo SET data_devolucao = ? WHERE id = ?", 
                    (data_devolucao, id_emprestimo))
        con.commit()
    except sqlite3.Error as e:
        print("Erro ao atualizar data de devolução:", e)
    finally:
        con.close()

# Executando as funções para garantir que tudo está funcionando corretamente
create_tables()

# Inserir exemplos de dados
# insert_ebook('Dom Quixote', 'Miguel de Cervantes', 'Editora 1', 1605, '123456')
# insert_user('Mikael', 'Dias', 'Angola/Portugal', 'mikaelsd1010@icloud.com', '84555555222')

# Exibir usuários e livros
print(get_users())
print(exibir_livros())

# Inserir um empréstimo de exemplo
# insert_loan(1, 1, '2024-06-04', None)

# Obter livros emprestados
print(get_books_on_loan())

# Atualizar data de devolução
# update_loan_return_date(1, '2024-06-10')

# Verificar novamente livros emprestados
print(get_books_on_loan())
