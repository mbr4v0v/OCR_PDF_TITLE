import os
import shutil

def deshacer_organizacion(ruta_carpeta):
    """
    Deshace la organización de archivos, moviendo todos los archivos de vuelta a la raíz de la carpeta especificada.
    Los archivos que clasifica en carpetas separadas, los vuelve a juntar en la raiz de ese directorio
    
    :param ruta_carpeta: Ruta de la carpeta raíz.
    """
    # Recorrer todas las subcarpetas
    for carpeta in os.listdir(ruta_carpeta):
        carpeta_destino = os.path.join(ruta_carpeta, carpeta)
        
        # Ignorar archivos y solo trabajar con carpetas
        if os.path.isdir(carpeta_destino):
            for archivo in os.listdir(carpeta_destino):
                ruta_archivo = os.path.join(carpeta_destino, archivo)
                
                # Mover el archivo a la carpeta raíz
                if os.path.isfile(ruta_archivo):
                    destino = os.path.join(ruta_carpeta, archivo)
                    shutil.move(ruta_archivo, destino)
                    print(f"{archivo} -> {ruta_carpeta}")
            
            # Eliminar la subcarpeta si está vacía
            if not os.listdir(carpeta_destino):
                os.rmdir(carpeta_destino)
                print(f"Carpeta eliminada: {carpeta_destino}")

# Ejemplo de uso
ruta_carpeta = 'C:/Users/marco/Desktop/test'
deshacer_organizacion(ruta_carpeta)