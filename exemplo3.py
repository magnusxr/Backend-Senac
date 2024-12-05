import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="Python",
    password="aula@123",
    host="exemplo-aula.mysql.database.azure.com",
    port=3306,
    database="aula6",
    ssl_disabled=True     
)

# Criação do cursor
cursor = cnx.cursor()

# Consulta
query = "SELECT nome, idade, tipo_sanguineo FROM aluno"
cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
for nome, idade, tipo_sanguineo in resultados:
    if tipo_sanguineo in ["B+", "B-", "O+", "O-"]:
        print(f"Posível doador: {nome}, {idade} anos.")

# Fechando o cursor e a conexão
cursor.close()
cnx.close()
