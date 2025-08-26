import tkinter as tk
from tkinter import messagebox

def verificar_senha():
    senha = entry_senha.get() #Espaçamento significa que está dentro da função #Irá pegar a informação
    
    if len(senha) == 8:
        resultado = "Senha válida"
        #print(resultado)
        messagebox.showinfo("Resultado", f"Situação: {resultado}") 
    else:
        resultado = "Errado"
        #print(resultado)
        messagebox.showerror("Errado", "Senha inválida!.")  
#Janela principal
root = tk.Tk()
root.title("Verificador de senha")
root.geometry("300x200") #Altura e largura da janela
root.configure(bg="#F0E68C") #Fundo amarelo

#Widgets 
tk.Label(root, text="Digite sua senha:", bg="#F0E68C", fg="black", font=("Arial", 11, "bold")).pack(pady=10)
entry_senha = tk.Entry(root)
entry_senha.pack(pady=5)

tk.Button(root, text="Verificar", command=verificar_senha, bg="blue", fg="white", font=("Arial", 11, "bold")).pack(pady=15)

root.mainloop()