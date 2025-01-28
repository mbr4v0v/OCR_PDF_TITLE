import os
import shutil
import requests

def get_file_category(file_name):
    # Realiza una consulta a internet para determinar la categoría del archivo
    query = f"Categoría del archivo {file_name}"
    try:
        response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
        if response.status_code == 200:
            data = response.json()
            # Intenta obtener una categoría de la respuesta (esto es solo un ejemplo simplificado)
            category = data.get("Abstract", "Otros")
            return category if category else "Otros"
    except Exception as e:
        print(f"Error al consultar la categoría para {file_name}: {e}")
    return "Otros"

def categorize_and_move_files(base_path):
    # Crear carpeta "Otros" por si no se encuentra categoría específica
    other_folder = os.path.join(base_path, "Otros")
    if not os.path.exists(other_folder):
        os.makedirs(other_folder)

    # Iterar sobre los archivos en la carpeta base
    for file_name in os.listdir(base_path):
        file_path = os.path.join(base_path, file_name)

        # Ignorar directorios
        if os.path.isdir(file_path):
            continue

        # Obtener la categoría del archivo
        category = get_file_category(file_name)

        # Crear carpeta para la categoría si no existe
        category_folder = os.path.join(base_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        # Mover el archivo a la carpeta correspondiente
        shutil.move(file_path, os.path.join(category_folder, file_name))
        print(f"Movido: {file_name} -> {category}")

if __name__ == "__main__":
    # Cambia esta ruta a la carpeta que deseas organizar
    folder_path = r"C:\Users\marco\Desktop\test"

    if os.path.exists(folder_path):
        categorize_and_move_files(folder_path)
    else:
        print(f"La ruta especificada no existe: {folder_path}")
