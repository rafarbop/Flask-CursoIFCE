from flask import Flask
from flask import render_template
from flask import redirect, request, url_for
from flask import flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column('nome', db.String(100))

    def __init__(self, nome):
        self.nome = nome


@app.route('/')
def inicio():
    return render_template('aula08/inicio.html', usuarios=users.query.all())


@app.route('/login')
def login():
    proximo = request.values.get('proximo')
    return render_template('aula08/login.html', proximo=proximo)


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
        return render_template('aula08/novo.html')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.values.get('nome')
    usuario = users(nome)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('inicio'))


@app.route('/editar/<id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo=url_for('editar', id=id)))
    else:
        usuario = users.query.filter_by(_id=id).first()
        return render_template('aula08/editar.html',
                               nome=usuario.nome,
                               id=usuario._id)


@app.route('/atualizar', methods=['POST'])
def atualizar():
    nome = request.values.get('nome')
    id = int(request.values.get('id'))
    usuario_novo_nome = users.query.filter_by(_id=id).first()
    usuario_novo_nome.nome = nome
    db.session.commit()
    return redirect(url_for('inicio'))


@app.route('/deletar/<id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo=url_for('deletar', id=id)))
    else:
        id = int(id)
        usuario_a_deletar = users.query.filter_by(_id=id).first()
        db.session.delete(usuario_a_deletar)
        db.session.commit()
        return redirect(url_for('inicio'))


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=True)
