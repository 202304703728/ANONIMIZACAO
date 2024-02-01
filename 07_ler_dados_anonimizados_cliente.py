# Lê e anonimiza os dados da tabela CONTATO

import pyodbc

try:

    conn = pyodbc.connect('Driver={SQL Server};Server=SFREITASC100\SQLEXPRESS;Database=FALE_COMIGO'
                              ';user=SFREITASC100\sfrei;')

    print("Conexão aberta com sucesso!")
    cursor = conn.cursor()

    comandoSQL = """ 
        SELECT
        CASE
        WHEN IDADE <= 10 THEN '0 - 10'
        WHEN IDADE >= 11 AND IDADE <= 20 THEN '11 - 20'
        WHEN IDADE >= 21 AND IDADE <= 30 THEN '21 - 30'
        WHEN IDADE >= 31 AND IDADE <= 40 THEN '31 - 40'
        WHEN IDADE >= 41 AND IDADE <= 50 THEN '41 - 50'
        WHEN IDADE >= 51 AND IDADE <= 59 THEN '51 - 59'
        ELSE 'IDOSO' END AS "FAIXA_ETARIA",
        Count(IDADE) AS "TOTAL POR IDADE",
        NOME_ANONIMIZADO
        FROM CLIENTE
        GROUP BY IDADE,NOME_ANONIMIZADO
        ORDER BY FAIXA_ETARIA ASC
    """

    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()

    print("\n")
    print("Generalização")
    print("(Faixa Etária, Total, Nome Anonimizado)")

    for result in resultado:
        # Generalização do nome por categoria de faixa etária
        print(result)

    comandoSQL = """ 
        SELECT
        C1.CIDADE, C2.VOLUME_COMPRA AS "TOTAL DE COMPRAS", C2.CPF_ANONIMIZADO
        FROM CONTATO C1
        INNER JOIN CLIENTE C2 ON C1.CODIGO_CLIENTE = C2.CODIGO
        GROUP BY C1.CIDADE, C2.VOLUME_COMPRA, C2.CPF_ANONIMIZADO
        ORDER BY C1.CIDADE, "TOTAL DE COMPRAS"
        DESC
    """
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()

    print("\n")
    print("Supressão")
    print("(Cidade, Total de Compras, CPF Anonimizado)")

    for result in resultado:
        # Supressão do cpf dos maiores compradores por cidade
        print(result)

    conn.commit()
    print("\n")
    print("Consulta realizada com sucesso!")
    conn.close()

except:
    # Exceção ampla, mas quis deixar assim mesmo
    print("Ocorreu um erro durante a leitura dos dados.")
    print("Conexao encerrada.")
    conn.close()
