import tkinter as tk 
from tkinter import messagebox, filedialog 

class TodoApp:
    def __init__(self, root):
        self.root = root 
        self.root.title("To-Do list App")
        self.root.geometry("400x450") 
        
        self.tasks = [] 
        
        self.task_entry = tk.Entry(root, font=("Arial", 14)) 
        self.task_entry.pack(pady=10) 
        
        self.add_button = tk.Button(root, text="Add Task", width=15, command=self.add_task) 
        self.add_button.pack(pady=10) 
        
        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12)) 
        self.task_listbox.pack(pady=10) 
        
        self.delete_button = tk.Button(root, text="Delete Selected Task", command=self.delete_task) 
        self.delete_button.pack(pady=5) 
        
        self.clear_button = tk.Button(root, text="clear All Tasks", command=self.clear_tasks) 
        self.clear_button.pack(pady=5) 
        
        
        self.save_button = tk.Button(root, text="save Tasks", command=self.save_tasks) 
        self.save_button.pack(pady=5) 
        
    def add_task(self):
            task = self.task_entry.get() 
            if task:
                self.tasks.append(task) 
                self.update_task_list() 
                self.task_entry.delete(0, tk.END) 
            else:
                messagebox.showwarning("Warning", "you must select a task to delete.") 
                
                
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task.pop(index)
            self.update_task_list() 
        except IndexError:
            messagebox.showwarning("Warning", "you must select a task to delete.") 
                        
                        
    def clear_tasks(self):
        self.tasks.clear() 
        self.update_tasks_list()
        
                            
    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaulttextension=".txt",filetypes=[("Text Files", "*.txt")])
        
        if file_path:
            with open(file_path, "r") as file:
                self.tasks = file.read().splitlines()
                self.update_tasks_list()
                
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
                    
# if __name__ ==" __main__":
root = tk.Tk() 
app = TodoApp(root)
root.mainloop()