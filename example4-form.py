from flask import Flask
from flask import render_template
from flask import redirect, request, url_for


app = Flask(__name__)

lista = ['savio', 'lucas', 'maria', 'shirley']


@app.route('/')
def inicio():
    return render_template('aula04/inicio.html', nomes=lista)


@app.route('/novo')
def novo():
    return render_template('aula04/novo.html')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.values.get('nome')
    lista.append(nome)
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
