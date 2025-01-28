import os
import tkinter as tk
from tkinter import scrolledtext

def listar_directorios(ruta, nivel=0):
    tree_str = ""
    for item in os.listdir(ruta):
        item_path = os.path.join(ruta, item)
        tree_str += "    " * nivel + "|-- " + item + "\n"
        if os.path.isdir(item_path):
            tree_str += listar_directorios(item_path, nivel + 1)
    return tree_str

def mostrar_arbol():
    ruta_carpeta = 'C:/Users/marco/Desktop/test'
    tree_str = listar_directorios(ruta_carpeta)
    
    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Estructura de Directorios")
    
    # Crear widget de texto con scroll
    text_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD)
    text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Insertar el árbol de directorios en el widget de texto
    text_area.insert(tk.END, tree_str)
    text_area.configure(state='disabled')  # Hacer que el texto sea de solo lectura
    
    # Ejecutar la ventana
    ventana.mainloop()

# Ejecutar la función para mostrar el árbol de directorios
mostrar_arbol()