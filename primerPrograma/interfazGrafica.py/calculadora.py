import tkinter as tk
from tkinter import messagebox

def on_click(symbol):
    current =entry.get()

    if symbol == "C":
        entry.delete(0, tk.END)
    elif symbol == "=":
        try: 
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Operación no válida")
    else: entry.insert(tk.END, symbol)


root=tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4, padx=10,pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
]

row_val = 1
col_val = 0

for button in buttons:
    action = (lambda x=button: on_click(x))
    b = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action)
    b.grid(row=row_val, column=col_val, sticky="nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()