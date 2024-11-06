import tkinter as tk
from tkinter import messagebox

def find_min_max():
    try:
        numbers = list(map(float, entry.get().split()))
        for num in numbers:
            if num < 0:
                    raise ValueError()
        min_num = min(numbers)
        max_num = max(numbers)
        messagebox.showinfo("Results", f"Minimum: {min_num}\nMaximum: {max_num}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers separated by spaces.")

window = tk.Tk()
window.geometry("300x150")
window.title("Min and Max Finder")

label = tk.Label(window, text="Enter numbers separated by spaces:")
label.pack(pady=5)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

btn_find = tk.Button(window, text="Find Min and Max", command=find_min_max)
btn_find.pack(pady=5)

window.mainloop()
