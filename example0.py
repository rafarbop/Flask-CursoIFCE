from flask import Flask

app = Flask("example0")


@app.route("/")
def index():
    return '''
        <h1 style="text-align:center;padding: 6vh 2vw">
            Index Page
        </h1>
        <div style="text-align:center;">
            <p>
                <a href="/hello">Página de Boas Vindas!</a>
            </p>
            <p>
                <a href="/user">Página de Usuários!</a>
            </p>
        </div>
        '''


@app.route("/hello")
def hello():
    return "Hello World"


@app.route("/user/")
def user():
    return '''
        <h1 style="text-align:center;padding: 6vh 2vw">
            User's Page
        </h1>
        <div style="text-align:center;">
            <p>
                Nenhum usuário cadastrado!
            </p>
            <p>
                Digite seu nome no barra de endereços após "/user/"
            </p>
        </div>
        '''


@app.route("/user/<username>")
def show_user_info(username):
    return f'Usuário é {username}'


@app.route("/teste/→")
def teste_simbolos():
    return 'Deu certo'


@app.route("/teste/-<int:numero>")
def teste_urls(numero):
    return f'Deu certo o número {numero}'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
