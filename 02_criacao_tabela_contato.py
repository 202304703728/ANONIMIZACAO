# Criação da tabela CONTATO

import pyodbc

try:

    conn = pyodbc.connect('Driver={SQL Server};Server=SFREITASC100\SQLEXPRESS;Database=FALE_COMIGO'
                          ';user=SFREITASC100\sfrei;')

    print("Conexão com o banco de dados feita com sucesso!")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE CONTATO
    (
     CODIGO INT NOT NULL PRIMARY KEY,
     TELEFONE_FIXO char(20),
     CELULAR char(20),
     ENDERECO VARCHAR(100) NOT NULL,
     BAIRRO VARCHAR(50) NOT NULL,
     CIDADE VARCHAR(50) NOT NULL,
     UF VARCHAR(2) NOT NULL,
     PAIS char(20) NOT NULL,
     CEP VARCHAR(9) NOT NULL,
     CODIGO_CLIENTE INT NOT NULL,
     CONSTRAINT FK_CLIENTE_CONTATO FOREIGN KEY (CODIGO_CLIENTE) REFERENCES CLIENTE (CODIGO)
     );
    ''')

    print("Tabela criada com sucesso!")
    conn.commit()
    conn.close()
    print("Conexao encerrada.")

except:
    # Exceção ampla, mas quis deixar assim mesmo
    print("Ocorreu um erro durante a criação da tabela.")
    print("Conexao encerrada.")
    conn.close()

