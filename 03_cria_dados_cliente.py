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
        cpf = str(fake.pyint(min_value=10000000000, max_value=99999999999, step=1))
        nome = fake.name()
        idade = fake.pyint(min_value=18, max_value=150, step=1)
        sexo = str(fake.pyint(min_value=1, max_value=2, step=1))
        limite = fake.pyfloat(left_digits=6, right_digits=2, positive=True, min_value=100, max_value=100000)
        volume = fake.pyfloat(left_digits=3, right_digits=0, positive=True, min_value=1, max_value=100)

        comandoSQL = """ INSERT INTO CLIENTE ("CODIGO", "CPF", "NOME", "IDADE", "SEXO", "LIMITE_CREDITO", "VOLUME_COMPRA") VALUES (?, ?, ?, ?, ?, ?, ?)"""
        registro = (codigo, cpf, nome, idade, sexo, limite, volume)
        cursor.execute(comandoSQL, registro)

    conn.commit()
    print("Inserção realizada com sucesso!")
    conn.close()

except:
    # Exceção ampla, mas quis deixar assim mesmo
    print("Ocorreu um erro durante a inserção dos dados.")
    print("Conexao encerrada.")
    conn.close()

