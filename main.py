       #Importação das bibliotecas tkinter
from tkinter import *
from tkinter import messagebox

import app
import tkinter as tk
from tkinter import messagebox

        #Definição da classe principal e interface inicial de login
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Shop")
        

        self.username_label = tk.Label(root, text="Usuário:")
        self.username_label.pack()
        
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        
        self.password_label = tk.Label(root, text="Senha:")
        self.password_label.pack()
        
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()
        
        self.login_button = tk.Button(root, text="Entrar", command=self.login)
        self.login_button.pack()
 

        # Credenciais de nome do usuário e senha
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "andreleandro" and password == "1234":
            self.root.destroy()
            self.open_main_window()
        else:
            tk.messagebox.showwarning(title='Erro', message='Senha Incorreta')

    def open_main_window(self):
        main_window = tk.Tk()
        main_window.title("Pet Shop")
        
        # Crie uma instância da TelaPrincipal do arquivo tela_un.py
        app.MainApp(main_window)
        
        main_window.mainloop()

        #dimensões da tela de login
root = tk.Tk()
root.geometry("1000x350")
login_app = LoginApp(root)
root.mainloop()


