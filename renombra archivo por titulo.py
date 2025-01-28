import os
import PyPDF2

def rename_pdf_by_title(pdf_folder):
    """
    Renombra archivos PDF basándose en el título del PDF.

    Args:
        pdf_folder (str): Ruta a la carpeta que contiene los archivos PDF.
    """
    for file_name in os.listdir(pdf_folder):
        file_path = os.path.join(pdf_folder, file_name)

        # Ignorar archivos que no sean PDF
        if not file_name.lower().endswith(".pdf"):
            continue

        try:
            # Abrir el archivo PDF
            with open(file_path, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                # Obtener el título del PDF (metadatos o primer texto de la primera página)
                title = pdf_reader.metadata.title
                if not title and pdf_reader.pages:
                    title = pdf_reader.pages[0].extract_text().strip().split("\n")[0]

                # Si no se encuentra un título, usar un nombre genérico
                if not title:
                    title = "Untitled"

                # Crear un nombre de archivo seguro
                new_file_name = f"{title}.pdf"
                new_file_name = new_file_name.replace("/", "-").replace("\\", "-").strip()

            # Renombrar el archivo PDF
            new_file_path = os.path.join(pdf_folder, new_file_name)
            os.rename(file_path, new_file_path)
            print(f"Renombrado: {file_name} -> {new_file_name}")

        except Exception as e:
            print(f"Error al procesar {file_name}: {e}")

if __name__ == "__main__":
    # Cambia esta ruta a la carpeta donde se encuentran los PDFs
    pdf_folder_path = r"C:\Users\marco\Desktop\pdf"

    if os.path.exists(pdf_folder_path):
        rename_pdf_by_title(pdf_folder_path)
    else:
        print(f"La ruta especificada no existe: {pdf_folder_path}")

        #carpeta en C:\Users\marco\Desktop\pdf con archivos PDF sin nombre de archivo
        