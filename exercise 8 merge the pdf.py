from pypdf import PdfReader, PdfWriter
import os

pdf_writer = PdfWriter()

# Automatically find all PDF files in the current directory
files = [file for file in os.listdir() if file.endswith(".pdf")]

# Optional: Sort the files if you want them in a specific order
files.sort()

# Iterate through each PDF file
for pdf_file in files:
    reader = PdfReader(pdf_file)
    # Add each page to the writer
    for page in reader.pages:
        pdf_writer.add_page(page)

# Write out the merged PDF
with open("merged-pdf.pdf", "wb") as output_file:
    pdf_writer.write(output_file)

print("PDFs merged successfully into 'merged-pdf.pdf'!")
