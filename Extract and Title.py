import os
import PyPDF2

def split_pdf_pages(root_dir, extract_to_folder):
    if not os.path.exists(extract_to_folder):
        os.makedirs(extract_to_folder)

    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            basename, extension = os.path.splitext(filename)
            if extension.lower() == ".pdf":
                # create a reference to the full filename path
                fullpath = os.path.join(root, filename)

                # open the pdf in read mode
                with open(fullpath, "rb") as pdf_file:
                    opened_pdf = PyPDF2.PdfReader(pdf_file)

                    # for each page in the pdf
                    for i in range(len(opened_pdf.pages)):
                        # write the page to a new pdf
                        output = PyPDF2.PdfWriter()
                        output.add_page(opened_pdf.pages[i])
                        with open(os.path.join(extract_to_folder, f"{basename}-{i}.pdf"), "wb") as output_pdf:
                            output.write(output_pdf)

def rename_pdfs(extracted_pdf_folder, rename_folder):
    if not os.path.exists(rename_folder):
        os.makedirs(rename_folder)

    for root, dirs, files in os.walk(extracted_pdf_folder):
        for filename in files:
            basename, extension = os.path.splitext(filename)
            if extension.lower() == ".pdf":
                # create a reference to the full filename path
                fullpath = os.path.join(root, filename)

                # open the individual pdf
                with open(fullpath, "rb") as pdf_file_obj:
                    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

                    # access the individual page
                    page_obj = pdf_reader.pages[0]
                    # extract the text
                    pdf_text = page_obj.extract_text()

                    # use the extracted text to rename the pdf
                    new_filename = pdf_text.split("\n")[0].strip() + ".pdf"
                    new_filename = new_filename.replace("/", "-").replace("\\", "-").strip()
                    new_fullpath = os.path.join(rename_folder, new_filename)
                    
                # Ensure the file is closed before renaming
                os.rename(fullpath, new_fullpath)
                print(f"Renombrado: {filename} -> {new_filename}")

if __name__ == "__main__":
    root_dir = r"C:\Users\marco\Desktop\pdf"
    extract_to = r"C:\Users\marco\Desktop\extracted"
    rename_to = r"C:\Users\marco\Desktop\renamed"

    if os.path.exists(root_dir):
        split_pdf_pages(root_dir, extract_to)
        rename_pdfs(extract_to, rename_to)
    else:
        print(f"La ruta especificada no existe: {root_dir}")