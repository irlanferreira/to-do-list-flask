import mysql.connector

def conectar():
    try:
        con = mysql.connector.connect(host='localhost', user='root',password='04052005',database='todo')
        return con
    except mysql.connector.Error as erro:
        print(erro)
conectar()

def pegardados(id=False):
    with conectar() as con:
        cursor = con.cursor()
        if id == False:
            cursor.execute('SELECT * FROM tarefas')
            res = cursor.fetchall()
        else:
            cursor.execute(f'SELECT * FROM tarefas where id = {id}')
            res = cursor.fetchall()
        return res

def inserir(nome):
    with conectar() as con:
        cursor = con.cursor()
        cursor.execute(f'INSERT INTO tarefas (nome, feito) VALUES ("{nome}", "off")')
        con.commit()

def deletar(id):
    with conectar() as con:
        cursor = con.cursor()
        cursor.execute(f'DELETE FROM tarefas WHERE id = {id};')
        con.commit()

def editar(id, novo_nome, feito):
    with conectar() as con:
        cursor = con.cursor()
        cursor.execute(f"UPDATE tarefas SET nome = '{novo_nome}'")
        cursor.execute(f'UPDATE tarefas SET feito = "{feito}" where id = {id}')
        con.commit()