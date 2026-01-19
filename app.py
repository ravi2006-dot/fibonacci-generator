import tkinter as tk
from tkinter import messagebox

def generate_fibonacci():
    try:
        n = int(entry.get())
        if n <= 0:
            messagebox.showerror("Error", "Enter a positive number")
            return

        a, b = 0, 1
        series = ""

        for i in range(n):
            series += str(a) + " "
            a, b = b, a + b

        result_label.config(text=series)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create window
root = tk.Tk()
root.title("Fibonacci Generator")
root.geometry("400x250")

# Widgets
tk.Label(root, text="Fibonacci Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter number of terms:").pack()
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_fibonacci).pack(pady=10)

result_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()
