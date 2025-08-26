import tkinter as tk
from tkinter import messagebox


def verificar_nota():
    #O que faz: pega o valor que o usuário digitou no Entry do Tkinter e guarda na variável nota_texto.
    nota_texto = entry_nota.get()
    #nota_texto.replace(".", "", 1):  .isdigit(): Verifica se a string contém apenas números.
    if nota_texto.replace(".", "", 1).isdigit():  # verifica se é número (aceita decimal)
        nota = float(nota_texto)


        if nota >= 7:
            resultado = "Aprovado!!"
        elif nota >= 5:
            resultado = "Recuperação !!"
        else:
            resultado = "Reprovado !!"
       
        messagebox.showinfo("Resultado", f"Situação: {resultado}")
    else:
        messagebox.showerror("Erro", "Digite um número válido.")


# Janela principal
root = tk.Tk()
root.title("Verificador de Nota")
root.geometry("300x200")
root.configure(bg="#F0E68C")  # fundo amarelo claro


# Widgets
tk.Label(root, text="Digite a nota do aluno:", bg="#F0E68C", fg="black", font=("Arial", 11, "bold")).pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)


tk.Button(root, text="Verificar", command=verificar_nota, bg="blue", fg="white", font=("Arial", 11, "bold")).pack(pady=15)


root.mainloop()
