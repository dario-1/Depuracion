import tkinter as tk
import pandas as pd
from tkinter import filedialog
import os

def buscar():
    try:
        archivo = filedialog.askopenfilename(title='Buscador de csv', filetypes=(('Archivos CSV', '*.csv'),))
        if archivo:
            label1.config(text=archivo)
            df = pd.read_csv(archivo)
            print("Contenido del archivo CSV:")
            print(df)
            columnas = df.columns
            print("Columnas del DataFrame:")
            print(columnas)
            tabla = df[['Abs (Corr)1', 'Abs (Corr)2', 'Abs (Corr)3']]
            print("Subconjunto del DataFrame:")
            print(tabla)
            
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
root.title('Buscador de CSV')

button1 = tk.Button(root, text='Buscar', command=buscar)
button1.pack()

label1 = tk.Label(root, text="")
label1.pack()

root.mainloop()
