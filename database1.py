import sqlite3

def criar_banco():
    """Criar banco e tabela"""
    conn = sqlite3.connect("vendas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT,
            quantidade INTERGER,
            preco REAL       
        )
    """)
    conn.commit()
    conn.close()

def inserir_venda(produto, quantidade, preco):
    conn = sqlite3.connect("vendas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vendas(produto,quantidade,preco) VALUES (?, ?, ?)",
                   (produto,quantidade,preco))
    conn.commit()
    conn.close()

def listar_vendas():
    conn = sqlite3.connect("vendas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendas")
    registros = cursor.fetchall()
    conn.close()
    return registros
    