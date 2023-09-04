import tkinter as tk
from tkinter import ttk, messagebox
import csv

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Shop")

        # Entrada de dados
        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.place(x=15, y =50)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.place(x=15, y =75)

        self.raca_label = tk.Label(root, text="Raça:")
        self.raca_label.place(x=15, y =100)
        self.raca_entry = tk.Entry(root)
        self.raca_entry.place(x=15, y =125)

        self.idade_label = tk.Label(root, text="Idade:")
        self.idade_label.place(x=15, y =150)
        self.idade_entry = tk.Entry(root)
        self.idade_entry.place(x=15, y =175)

        # Botões para realizar operação CRUD
        self.create_button = tk.Button(root, text="Inserir", command=self.create_record)
        self.create_button.place(x=100, y=300)

        self.update_button = tk.Button(root, text="Atualizar", command=self.update_record)
        self.update_button.place(x=300, y=300)

        self.delete_button = tk.Button(root, text="Deletar", command=self.delete_record)
        self.delete_button.place(x= 400, y=300)

        self.read_button = tk.Button(self.root, text="Visualizar", command=self.read_records)
        self.read_button.place(x= 200, y=300)

        # Tabela para exibição dos registros
        self.tree = ttk.Treeview(root, columns=("Nome", "Raça", "Idade"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Raça", text="Raça")
        self.tree.heading("Idade", text="Idade")
        self.tree.pack()
        
        # Variável para armazenar o índice do registro selecionado
        self.selected_index = None

        # Lidar com a seleção de um item na Treeview
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        


    def read_records(self):
        try:
            # Abra o arquivo de texto (CSV) para leitura
            with open("dados.csv", "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    registro2 = (row[0],row[1],row[2])
                    self.tree.insert("", "end", values=registro2)
        except FileNotFoundError:
            messagebox.showinfo("Arquivo Não Encontrado", "O arquivo de dados não foi encontrado.")

        # Obtendo dados de entrada
    def create_record(self):
        nome = self.nome_entry.get()
        raca = self.raca_entry.get()
        idade = self.idade_entry.get()


        # Criação de um registro como string formatada
#        registro = f"Nome: {nome}, Raça: {raca}, Idade: {idade}"
        registro = (nome, raca, idade)
        self.tree.insert("", "end", values=registro)


        # Limpando as entradas após a criação do registro
        self.nome_entry.delete(0, tk.END)
        self.raca_entry.delete(0, tk.END)
        self.idade_entry.delete(0, tk.END)

    # Escrevendo o novo registro no arquivo de texto (CSV)
        with open("dados.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(registro)
        
        #Mensagem de sucesso para confirmar registro
        messagebox.showinfo("Sucesso", "Registro criado com sucesso!")



        # Atualizando o item selecionado na tabela
    def update_record(self):
        if self.selected_index is not None:
            nome = self.nome_entry.get()
            raca = self.raca_entry.get()
            idade = self.idade_entry.get()


            self.tree.item(self.selected_index, values=(nome, raca, idade))
            registro3 = (nome,raca,idade)
            with open("dados.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(registro3)
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
        else:
            messagebox.showinfo("Nenhum Item Selecionado", "Selecione um item para atualizar.")

        # Obtendo o índice do item selecionado
    def on_select(self, event):
        
        selected_item = self.tree.selection()
        if selected_item:
            self.selected_index = selected_item[0]
            
            # Preenchendo as entradas com os valores do item selecionado para facilitar a atualização
            values = self.tree.item(self.selected_index, "values")
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.insert(0, values[0])
            self.raca_entry.delete(0, tk.END)
            self.raca_entry.insert(0, values[1])
            self.idade_entry.delete(0, tk.END)
            self.idade_entry.insert(0, values[2])

        else:
            self.selected_index = None

    def delete_record(self):

    # Obtendo o item selecionado na tabela
        selected_item = self.tree.selection()

        if selected_item:
            # Obtendo os valores do item selecionado
            values = self.tree.item(selected_item, "values")

        # Removendo o item selecionado da tabela
            self.tree.delete(selected_item)
        # Removendo o item selecionado do arquivo CSV (base de dados)
            self.remove_from_csv(values)    
        else:
                messagebox.showinfo("Nenhum Item Selecionado", "Selecione um item para excluir.")

def remove_from_csv(self,values_to_remove):
    try:
        # Abrir o arquivo de texto (CSV) para leitura e escrita
        with open("dados.csv", "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Identificando a linha que contém os valores a serem removidos
        rows_to_update = []
        for row in rows:
            if tuple(row) != tuple(values_to_remove):
                rows_to_update.append(row)

        if rows_to_update:
            # Removendo as linhas que contêm os valores a serem removidos
            for row in rows_to_update:
                rows.write(row)
        

        messagebox.showinfo("Sucesso", "Registro excluído com sucesso da Base!")
    except FileNotFoundError:
        messagebox.showinfo("Arquivo Não Encontrado", "O arquivo de dados não foi encontrado.")

#        with open("dados.csv", "a", newline="") as file:
 #           writer = csv.writer(file)
 #           writer.writerow(registro)
            
#root = tk.Tk()
#root.geometry("1000x350")
#login_app = MainApp(root)
#root.mainloop()

