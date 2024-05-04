import sqlite3

# Conectar ao banco de dados ou criar um novo banco de dados
con = sqlite3.connect('dados.db')

# Criar tabela de livros 
con.execute('CREATE TABLE livro(\
                id INTEGER PRIMARY KEY,\
                titulo TEXT,\
                autor TEXT,\
                editora TEXT,\
                ano_publicacao INTEGER,\
                isbn TEXT)')

# Criar tabela de Usuários
con.execute('CREATE TABLE usuario(\
                id INTEGER PRIMARY KEY,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT,\
                email TEXT,\
                telefone TEXT)')

# Criar tabela de empréstimo
con.execute('CREATE TABLE emprestimo(\
                id INTEGER PRIMARY KEY,\
                id_livro INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREIGN KEY(id_livro) REFERENCES livro(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuario(id))')

# Commit para salvar as alterações no banco de dados
con.commit()

# Fechar a conexão com o banco de dados
con.close()