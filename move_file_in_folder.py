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
        all_files = os.listdir(os.path.join(path, folder))
        files = natsorted([file for file in all_files if os.path.isfile(os.path.join(path, folder, file))])

        for file in files:
            if '.pdf' in file:
                shutil.move(os.path.join(path, folder, file), os.path.join(path))

if len(argv) >= 2:
    print('Proses memindah...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('Tidak ada file atau direktori...')