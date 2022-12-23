from flask import Flask,flash,render_template,redirect, Response,jsonify
from flask.globals import request
import mysql.connector

import json

from dbpy import BancoDeDados
import pymysql as pydb
 
app = Flask(__name__)
bd = BancoDeDados()
mydb = pydb.connect(
        host="localhost",
        user="root",
        password="",
        database="database"
    )

mycursor = mydb.cursor()
        
#selecionar tudo da tabelaCadastro
@app.route("/tabelaCadastro", methods=["GET"])
def tabelaCadastro(id=1):
    mycursor.execute("Select * FROM Cadastro")
    fetchal = mycursor.fetchall()
    listaUsuarios = bd.selectCadastroCliente()
    count = 0
    return render_template("tabelaCadastro.html", lista = listaUsuarios,count = count,listando = fetchal, id = id)

#PAGINA DE LOGIN
@app.route("/")
def login():
    return "vazio"
   

#PAGINA INCIAL
@app.route("/home")
def home():
    mycursor.execute("Select * FROM Cadastro")
    fetchal = mycursor.fetchall()
    listaUsuarios = bd.selectCadastroCliente()
   
    return render_template("./admin/home/index.html", x = listaUsuarios )

# Pagina De cadastro cliente
@app.route("/CadastroCliente", methods = ['POST','GET'])
def CadastroCliente():
    if request.method == 'GET':
        return render_template("cadastroCliente.html")
    if request.method == 'POST':
        vendedor = request.form.get('vendedor')
        cliente = request.form.get('cliente')
        telefone = request.form.get('telefone')
        cidade = request.form.get('cidade')
        bairro = request.form.get('bairro')
        endereco = request.form.get('endereco')
        meio = request.form.get('meio')
        codigo = request.form.get('codigo')
        quantidade = request.form.get('quantidade')
        venda = request.form.get('venda')
        entrega = request.form.get('entrega')
        valor = request.form.get('valor')
        pagamento = request.form.get('pagamento')
        obs = request.form.get('obs')
        db = BancoDeDados()
        db.inserirCadastroCliente(vendedor,cliente,telefone,cidade,bairro,endereco,meio,codigo,quantidade,venda,entrega,valor,pagamento,obs)
        return redirect("Insert com sucesso")

#SELECIONANDO PELO ID
@app.route("/tabelaCadastro/<id>", methods = ["GET","POST"])
def tabelaCadastroID(id):
    usuario = bd.selectUserID(id)
    if request.method == "GET":
        return render_template("editcadastro.html",usuario = usuario)
    if request.method == "POST":
        vendedor = request.form.get('vendedor')
        cliente = request.form.get('cliente')
        telefone = request.form.get('telefone')
        cidade = request.form.get('cidade')
        bairro = request.form.get('bairro')
        endereco = request.form.get('endereco')
        meio = request.form.get('meio')
        codigo = request.form.get('codigo')
        quantidade = request.form.get('quantidade')
        venda = request.form.get('venda')
        entrega = request.form.get('entrega')
        valor = request.form.get('valor')
        pagamento = request.form.get('pagamento')
        obs = request.form.get('obs')
        db = BancoDeDados()
        db.UpdateTabelaCadastro(id,vendedor,cliente,telefone,cidade,bairro,endereco,meio,codigo,quantidade,venda,entrega,valor,pagamento,obs)
        return redirect("/home")
        

    
app.run(debug=True)