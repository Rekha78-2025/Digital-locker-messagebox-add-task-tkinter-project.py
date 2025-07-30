import tkinter as tk 
import time 


def update_time():
    current_time = time.strftime('%H:%M:%S %p') 
    time_label.config(text=current_time) 
    time_label.after(1000, update_time) 
    
    
root = tk.Tk() 
root.title("Digital clock") 
    
time_label = tk.Label(root, font=("Arial", 40, "bold"), bg="black", fg="white") 
time_label.pack(padx=20, pady=20) 

update_time() 
    
root.mainloop()  