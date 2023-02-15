from flask import Flask, request, render_template, redirect, url_for
import mysql.connector, model


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', tarefas=model.pegardados())

@app.route('/adicionar', methods=['POST','GET'])
def adicionar():
    if request.method == 'POST':
        tarefa_nome = request.form['tarefa']
        model.inserir(tarefa_nome)
        return redirect(url_for('index'))
    else:
        return render_template('adicionar.html')
    
@app.route('/excluir/<id>/')
def excluir(id):
    model.deletar(str(id))
    return redirect(url_for('index'))

@app.route('/editar/<id>/', methods=['POST','GET'])
def editar(id):
    if request.method == 'GET':
        dados = model.pegardados(id)[0]
        return render_template('editar.html',dados=dados)
    else:
        tarefa_nome = request.form['tarefa']
        try:
            feito = request.form['feito']
        except:
            feito = 'off'
        print(feito)
        model.editar(id, tarefa_nome, feito)
        return redirect(url_for('index'))

app.run(debug=True)
