import pdfplumber

pdf = pdfplumber.open("1장.pdf")

pnum = len(pdf.pages)

for i in range(pnum):
    p = pdf.pages[i]
    print(p.extract_text())