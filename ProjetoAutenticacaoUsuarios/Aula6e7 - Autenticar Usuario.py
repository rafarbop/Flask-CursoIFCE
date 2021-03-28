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
    proximo = request.values.get('proximo')
    return render_template('aula06/login.html', proximo=proximo)


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('login'))


@app.route('/autenticar', methods=['POST'])
def autenticar():
    password = request.values.get('password')
    nome = request.values.get('nome')
    proximo = request.values.get('proximo')
    if nome.strip() == 'rafael' and password.strip() == '1234':
        session['usuario_logado'] = nome
        return redirect(proximo)
    else:
        flash('Você digitou um usuário ou senha inválidos!')
        return redirect(url_for('login'))


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo=url_for('novo')))
    else:
        return render_template('aula06/novo.html')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.values.get('nome')
    lista.append(nome)
    return redirect(url_for('inicio'))


@app.route('/editar/<id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo=url_for('editar', id=id)))
    else:
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
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo=url_for('deletar', id=id)))
    else:
        id = int(id)
        del lista[id]
        return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
