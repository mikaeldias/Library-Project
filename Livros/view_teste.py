import sqlite3
import time

# Função para inserir um empréstimo
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

# Exemplo de chamada da função
insert_loan(1, 1, "2024-04-30", None)