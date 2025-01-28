import os
import shutil

def ordenar_archivos_por_contenido(ruta_carpeta, reglas):
    """
    Ordena los archivos en la carpeta especificada según las reglas dadas.
    
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
            contenido_archivo = ""
            
            # Leer el contenido del archivo si es un archivo de texto
            if archivo.lower().endswith(('.txt', '.md', '.py', '.java', '.c', '.cpp', '.html', '.css', '.js')):
                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as f:
                        contenido_archivo = f.read().lower()
                except Exception as e:
                    print(f"No se pudo leer el archivo {archivo}: {e}")
            
            for carpeta, palabras_clave in reglas.items():
                # Verificar si el archivo coincide con alguna palabra clave o extensión en el nombre o contenido
                if any(palabra in archivo.lower() or palabra in contenido_archivo for palabra in palabras_clave):
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

# Ejemplo de uso
ruta_carpeta = r'C:\Users\marco\Desktop\test' #ojo con la r de RAW
reglas = {
    'Documentos': ['.doc', '.docx', '.pdf', 'informe', 'reporte'],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif'],
    'Codigo': ['.py', '.java', '.c', '.cpp', '.html', '.css', '.js'],
    'Musica': ['.mp3', '.wav', '.flac']
}

ordenar_archivos_por_contenido(ruta_carpeta, reglas)