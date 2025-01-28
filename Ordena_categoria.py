import os
import shutil

def categorize_and_move_files(base_path):
    # Define una lista de categorías basadas en extensiones de archivo
    categories = {
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".html"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Programas": [".exe", ".msi"],
        "Otros": []
    }

    # Crear carpetas de categorías si no existen
    for category in categories.keys():
        category_path = os.path.join(base_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Iterar sobre los archivos en la carpeta base
    for file_name in os.listdir(base_path):
        file_path = os.path.join(base_path, file_name)

        # Ignorar directorios
        if os.path.isdir(file_path):
            continue

        # Identificar la categoría según la extensión
        file_extension = os.path.splitext(file_name)[1].lower()
        category_found = False

        for category, extensions in categories.items():
            if file_extension in extensions:
                category_folder = os.path.join(base_path, category)
                shutil.move(file_path, os.path.join(category_folder, file_name))
                print(f"Movido: {file_name} -> {category}")
                category_found = True
                break

        # Si no se encuentra la categoría, mover a "Otros"
        if not category_found:
            other_folder = os.path.join(base_path, "Otros")
            shutil.move(file_path, os.path.join(other_folder, file_name))
            print(f"Movido: {file_name} -> Otros")

if __name__ == "__main__":
    # Cambia esta ruta a la carpeta que deseas organizar
    folder_path = r"C:\Users\marco\Desktop\test"

    if os.path.exists(folder_path):
        categorize_and_move_files(folder_path)
    else:
        print(f"La ruta especificada no existe: {folder_path}")
