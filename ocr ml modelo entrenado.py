import os
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import joblib

# Configurar la ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Cargar el modelo de clasificación de texto
model_path = r'C:\Users\marco\Desktop\text_classifier_model.pkl'
text_classifier = joblib.load(model_path)

def ocr_first_page(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Get the first page
    first_page = pdf_document.load_page(0)
    
    # Render the page to an image
    pix = first_page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Perform OCR on the image
    text = pytesseract.image_to_string(img)
    
    # Print the OCR result
    print(f"OCR Result for {os.path.basename(pdf_path)}:")
    print(text)
    
    # Use the first line of the text as the title
    title = text.split('\n')[0].strip()
    title = title.replace("/", "-").replace("\\", "-").replace(":", "-").replace("*", "-").replace("?", "-").replace("\"", "-").replace("<", "-").replace(">", "-").replace("|", "-")
    
    # Save the image as PNG with the title as the filename
    png_path = os.path.join(os.path.dirname(pdf_path), f"{title}.png")
    img.save(png_path, "PNG")
    print(f"First page saved as PNG: {png_path}")
    
    # Display the image
    img.show()
    
    return text

def identify_title(text):
    # Preprocesar el texto si es necesario
    # Aquí puedes agregar cualquier preprocesamiento que necesites
    processed_text = text.lower()
    
    # Usar el modelo de clasificación para identificar el título
    title = text_classifier.predict([processed_text])[0]
    return title

def process_pdfs_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        files.sort()  # Ordenar los archivos alfabéticamente
        for filename in files:
            if filename.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, filename)
                try:
                    text = ocr_first_page(pdf_path)
                    title = identify_title(text)
                    print(f"Identified Title for {os.path.basename(pdf_path)}: {title}")
                except Exception as e:
                    print(f"Error processing {pdf_path}: {e}")

if __name__ == "__main__":
    folder_path = r"C:\Users\marco\Desktop\pdf2"
    
    if os.path.exists(folder_path):
        process_pdfs_in_folder(folder_path)
    else:
        print(f"La ruta especificada no existe: {folder_path}")