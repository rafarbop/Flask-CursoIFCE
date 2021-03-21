from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('hello'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('aula03/hello.html', name=name)


app.debug = True
app.run(host='0.0.0.0')
