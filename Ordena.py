#versión 1
#27-1-2024
import os
import shutil

def clasificar_archivos(origen, destino, criterio="extension"):
    """
    Clasifica los archivos de una carpeta en subcarpetas según el criterio especificado.

    :param origen: Ruta de la carpeta origen con los archivos.
    :param destino: Ruta de la carpeta destino para clasificar los archivos.
    :param criterio: Criterio para clasificar ("extension" o "nombre").
    """
    if not os.path.exists(origen):
        print(f"La carpeta de origen '{origen}' no existe.")
        return

    if not os.path.exists(destino):
        os.makedirs(destino)

    for archivo in os.listdir(origen):
        archivo_path = os.path.join(origen, archivo)

        # Solo procesar archivos (ignorar carpetas)
        if os.path.isfile(archivo_path):
            if criterio == "extension":
                ext = archivo.split('.')[-1]  # Obtener la extensión del archivo
                subcarpeta = os.path.join(destino, ext)
            elif criterio == "nombre":
                # Clasificar según una palabra clave en el nombre del archivo
                if "proyecto" in archivo.lower():
                    subcarpeta = os.path.join(destino, "proyectos")
                elif "informe" in archivo.lower():
                    subcarpeta = os.path.join(destino, "informes")
                else:
                    subcarpeta = os.path.join(destino, "otros")
            else:
                print(f"Criterio '{criterio}' no soportado.")
                return

            # Crear la subcarpeta si no existe
            if not os.path.exists(subcarpeta):
                os.makedirs(subcarpeta)

            # Mover el archivo a la subcarpeta correspondiente
            shutil.move(archivo_path, os.path.join(subcarpeta, archivo))
            print(f"Archivo '{archivo}' movido a '{subcarpeta}'.")

# Ejemplo de uso
if __name__ == "__main__":
    carpeta_origen = r"C:\Users\marco\Desktop\2025 CV Preparation"  # Cambia esta ruta
    carpeta_destino = r"C:\Users\marco\Desktop\2025 CV Preparation"  # Cambia esta ruta
    clasificar_archivos(carpeta_origen, carpeta_destino, criterio="nombre")
