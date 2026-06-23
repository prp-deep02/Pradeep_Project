#Read from PDF

from pypdf import PdfReader

reader = PdfReader("Sample.pdf")

print("Number of pages:", len(reader.pages))

for page in reader.pages:
    text = page.extract_text()
    print(text)


#Copy Paste from exisiting PDF
"""
from pypdf import PdfReader, PdfWriter

reader = PdfReader("sample.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

with open("output.pdf", "wb") as f:
    writer.write(f)
    """


#Merge PDFs
"""
from pypdf import PdfWriter

writer = PdfWriter()

writer.append("input-1.pdf")
writer.append("input-2.pdf")

writer.write("merged.pdf")
writer.close()
"""