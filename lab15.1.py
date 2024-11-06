import json
import tkinter as tk

def load_settings():
    with open("setting.json", "r", encoding='utf-8') as file:
        settings = json.load(file)
    return settings

def apply_settings():
    settings = load_settings()
    window.geometry(f"{settings['w']}x{settings['h']}")
    window.config(bg=settings['col'])
    window.title(settings['tit'])

window = tk.Tk()
window.geometry("280x180")
window.config(bg="olive")
window.title("Default Window")

btn_apply = tk.Button(window, text="Apply Settings", command=apply_settings)
btn_apply.place(x=100, y=80)

window.mainloop()