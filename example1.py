from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'''
    <h1 style='padding:4vh 2vw;text-align:center'>
        Bem vindo ao teste de flask!</h1>
    <a href="/user">Página Nome</a>
    '''


@app.route('/user/')
@app.route('/user/<nome>')
def user(nome=None):
    return f'''
    <h1 style="padding:4vh 2vw;text-align:center">
        O usuário cadastrado é {nome if nome!=None else 'ERRO'}
    </h1>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0')