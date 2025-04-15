import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from datetime import datetime
import pandas as pd


data = []
        
def save_file():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = asksaveasfilename(defaultextension=".txt", initialfile=f"jyvädata_{timestamp}")
    df = pd.DataFrame(data)
    df.to_csv(filepath, encoding="utf-8", index=False)

root = tk.Tk()
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Tallenna nimellä...", command=lambda: save_file(), accelerator="Ctrl+S")
root.bind("<Control_L>s", lambda _: save_file())
menubar.add_cascade(label="Tiedosto", menu=filemenu)

root.config(menu=menubar)
root.grid_anchor("center")

style = ttk.Style()
style.theme_use("clam")
style.configure("Kirkas.TButton", background="#efefff", foreground="black")
style.configure("Valkea.TButton", background="white", foreground="black")
style.configure("Kellertävä.TButton", background="peachpuff", foreground="black")
style.configure("Punainen.TButton", background="red", foreground="black")
style.configure("Musta.TButton", background="black", foreground="white")

varit = ["Kirkas", "Valkea", "Kellertävä", "Punainen", "Musta"]
laskurit = {v: 0 for v in varit}
labels = {}

koko = tk.IntVar(root)

def lisaa_laskuriin(vari):
    laskurit[vari] += 1
    labels[vari].configure(text=laskurit[vari])
    timestamp = datetime.now()
    data.append({"datetime": timestamp, "väri": vari, "koko": koko.get()})
    print(timestamp)
    print(laskurit)

for idx, vari in enumerate(varit):
    button_vari = ttk.Button(root, text=vari, style=f"{vari}.TButton", command=lambda x=vari: lisaa_laskuriin(x))
    button_vari.grid(row=idx, column=0, pady=4)
    label_vari = ttk.Label(root, text=laskurit[vari])
    label_vari.grid(row=idx, column=1, padx=6)
    labels[vari] = label_vari

radio_koko1 = tk.Radiobutton(root, text="Koko 1", value=1, variable=koko)
radio_koko2 = tk.Radiobutton(root, text="Koko 2", value=2, variable=koko)
radio_koko3 = tk.Radiobutton(root, text="Koko 3", value=3, variable=koko)

radio_koko1.grid(row=1, column=2)
radio_koko2.grid(row=2, column=2)
radio_koko3.grid(row=3, column=2)

def on_exit():
    if messagebox.askokcancel("Sulje", "Sulje ohjelma?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()