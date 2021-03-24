from flask import Flask
from flask import render_template
from flask import redirect, request, url_for
from flask import flash, session


app = Flask(__name__)
app.secret_key = "super secret key"

lista = ['savio', 'lucas', 'maria', 'shirley']


@app.route('/')
def inicio():
    return render_template('aula06/inicio.html', nomes=lista)


@app.route('/login')
def login():
    return render_template('aula06/login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    password = request.values.get('password')
    nome = request.values.get('nome')
    if nome.strip() == 'rafael' and password.strip() == '1234':
        session['usuario_logado'] = nome
        return redirect(url_for('inicio'))
    else:
        flash('Você digitou um usuário ou senha inválidos!')
        return redirect(url_for('login'))


@app.route('/novo')
def novo():
    return render_template('aula06/novo.html')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.values.get('nome')
    lista.append(nome)
    return redirect(url_for('inicio'))


@app.route('/editar/<id>')
def editar(id):
    id = int(id)
    return render_template('aula06/editar.html', nome=lista[id], id=id)


@app.route('/atualizar', methods=['POST'])
def atualizar():
    nome = request.values.get('nome')
    id = int(request.values.get('id'))
    lista[id] = nome
    return redirect(url_for('inicio'))


@app.route('/deletar/<id>')
def deletar(id):
    id = int(id)
    del lista[id]
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
