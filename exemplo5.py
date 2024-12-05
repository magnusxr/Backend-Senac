import mysql.connector

cnx = mysql.connector.connect(
    user="Python",
    password="aula@123",
    host="exemplo-aula.mysql.database.azure.com",
    port=3306,
    database="aula6",
    ssl_disabled=True
)

cursor = cnx.cursor()

query = "SELECT nome, CPF, cpf_responsavel2 FROM aluno"
cursor.execute(query)

resultados = cursor.fetchall()

for nome, CPF, cpf_responsavel2 in resultados:
    if cpf_responsavel2 is not None:
        print(f"Nome: {nome}. CPF: {CPF}")

cursor.close()
cnx.close()
