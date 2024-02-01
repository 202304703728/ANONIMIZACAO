# Cria dados aleatórios para a tabela CLIENTE

from faker import Faker
import pyodbc

try:

    conn = pyodbc.connect('Driver={SQL Server};Server=SFREITASC100\SQLEXPRESS;Database=FALE_COMIGO'
                              ';user=SFREITASC100\sfrei;')

    print("Conexão aberta com sucesso!")
    cursor = conn.cursor()
    fake = Faker('pt_BR')
    n = 100
    for i in range(n):
        codigo = i+1
        codigo_cliente = fake.pyint(min_value=1, max_value=n, step=1)
        telefone_fixo = str(fake.phone_number())
        celular = str(fake.phone_number())
        endereco = fake.street_address()
        bairro = fake.city_suffix()
        cidade = fake.city()
        uf = fake.country_code()
        pais = fake.current_country_code()
        cep = str(fake.postcode())

        comandoSQL = """ INSERT INTO CONTATO ("CODIGO", "TELEFONE_FIXO", "CELULAR", "ENDERECO", "BAIRRO", "CIDADE", "UF", "PAIS", "CEP", "CODIGO_CLIENTE") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        registro = (codigo, telefone_fixo, celular, endereco, bairro, cidade, uf, pais, cep, codigo_cliente)
        cursor.execute(comandoSQL, registro)

    conn.commit()
    print("Inserção realizada com sucesso!")
    conn.close()

except:
    # Exceção ampla, mas quis deixar assim mesmo
    print("Ocorreu um erro durante a inserção dos dados.")
    print("Conexao encerrada.")
    conn.close()

