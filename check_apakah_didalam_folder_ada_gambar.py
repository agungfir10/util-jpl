import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted
import shutil
import subprocess

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_folders = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])

    for i, folder in enumerate(folders):
        # print(f'{i+1}/{len(folders)}')

        files = os.listdir(os.path.join(path, folder))
        for file in files:
            if '.jpg' in file or '.png' in file:
                print(folder)
                print(file)


if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images