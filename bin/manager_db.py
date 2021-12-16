import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    #Cria a conexão com o banco de dados e cria novo banco caso não exista.
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print (e)
    finally:
        if conn:
            conn.close()

def create_table_db(db_file):
    #Cria uma tabela para a gravação dos contatos de email
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, 
        email TEXT NOT NULL);""")
    conn.close()

def insert_value(db_file, data):
    #Insere as entradas na Tabela de contatos.
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('INSERT INTO contatos (nome, email) VALUES (NULL,  ?, ? )', data)
    conn.commit()

def insert_mult_values(db_file, multi_data):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.executemany('INSERT INTO contatos VALUES (NULL, ?, ? )', multi_data)
    conn.commit()

def select_value(db_file, index):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    data = c.execute('SELECT * FROM contatos WHERE ID ='+str(index)).fetchall()
    c.close()
    email = data[0]
    return email

def cont_rows(db_file):
    conn = sqlite3.connect(db_file)
    n_rows = conn.cursor().execute('SELECT * FROM contatos')
    conn.cursor().close()
    return n_rows