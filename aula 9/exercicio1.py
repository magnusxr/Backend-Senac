import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()

idade_min = input("Digite a idade mínima desejada: ")
idade_max = input("Digite a idade máxima desejada: ")

query = "SELECT nome, idade, idturma, alergias FROM aluno WHERE alergias NOT LIKE 'Leite' AND idade BETWEEN %s and %s"
cursor.execute(query, (idade_min,idade_max,))

resultados = cursor.fetchall()

if resultados:
    for nome, idade, idturma, alergias in resultados:
        print(f"Aluno: {nome}. Idade: {idade}. Turma: {idturma}.")
else:
    print("Nenhum aluno encontrado.")

cursor.close
cnx.close
