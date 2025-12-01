import tkinter as tk

# Button click function
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Clear screen
def clear():
    entry.delete(0, tk.END)

# Calculate result safely
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("GUI Calculator")
root.config(bg="black")

# Display box
entry = tk.Entry(root, width=15, borderwidth=8, font=("Arial", 22), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button style
button_params = {"width": 5, "height": 2, "font": ("Arial", 18)}

# Number Buttons
numbers = [
    (1, 3, 0), (2, 3, 1), (3, 3, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (7, 1, 0), (8, 1, 1), (9, 1, 2),
    (0, 4, 1)
]

for (num, r, c) in numbers:
    tk.Button(root, text=str(num), **button_params,
              bg="#4CAF50", fg="white",
              command=lambda n=num: click_button(n)).grid(row=r, column=c)

# Operator Buttons
operators = [
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 3),
    ("%", 4, 0),
    ("^", 4, 2)
]

for (op, r, c) in operators:
    tk.Button(root, text=op, **button_params,
              bg="#FF9800", fg="white",
              command=lambda o=op: click_button("**" if o == "^" else o)).grid(row=r, column=c)

# Clear and Equals Button
tk.Button(root, text="C", **button_params,
          bg="#f44336", fg="white",
          command=clear).grid(row=5, column=0)

tk.Button(root, text="=", **button_params,
          bg="#2196F3", fg="white",
          command=calculate).grid(row=5, column=1, columnspan=3, sticky="we")

root.mainloop()
