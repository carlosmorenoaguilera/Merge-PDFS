
#!/usr/bin/env python
# Author: carlos.moreno
# Contributor(s): carlos.moreno
# jul, 2022

"""_summary_
Simple pdf merge script and compress 
"""


import os, sys
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
sys.path.append(r'C:\Users\Carlos Moreno\source\repos\Merge PDFS\PDFs')

from pdfc.pdf_compressor import compress

directory_path = './PDFs'
directory =  os.listdir(directory_path)

merger = PdfFileMerger()

for pdf in directory:
    file = 'C:/Users/Carlos Moreno/source/repos/Merge PDFS/PDFs/' + pdf
    merger.append(file, import_bookmarks=False)

filename = 'Carlos Mauricio Moreno Aguilera CV Certificados.pdf'     
merger.write(filename) 
merger.close()

writer = PdfFileWriter()
reader = PdfFileReader(filename)
for page in reader.pages:
    page.compressContentStreams()
    writer.addPage(page)
    
with open(filename + ' r', "wb") as f:
    writer.write(f)


compress(filename, filename + 'r.pdf', power=3)