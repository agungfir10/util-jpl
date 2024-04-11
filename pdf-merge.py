from PyPDF2 import PdfMerger
from os import path,listdir
from natsort import natsorted
import os
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(index, path):
    all_folders = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])

    for i,folder in enumerate(folders):
        pdf_merger = PdfMerger()
        if os.path.exists(os.path.join(path, folder, 'BAST DESA.pdf')) and os.path.exists(os.path.join(path, folder, 'DTT-ONLY.pdf')):
            pdf_merger.append(os.path.join(path, folder, 'BAST DESA.pdf'))
            pdf_merger.append(os.path.join(path, folder, 'DTT-ONLY.pdf'))
            pdf_merger.write(os.path.join(path, folder, 'DTT.pdf'))
            pdf_merger.close()

if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(0, path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images