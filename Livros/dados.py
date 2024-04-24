import sqlite3

# Conectar ao banco de dados ou criar um novo banco de dados
con = sqlite3.connect('dados.db')

# Criar tabela de livros 
con.execute('CREATE TABLE livros(\
                id INTEGER PRIMARY KEY,\
                titulo TEXT,\
                autor TEXT,\
                editora TEXT,\
                ano_publicacao INTEGER,\
                isbn TEXT)')

# Criando tabela de Usuarios
con.execute('CREATE TABLE usuarios(\
                id INTEGER PRIMARY KEY,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT,\
                email TEXT,\
                telefone TEXT)')

# Criando tabela de emprestimo
con.execute('CREATE TABLE emprestimo(\
                id INTEGER PRIMARY KEY,\
                id_livro INTEGER,\
                id_usuario INTIGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREIGN KEY(id_livro) REFERENCES livros(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')
