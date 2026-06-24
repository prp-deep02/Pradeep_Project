from pypdf import PdfReader
reader = PdfReader("Intern.pdf")
print("Number of pages:", len(reader.pages))
page = reader.pages[0].extract_text()
print(page)

reader = PdfReader("Intern.pdf")
text = reader.pages[1].extract_text()
print(text)

full_text = ""
for i in reader.pages:
    full_text += i.extract_text()
print(full_text)

text = reader.pages[0].extract_text(extraction_mode="layout")   