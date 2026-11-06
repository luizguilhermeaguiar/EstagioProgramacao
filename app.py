from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/registrar-venda", methods=["POST"])
def registrar_venda():
    nome_produto = request.form.get("produto")
    if nome_produto is None: 
        return render_template("index.html", erro="Erro: nome não localizado")

    nome_produto = nome_produto.strip()
    
    if not nome_produto:
        return render_template("index.html", erro="Erro: o nome do produto não pode estar vazio!")
    
    try: 
        preco_unitario = float(request.form.get("preco"))
        if preco_unitario <= 0: 
            return render_template("index.html", erro="Preço inválido!")

        if not math.isfinite(preco_unitario):
            return render_template("index.html", erro="Preço inválido!")

    except (ValueError, TypeError):
        return render_template("index.html", erro="Preço inválido!")
        
    try: 
        quantidade = int(request.form.get("quantidade"))
        if quantidade <= 0: 
            return render_template("index.html", erro="Erro: a quantidade deve ser maior que zero!")
            
    except (ValueError, TypeError):
        return render_template("index.html", erro="Erro: Quantidade inválida!")
    
    subtotal = preco_unitario * quantidade
    
    return render_template("resultado.html", produto=nome_produto, preco=preco_unitario, quantidade=quantidade, subtotal=subtotal)