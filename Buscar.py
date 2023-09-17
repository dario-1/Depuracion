import tkinter as tk
import pandas as pd
from tkinter import filedialog

def buscar():
    global archivo
    archivo = filedialog.askopenfilename(title='Buscador de csv', filetypes=(('Todos los archivos', '*.*'),))
    label1.config(text=archivo)
    if archivo:
        df = pd.read_csv(archivo)
        print(df)
    
root = tk.Tk()
root.title('Buscador')
archivo = ""  # Variable global para almacenar la ruta del archivo

button1 = tk.Button(root, text='Buscar', command=buscar)
button1.pack()

label1 = tk.Label(root, text="")
label1.pack()


root.mainloop()

