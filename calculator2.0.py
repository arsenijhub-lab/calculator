import tkinter as tk
from tkinter import messagebox 


current_input = ""  
result_shown = False 
def on_button_click(button_text):
    global current_input, result_shown
    if button_text == '=':
        try:
            expression = current_input.replace('x', '*').replace('÷', '/')
            
           
            if not expression or expression[-1] in '+-*/':
                return 
                
            result = eval(expression)
            entry.delete(0, tk.END) 
            entry.insert(0, str(result)) 
            current_input = str(result) 
            result_shown = True
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(0, "Помилка")
            current_input = ""
            result_shown = True
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Помилка")
            current_input = ""
            result_shown = True
            
    elif button_text == 'C': 
        current_input = ""
        entry.delete(0, tk.END)
        result_shown = False
        
    else:
        if result_shown:
            entry.delete(0, tk.END)
            result_shown = False
            
       
        current_input += button_text
        entry.delete(0, tk.END) 
        entry.insert(0, current_input) 


root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.configure(bg="#020202") 


entry = tk.Entry(root, font=('Arial', 24), bg="#F7F6F6", fg="black", justify='right', bd=0)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)


buttons_config = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0) 
]

button_params = {'font': ('Arial', 18), 'bg': "#FFFFFF", 'fg': "black", 'bd': 0, 'relief': tk.RAISED}


for (text, row, col) in buttons_config:
    
    button = tk.Button(root, text=text, **button_params, command=lambda t=text: on_button_click(t))
    
   
    if text == '0':
        button.grid(row=row, column=col, columnspan=1, sticky="nsew", padx=2, pady=2)
    elif text == '=':
        button.grid(row=row, column=col, columnspan=1, sticky="nsew", padx=2, pady=2)
    elif text == 'C':
        button.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=2, pady=2) 
    else:
        button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)


for i in range(6): 
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
