import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

# render_template: função do Flask para renderizar arquivos HTML (templates)
# request: objeto que contém dados da requisição HTTP, como os dados do formulário
# redirect e url_for: funções para redirecionar o usuário para outra página dentro da aplicação

app = Flask(__name__, template_folder='templates')

# template_folder='templates': define que os templates HTML estarão na pasta chamada templates dentro do diretório onde o script está
# indica ao Flask que os arquivos .html estão dentro de "templates"

db_config = {
    'user': 'python',
    'password': 'aula@123',
    'host': 'exemploaulacaio.mysql.database.azure.com',
    'port': 3306,
    'database': 'escolasenac'
}

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/cadastro', methods=['GET', 'POST']): define a rota /cadastro para responder a métodos HTTP GET e POST
# quando o método é POST, os dados do formulário são capturados usando request.form.get(), onde:
# usuario: obtém o valor do campo usuario do formulário
# senha: obtém o valor do campo senha do formulário

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = "INSERT INTO usuario_secretaria (usuario, senha) VALUES (%s, %s)"
        cursor.execute(query, (usuario, senha))
        cnx.commit()  # confirma a transação, ou seja, realiza a inserção no banco de dados
        cursor.close()
        cnx.close()

        return redirect(url_for('cadastro'))
    else:
        return render_template('cadastro.html')
    
if __name__ == '__main__':
    app.run(debug=True)

# debug=True faz com que o servidor reinicie automaticamente se houver mudanças no código e também exibe mensagens de erro mais detalhadas
