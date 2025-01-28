import os
import shutil

def clasificar_archivos(ruta_carpeta, reglas):
    """
    Clasifica archivos en carpetas según las reglas especificadas.
    
    :param ruta_carpeta: Ruta de la carpeta con los archivos.
    :param reglas: Diccionario donde la clave es el nombre de la carpeta destino y 
                   el valor es una lista de palabras clave o extensiones.
    """
    # Crear subcarpetas según las reglas si no existen
    for carpeta in reglas.keys():
        carpeta_destino = os.path.join(ruta_carpeta, carpeta)
        os.makedirs(carpeta_destino, exist_ok=True)
    
    # Clasificar archivos
    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        
        # Ignorar carpetas y solo trabajar con archivos
        if os.path.isfile(ruta_archivo):
            clasificado = False
            for carpeta, palabras_clave in reglas.items():
                # Verificar si el archivo coincide con alguna palabra clave o extensión
                if any(palabra in archivo.lower() for palabra in palabras_clave):
                    destino = os.path.join(ruta_carpeta, carpeta, archivo)
                    shutil.move(ruta_archivo, destino)
                    print(f"{archivo} -> {carpeta}")
                    clasificado = True
                    break
            
            # Si el archivo no coincide con ninguna regla, se coloca en una carpeta "Otros"
            if not clasificado:
                carpeta_otros = os.path.join(ruta_carpeta, "Otros")
                os.makedirs(carpeta_otros, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(carpeta_otros, archivo))
                print(f"{archivo} -> Otros")

if __name__ == "__main__":
    # Ruta de la carpeta que quieres clasificar
    ruta_carpeta = r"C:\Users\marco\Desktop\2025 CV Preparation"
    
    # Reglas de clasificación (puedes agregar más categorías)
    reglas = {
        "Documentos": [".pdf", ".docx", ".xlsx", ".txt"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Audios": [".mp3", ".wav", ".aac"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Códigos": [".py", ".js", ".html", ".css"],
    }
    
    # Ejecutar la clasificación
    clasificar_archivos(ruta_carpeta, reglas)
