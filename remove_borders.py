#!/usr/bin/env python
import copy, sys
from PyPDF2 import PdfFileWriter, PdfFileReader

input = PdfFileReader('transparencia-novembro-2018.pdf')
output = PdfFileWriter()
for p in [input.getPage(i) for i in range(1,input.getNumPages())]:
    (w, h) = p.mediaBox.upperRight
    p.mediaBox.upperLeft = (0, h*0.74)
    p.mediaBox.lowerLeft = (0, h*0.1)
    output.addPage(p)
output.write(open("output.pdf","wb")) 
