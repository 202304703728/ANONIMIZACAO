# Alteração da tabela CLIENTE
# para incluir as colunas CPF_ANONIMIZADO e NOME_ANONIMIZADO

import pyodbc

try:

    conn = pyodbc.connect('Driver={SQL Server};Server=SFREITASC100\SQLEXPRESS;Database=FALE_COMIGO'
                          ';user=SFREITASC100\sfrei;')

    print("Conexão com o banco de dados feita com sucesso!")
    cur = conn.cursor()
    cur.execute('''
    ALTER TABLE CLIENTE
    ADD CPF_ANONIMIZADO VARCHAR(11) NULL,
    NOME_ANONIMIZADO VARCHAR(100) NULL;
    ''')

    print("Tabela alterada com sucesso!")
    conn.commit()
    conn.close()

except:
    # Exceção ampla, mas quis deixar assim mesmo
    print("Ocorreu um erro durante a alteração da tabela.")
    print("Conexao encerrada.")
    conn.close()
