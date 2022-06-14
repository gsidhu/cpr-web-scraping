import PyPDF2

pdfFileObj = open('D-2020:33-16456-000032.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0) 

writer = PyPDF2.PdfFileWriter()

pageObj.mediaBox.upperRight = (1250/2, 690/2.7)
pageObj.mediaBox.lowerLeft = (478/2, 1512/2.25)

writer.addPage(pageObj)

with open("PyPDF2-output.pdf", "wb") as fp:
  writer.write(fp)


import PyPDF2
pdfFileObj = open('45.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0) 

text = pageObj.extractText()
text = text.split('\n')
for i in range(len(text)):
  print(str(i) + '\t' + text[i])

pdfFileObj = open('44.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0) 

text = pageObj.extractText()
text = text.split('\n')
for i in range(len(text)):
  print(str(i) + '\t' + text[i])

pdfFileObj = open('43.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0) 

text = pageObj.extractText()
text = text.split('\n')
for i in range(len(text)):
  print(str(i) + '\t' + text[i])

pdfFileObj = open('42.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0) 

text = pageObj.extractText()
text = text.split('\n')
for i in range(len(text)):
  print(str(i) + '\t' + text[i])

pdfFileObj = open('41.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0) 

text = pageObj.extractText()
text = text.split('\n')
for i in range(len(text)):
  print(str(i) + '\t' + text[i])

pdfFileObj = open('40.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0) 

text = pageObj.extractText()
text = text.split('\n')
for i in range(len(text)):
  print(str(i) + '\t' + text[i])

