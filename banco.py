import sqlite3

ARQUIVO = "cardapio.db"

def criar_tabela():
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            categoria TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()
    
def popular_dados_iniciais():
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM itens")
    total = cursor.fetchone()[0]
    
    if total == 0:
        itens_iniciais = [
            ("X-Burger", 18.00, "Lanches"),
            ("X-Salada", 20.00, "Lanches"),
            ("Refrigerante", 6.00, "Bebidas"),
            ("Suco Natural", 8.00, "Bebidas"),
        ]
        cursor.executemany(
            "INSERT INTO itens (nome, preco, categoria) VALUES (?, ?, ?)",
            itens_iniciais
        )
        conexao.commit()
        
    conexao.close()
    
def buscar_itens():
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, preco, categoria FROM itens")
    resultados = cursor.fetchall()
    conexao.close()
    
    itens = []
    for nome, preco, categoria in resultados:
        itens.append({"nome": nome, "preco": preco, "categoria": categoria})
        
    return itens

def inserir_item(nome, preco, categoria):
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO itens (nome, preco, categoria) VALUES (?, ?, ?)",
        (nome, preco, categoria)
    )
    conexao.commit()
    conexao.close()