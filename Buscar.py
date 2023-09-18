# -*- coding: utf-8 -*-
import tkinter as tk
import pandas as pd
from tkinter import font
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
import os

def font1(size):
     return font.Font(family="Times New Roman", size=size)
    

def seleccionar_opcion():
    seleccion = variable.get()
    if seleccion == "Maquina 1":
        etiqueta.config(text="Has seleccionado la Maquina 1")
    elif seleccion == "Maquina 2":
        etiqueta.config(text="Has seleccionado la Maquina 2")
    

def buscar():
    try:
        archivo = filedialog.askopenfilename(title='Buscador de csv', filetypes=(('Archivos CSV', '*.csv'),))
        if archivo:
            label1.config(text=archivo)
            df = pd.read_csv(archivo)
            #print("Contenido del archivo CSV:")
            #print(df)
            columnas = df.columns
            #print("Columnas del DataFrame:")
            #print(columnas)
            tabla = df[['Abs (Corr)1', 'Abs (Corr)2', 'Abs (Corr)3']]
            #print("Subconjunto del DataFrame:")
            #print(tabla)
            
            # Obtener el nombre del archivo sin la extension .csv
            nombre_archivo = os.path.splitext(os.path.basename(archivo))[0]
            
            # Crear el nuevo nombre del archivo Excel con el termino filtrado al principio
            nuevo_nombre_excel = f"Filtrado_{nombre_archivo}.xlsx"
            
            # Pedir al usuario que seleccione la ruta de guardado del archivo Excel
            ruta_guardado = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=(('Archivos Excel', '*.xlsx'),))
            
            if ruta_guardado:
                # Guardar 'tabla' en un archivo Excel en la ruta seleccionada
                tabla.to_excel(ruta_guardado, index=False)
                print(f"Archivo Excel guardado en: {ruta_guardado}")
            else:
                print("No se selecciono una ruta de guardado.")
        else:
            label1.config(text="No se selecciono ningun archivo.")
    except Exception as e:
        label1.config(text=f"Error: {str(e)}")

root = tk.Tk()

root.title('Depurador de archivos')
root.geometry("1587x850")
#fuente=font.Font(family="Times New Roman",size=18)
encabezado1 = tk.Label(root, text="SELECCION DE MAQUINA:",font=font1(10))
encabezado1.grid(row=0, column=0, padx=20, pady=20, columnspan=2)
opciones = ["Maquina 1", "Maquina 2"]
variable = tk.StringVar(root)
variable.set("Seleccione el equipo")
menu_desplegable = tk.OptionMenu(root, variable, *opciones)
menu_desplegable.config(width=25, height=1)  # Ancho de 120 y alto de 8
#menu_desplegable.pack(side="left")  # Colocar a la izquierda
menu_desplegable.grid(row=1, column=0, padx=20, pady=5, sticky="w")

button1 = tk.Button(root, text='BUSCAR',font=font.Font(family="Times New Roman",size=12), command=buscar)
#button1.pack()
button1.grid(row=2, column=0, padx=20, pady=5, sticky="w")



label1 = tk.Label(root, text="")
label1.grid(row=3, column=0, padx=20, pady=5, sticky="w")

root.mainloop()
