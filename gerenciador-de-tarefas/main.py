import tkinter as tk
from tkinter import messagebox, ttk
import json

# Arquivo onde as tarefas serão salvas
FILE_NAME = "tasks.json"

def load_tasks():
    """Carrega as tarefas do arquivo JSON."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    """Salva as tarefas no arquivo JSON."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Adiciona uma nova tarefa."""
    task = task_entry.get().strip()
    if task:
        tasks.append({"text": task, "done": False})
        update_listbox()
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Aviso", "A tarefa não pode estar vazia!")

def remove_task():
    """Remove a tarefa selecionada."""
    try:
        selected_index = listbox.curselection()[0]
        del tasks[selected_index]
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

def edit_task():
    """Edita a tarefa selecionada."""
    try:
        selected_index = listbox.curselection()[0]
        new_text = task_entry.get().strip()
        if new_text:
            tasks[selected_index]["text"] = new_text
            update_listbox()
            save_tasks()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "A nova tarefa não pode estar vazia!")
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para editar!")

def toggle_task():
    """Alterna o estado de conclusão da tarefa selecionada."""
    try:
        selected_index = listbox.curselection()[0]
        tasks[selected_index]["done"] = not tasks[selected_index]["done"]
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para marcar/concluir!")

def update_listbox():
    """Atualiza a exibição da lista de tarefas."""
    listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        text = task["text"]
        display_text = f"✔ {text}" if task["done"] else text
        listbox.insert(tk.END, display_text)

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciador de Tarefas")
root.geometry("500x600")
root.configure(bg="#f0f0f0")
root.resizable(True, True)

# Criando frame principal
main_frame = ttk.Frame(root, padding=10)
main_frame.pack(expand=True, fill="both")

# Criando widgets
task_entry = ttk.Entry(main_frame, width=50)
add_button = ttk.Button(main_frame, text="Adicionar", command=add_task)
edit_button = ttk.Button(main_frame, text="Editar", command=edit_task)
remove_button = ttk.Button(main_frame, text="Remover", command=remove_task)
toggle_button = ttk.Button(main_frame, text="Concluir", command=toggle_task)
listbox = tk.Listbox(main_frame, width=60, height=15, selectbackground="#42a5f5", font=("Arial", 10))

# Layout responsivo
task_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
add_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
edit_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
toggle_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
remove_button.grid(row=1, column=3, padx=5, pady=5, sticky="ew")
listbox.grid(row=2, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

# Ajustar redimensionamento
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)
main_frame.rowconfigure(2, weight=1)

# Carregar tarefas ao iniciar
tasks = load_tasks()
update_listbox()

# Iniciar loop da interface gráfica
root.mainloop()
