# Lê e anonimiza os dados da tabela CLIENTE

import pyodbc
import hashlib

try:

    conn = pyodbc.connect('Driver={SQL Server};Server=SFREITASC100\SQLEXPRESS;Database=FALE_COMIGO'
                              ';user=SFREITASC100\sfrei;')

    print("Conexão aberta com sucesso!")
    cursor = conn.cursor()

    comandoSQL = """ 
        SELECT *
        FROM CLIENTE;
    """

    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()

    for result in resultado:

        # Mascaramento dos caracteres do CPF
        result.CPF_ANONIMIZADO = result.CPF.replace(result.CPF, result.CPF[:3]+"********")

        # Ofuscação do nome por um hash
        result.NOME_ANONIMIZADO =hashlib.md5(result.NOME.encode()).hexdigest()
        #print(result)

        comandoSQL = """ 
                UPDATE CLIENTE
                SET CPF_ANONIMIZADO = ?,
                NOME_ANONIMIZADO = ?
                WHERE CODIGO = ?;
            """

        registro = (result.CPF_ANONIMIZADO, result.NOME_ANONIMIZADO, result.CODIGO)
        cursor.execute(comandoSQL, registro)

    conn.commit()
    print("Leitura e anonimização realizadas com sucesso!")
    conn.close()

except:
    # Exceção ampla, mas quis deixar assim mesmo
    print("Ocorreu um erro durante a leitura dos dados.")
    print("Conexao encerrada.")
    conn.close()
