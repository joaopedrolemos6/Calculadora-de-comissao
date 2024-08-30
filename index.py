import tkinter as tk
from tkinter import messagebox

def calcular_comissao():
    try:
        valor_venda = float(entry_valor_venda.get())
        meses_parcelamento = int(entry_meses_parcelamento.get())
        taxa_comissao = float(entry_taxa_comissao.get())

        comissao_total = valor_venda * taxa_comissao / 100
        comissao_mensal = comissao_total / meses_parcelamento

        messagebox.showinfo("Resultado", f"Sua comissão mensal será de R${comissao_mensal:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

root = tk.Tk()
root.title("Calculadora de Comissão")
root.grid_columnconfigure(0, weight=1, uniform="col")
root.grid_columnconfigure(1, weight=2, uniform="col")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

label_valor_venda = tk.Label(root, text="Digite o valor da venda:")
label_meses_parcelamento = tk.Label(root, text="Digite o número de meses de parcelamento:")
label_taxa_comissao = tk.Label(root, text="Digite a taxa de comissão (%):")

entry_valor_venda = tk.Entry(root)
entry_meses_parcelamento = tk.Entry(root)
entry_taxa_comissao = tk.Entry(root)

button_calcular = tk.Button(root, text="Calcular", command=calcular_comissao)

label_valor_venda.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
label_meses_parcelamento.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
label_taxa_comissao.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

entry_valor_venda.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
entry_meses_parcelamento.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
entry_taxa_comissao.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

button_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

root.mainloop()
