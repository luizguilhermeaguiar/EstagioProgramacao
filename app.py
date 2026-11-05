from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem-vindo ao Sistema de Vendas!"