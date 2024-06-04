import sqlite3

# Nome do arquivo do banco de dados
db_filename = 'dados.db'

# Conectar ao banco de dados 
def connect():
    return sqlite3.connect(db_filename)

# Função para criar as tabelas se não existirem
def create_tables():
    con = connect()
    # Verificar se a tabela livro já existe
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='livro'")
    result = cursor.fetchone()
    # Se a tabela livro não existir, crie-a
    if result is None:
        con.execute('''CREATE TABLE livro(
                        id INTEGER PRIMARY KEY,
                        titulo TEXT,
                        autor TEXT,
                        editora TEXT,
                        ano_publicacao INTEGER,
                        isbn TEXT)''')
    # Criar as tabelas usuario e emprestimo
    con.execute('''CREATE TABLE IF NOT EXISTS usuario(
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    sobrenome TEXT,
                    endereco TEXT,
                    email TEXT,
                    telefone TEXT)''')

    con.execute('''CREATE TABLE IF NOT EXISTS emprestimo(
                    id INTEGER PRIMARY KEY,
                    id_livro INTEGER,
                    id_usuario INTEGER,
                    data_emprestimo TEXT,
                    data_devolucao TEXT,
                    FOREIGN KEY(id_livro) REFERENCES livro(id),
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id))''')
    con.commit()
    con.close()

# Chamar a função para criar as tabelas
create_tables()
