import fitz  # PyMuPDF
import os
import shutil
import subprocess
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_items = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_items if os.path.isdir(os.path.join(path, folder))])

    for folder in folders:
        os.mkdir(os.path.join(path, folder, 'DTT'))
        os.mkdir(os.path.join(path, folder, 'SPTJM'))
        os.mkdir(os.path.join(path, folder, 'PENGGANTI'))
        os.mkdir(os.path.join(path, folder, 'PERWAKILAN'))

if len(argv) >= 2:
    print('OCR Ready...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')