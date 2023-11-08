import tkinter as tk
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.grid_anchor("center")

style = ttk.Style()
style.theme_use("clam")
style.configure("Kirkas.TButton", background="white", foreground="black")
style.configure("Musta.TButton", background="black", foreground="white")
style.configure("Ruskea.TButton", background="brown", foreground="black")
style.configure("Punainen.TButton", background="red", foreground="black")

varit = ["Kirkas", "Musta", "Ruskea", "Punainen"]
laskurit = {v: 0 for v in varit}
labels = {}

def lisaa_laskuriin(vari):
    laskurit[vari] += 1
    labels[vari].configure(text=laskurit[vari])
    print(datetime.now())
    print(laskurit)

for idx, vari in enumerate(varit):
    button_vari = ttk.Button(root, text=vari, style=f"{vari}.TButton", command=lambda x=vari: lisaa_laskuriin(x))
    button_vari.grid(row=idx, column=0, pady=4)
    label_vari = ttk.Label(root, text=laskurit[vari])
    label_vari.grid(row=idx, column=1, padx=6)
    labels[vari] = label_vari


root.mainloop()