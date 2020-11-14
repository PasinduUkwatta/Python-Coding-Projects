

import pyttsx3
import PyPDF2

pdf_book = open("Python.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_book)
pages = pdf_reader.numPages
print(pages)
speaker = pyttsx3.init()

for num in range(0, pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()





