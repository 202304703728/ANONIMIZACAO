# Criação da tabela CLIENTE

import pyodbc

try:

    conn = pyodbc.connect('Driver={SQL Server};Server=SFREITASC100\SQLEXPRESS;Database=FALE_COMIGO'
                          ';user=SFREITASC100\sfrei;')

    print("Conexão com o banco de dados feita com sucesso!")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE CLIENTE
    (
    CODIGO INT NOT NULL PRIMARY KEY,
    CPF VARCHAR(11) NOT NULL,
    NOME VARCHAR(100) NOT NULL,
    IDADE INT NOT NULL,
    SEXO VARCHAR(1) NOT NULL,
    LIMITE_CREDITO FLOAT NOT NULL,
    VOLUME_COMPRA FLOAT NOT NULL
    );
    ''')

    print("Tabela criada com sucesso!")
    conn.commit()
    conn.close()

except:
    # Exceção ampla, mas quis deixar assim mesmo
    print("Ocorreu um erro durante a criação da tabela.")
    print("Conexao encerrada.")
    conn.close()
