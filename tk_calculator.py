import tkinter as tk
from tkinter import ttk

def calculate(op):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        if op == "+":
            result.set(n1 + n2)
        elif op == "-":
            result.set(n1 - n2)
        elif op == "*":
            result.set(n1 * n2)
        elif op == "/":
            result.set("Cannot divide by 0" if n2 == 0 else n1 / n2)
    except ValueError:
        result.set("Invalid input")

# Window setup
root = tk.Tk()
root.title("Elegant Pink Calculator")
root.geometry("450x500")
root.configure(bg="#fbe4e6")

# Style configuration
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
                font=("Segoe UI", 14),
                padding=10,
                foreground="#ffffff",
                background="#d291bc")
style.map("TButton",
          background=[('active', '#b36b9d')])

# Heading
tk.Label(root,
         text="💗 Elegant Calculator 💗",
         font=("Georgia", 20, "bold"),
         bg="#fbe4e6",
         fg="#b85c9e").pack(pady=20)

# Input fields
entry_frame = tk.Frame(root, bg="#fbe4e6")
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="First Number:", font=("Segoe UI", 13), bg="#fbe4e6").grid(row=0, column=0, padx=10, pady=5)
entry1 = ttk.Entry(entry_frame, font=("Segoe UI", 14), width=20)
entry1.grid(row=0, column=1)

tk.Label(entry_frame, text="Second Number:", font=("Segoe UI", 13), bg="#fbe4e6").grid(row=1, column=0, padx=10, pady=5)
entry2 = ttk.Entry(entry_frame, font=("Segoe UI", 14), width=20)
entry2.grid(row=1, column=1)

# Buttons
button_frame = tk.Frame(root, bg="#fbe4e6")
button_frame.pack(pady=30)

ttk.Button(button_frame, text="Add", command=lambda: calculate("+")).grid(row=0, column=0, padx=15, pady=10)
ttk.Button(button_frame, text="Subtract", command=lambda: calculate("-")).grid(row=0, column=1, padx=15, pady=10)
ttk.Button(button_frame, text="Multiply", command=lambda: calculate("*")).grid(row=1, column=0, padx=15, pady=10)
ttk.Button(button_frame, text="Divide", command=lambda: calculate("/")).grid(row=1, column=1, padx=15, pady=10)

# Result Display
result = tk.StringVar()
tk.Label(root, text="Result:", font=("Segoe UI", 14, "bold"), bg="#fbe4e6", fg="#b85c9e").pack(pady=10)
tk.Entry(root, textvariable=result, font=("Segoe UI", 16), width=30, justify='center', state='readonly').pack(pady=5)

root.mainloop()
