import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted
import shutil
import subprocess

cwd = os.path.dirname(__file__)

def split_pdf_to_images(index, path):
    all_folders = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])

    for i,folder in enumerate(folders):
        if not os.path.exists(os.path.join(path, folder, 'DTT.pdf')):
            if not os.path.exists(os.path.join(path, 'BELUM ADA DTT')):
                os.mkdir(os.path.join(path, 'BELUM ADA DTT'))
            shutil.move(os.path.join(path, folder), os.path.join(path, 'BELUM ADA DTT'))

if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(0, path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images