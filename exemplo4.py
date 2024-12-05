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

query = "SELECT nome, naturalidade, sexo FROM aluno"
cursor.execute(query)

resultados = cursor.fetchall()

print(f"Alunos cariocas:")
for nome, naturalidade, sexo in resultados:
    if sexo == "M" and naturalidade == "Rio de Janeiro":
        print(f"{nome}, {naturalidade}")

print(f"\nAlunas paulistanas:")
for nome, naturalidade, sexo in resultados:
    if sexo == "F" and naturalidade == "São Paulo":
        print(f"{nome}, {naturalidade}")

cursor.close()
cnx.close()
