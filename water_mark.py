import PyPDF2

template = PyPDF2.PdfFileReader(open('new_file.pdf','rb'))

watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    #in the getpage method we use 0 index
    #becuse in the 0 index the place where that watermark is saved
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open ('water_marked_file.pdf','wb') as file:
        output.write(file)

