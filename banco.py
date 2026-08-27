import psycopg2
import os


def conectar():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
    )
    
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            categoria TEXT NOT NULL
        )
    """)
    conexao.commit()
    cursor.close()
    conexao.close()
    
    
def popular_dados_iniciais():
    conexao = conectar()
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
            "INSERT INTO itens (nome, preco, categoria) VALUES (%s, %s, %s)",
            itens_iniciais
        )
        conexao.commit()
        
    cursor.close()
    conexao.close()
    
    
def buscar_itens():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, preco, categoria FROM itens")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    
    itens = []
    for nome, preco, categoria in resultados:
        itens.append({"nome": nome, "preco": preco, "categoria": categoria})
        
    return itens


def inserir_item(nome, preco, categoria):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO itens (nome, preco, categoria) VALUES (%s, %s, %s)",
        (nome, preco, categoria)
    )
    conexao.commit()
    cursor.close()
    conexao.close()