from flask import Flask, request, render_template, redirect

app = Flask(__name__)

series = []

@app.route('/')
def index():
    return render_template('index.html', series=series)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        codigo = len(series)
        nome = request.form['nome']
        genero = request.form['genero']
        duracao = request.form['duracao']
        series.append([codigo, nome, genero, duracao])
        return redirect('/')

    return render_template('adicionar.html')
@app.route('/editar', methods=['GET', 'POST'])
def editar_series(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']

        series.append([codigo, nome, genero, duracao])
        return redirect('/')
    else:
        serie = series[codigo]
        return render_template('adicionar.html', serie=serie)

@app.route('/excluir_', methods=['GET', 'POST'])
def excluir_series(codigo):
    del series[codigo]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)