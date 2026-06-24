from pypdf import PdfReader

reader = PdfReader("evs file.pdf")

pdf_text = ""

for page in reader.pages:
    pdf_text += page.extract_text()

sentences = pdf_text.split(".")

while True:

    question = input("Ask Question: ")

    if question.lower() == "exit":
        break

    found = False

    for sentence in sentences:

        if question.lower() in sentence.lower():

            print("\nAnswer:")
            print(sentence)

            found = True
            break

    if not found:
        print("Answer not found")