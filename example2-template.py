from flask import Flask, render_template

app = Flask('template0')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


app.run(host='0.0.0.0')
