import tkinter as tk
from database import  criar_banco, inserir_venda, listar_vendas

def registrar_venda():
    produto = entry_produto.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()

    if produto and quantidade and preco:
        try:
            quantidade = int(quantidade)
            preco = float(preco)
        except ValueError:
            tk.messagebox.showerror("Erro", "Quantidade deve ser inteiro, e preço número")

    inserir_venda(produto, quantidade, preco)
    entry_produto.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    atualizar_lista()
    
def atualizar_lista():
    lista.delete(0, tk.END)
    for venda in listar_vendas():
        lista.insert(tk.END, venda)

########### interface
root = tk.Tk()
root.title("Registro de Vendas")
root.configure(bg="#83ADB7")

tk.Label(root, text="Produto").pack()
entry_produto = tk.Entry(root)
entry_produto.pack()

tk.Label(root, text="Quantidade").pack()
entry_quantidade = tk.Entry(root)
entry_quantidade.pack()

tk.Label(root, text="Preço").pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

tk.Button(root, text="Registrar Venda", command=registrar_venda).pack(pady=5)

lista = tk.Listbox(root, width=50)
lista.pack()

criar_banco()
atualizar_lista()
root.mainloop()