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
query = "SELECT nome, endereco FROM aluno;"
cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
for nome, endereco in resultados:
    print(f"Nome: {nome}. Endereço: {endereco}.")

# Fechando o cursor e a conexão
cursor.close()
cnx.close()
