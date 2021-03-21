from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('aula03/base.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('aula03/hello.html', name=name)


@app.route('/filho')
def filho():
    return render_template('aula03/filho.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')