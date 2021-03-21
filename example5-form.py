from flask import Flask
from flask import render_template
from flask import redirect, request, url_for


app = Flask(__name__)

lista = ['savio', 'lucas', 'maria', 'shirley']


@app.route('/')
def inicio():
    return render_template('aula05/inicio.html', nomes=lista)


@app.route('/novo')
def novo():
    return render_template('aula05/novo.html')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.values.get('nome')
    lista.append(nome)
    return redirect(url_for('inicio'))


@app.route('/editar/<id>')
def editar(id):
    id = int(id)
    return render_template('aula05/editar.html', nome=lista[id], id=id)


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
    app.debug = True
    app.run(host='0.0.0.0')
