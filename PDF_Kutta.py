import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_into_chunks(pdf_path, chunk_size=40):
    print(f"Starting split_pdf_into_chunks with pdf_path={pdf_path} and chunk_size={chunk_size}")
    # Read the PDF file
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages in PDF: {total_pages}")

    # Get the directory and file name
    folder = os.path.dirname(pdf_path)
    file_name = os.path.basename(pdf_path)
    base_name, ext = os.path.splitext(file_name)
    print(f"PDF directory: {folder}, file name: {file_name}")

    # Split the PDF into chunks
    for start_page in range(0, total_pages, chunk_size):
        writer = PdfWriter()
        end_page = min(start_page + chunk_size, total_pages)
        print(f"Creating chunk from page {start_page} to {end_page - 1}")

        # Add pages to the writer
        for page_number in range(start_page, end_page):
            writer.add_page(reader.pages[page_number])

        # Save the chunk
        chunk_file_name = f"{base_name}-{start_page // chunk_size + 1}{ext}"
        chunk_path = os.path.join(folder, chunk_file_name)
        print(f"Saving chunk to {chunk_path}")
        with open(chunk_path, "wb") as chunk_file:
            writer.write(chunk_file)

    print(f"PDF split into {((total_pages - 1) // chunk_size) + 1} chunks in {folder}.")

# GUI to select PDF file
def browse_pdf_file():
    print("Launching file dialog for PDF selection")
    # Hide the root window
    root = Tk()
    root.withdraw()

    # Open the file dialog
    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        print(f"Selected PDF file: {file_path}")
        split_pdf_into_chunks(file_path)
    else:
        print("No file selected")

if __name__ == "__main__":
    print("Starting the application")
    browse_pdf_file()
      
