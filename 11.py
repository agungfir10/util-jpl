import os
import shutil
import subprocess
from sys import argv
from natsort import natsorted
from PyPDF2 import PdfMerger
import fitz  # PyMuPDF


cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_items = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_items if os.path.isdir(os.path.join(path, folder))])

    for folder in folders:
        all_sub_folders = os.listdir(os.path.join(path, folder))
        sub_folders = natsorted([sub_folder for sub_folder in all_sub_folders if os.path.isdir(os.path.join(path, folder, sub_folder))])

        for sub_folder in sub_folders:
            # os.rename(os.path.join(path, folder, sub_folder), os.path.join(path, folder, f'KAB. SUKOHARJO-{folder}-{sub_folder}'))
            all_files = os.listdir(os.path.join(path, folder, sub_folder))
            files = natsorted([file for file in all_files if os.path.isfile(os.path.join(path, folder, sub_folder, file))])

            pdf_merger = PdfMerger()

            for file in files:
                if '.pdf' in file:
                    if '1' in file:
                        pdf_merger.append(os.path.join(path, folder, sub_folder, file))
                    if '3' in file:
                        pdf_merger.append(os.path.join(path, folder, sub_folder, file))
            pdf_merger.write(os.path.join(path, folder, sub_folder, 'DTT.pdf'))
            pdf_merger.close()


if len(argv) >= 2:
    print('Proses merge pdf...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('Tidak ada file atau direktori...')