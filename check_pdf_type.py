from PyPDF2 import PdfReader
import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_items = os.listdir(os.path.join(path))
    files = natsorted([file for file in all_items if os.path.isfile(os.path.join(path, file))])

    for file in files:
        doc = PdfReader(os.path.join(path, file))
        doc.stream.seek(0) # Necessary since the comment is ignored for the PDF analysis
        print(file)
        print(doc.stream.readline().decode())



if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images