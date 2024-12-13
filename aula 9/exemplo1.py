import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()

nome_aluno = input("Digite o turno do aluno que deseja buscar: ")

query = "SELECT nome, idade, turno FROM aluno where nome = %s;"  # %s = input
cursor.execute(query, (nome_aluno,))  #  "," é necessário

resultados = cursor.fetchall()

if resultados:
    for nome, idade, turno in resultados:
        print(f"Aluno: {nome}. Idade: {idade}. Turno: {turno}.")
else:
    print("Nenhum aluno encontrado com este nome.")

cursor.close
cnx.close