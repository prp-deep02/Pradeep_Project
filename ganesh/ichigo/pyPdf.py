

from pypdf import PdfReader

reader = PdfReader("evs file.pdf")

print("Number of pages:", len(reader.pages))

for page in reader.pages:
    text = page.extract_text()
    print(text)


#Copy Paste from exisiting PDF

from pypdf import PdfReader, PdfWriter

reader = PdfReader("evs file.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

with open("output.pdf", "wb") as f:
    writer.write(f)


#Merge PDFs

from pypdf import PdfWriter

writer = PdfWriter()
# Option 1: Full path
writer.append(r"C:\Users\Sanjay\Documents\input-1.pdf")

# Option 2: Check before appending
import os
if os.path.exists("input-1.pdf"):
    writer.append("input-1.pdf")
else:
    print("File not found!")
writer.append("input-1.pdf")
writer.append("input-2.pdf")

writer.write("merged.pdf")
writer.close()
