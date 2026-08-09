from flask import Flask, render_template, request, redirect
from banco import criar_tabela, popular_dados_iniciais, buscar_itens, inserir_item
import os

app = Flask(__name__)


@app.route("/")
def pagina_inicial():
    itens = buscar_itens()
    return render_template("index.html", titulo="Cardápio da Lanchonete", itens=itens)

@app.route("/adicionar", methods=["POST"])
def adicionar_item():
    nome = request.form.get("nome")
    preco = request.form.get("preco")
    categoria = request.form.get("categoria")
    
    inserir_item(nome, float(preco), categoria)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)