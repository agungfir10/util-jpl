from PyPDF2 import PdfMerger
from os import path,listdir
from natsort import natsorted
import os
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_folders = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])

    for i,folder in enumerate(folders):
        pdf_merger = PdfMerger()
        if os.path.exists(os.path.join(path, folder, '00DTT.pdf')) and os.path.exists(os.path.join(path, folder, '0DTT.pdf')):
            print(folder)
            pdf_merger.append(os.path.join(path, folder, '00DTT.pdf'))
            pdf_merger.append(os.path.join(path, folder, '0DTT.pdf'))
            pdf_merger.write(os.path.join(path, folder, 'BAST-DESA-DTT.pdf'))
            pdf_merger.close()
            # os.remove(os.path.join(path, folder, 'DTT.pdf'))
            os.rename(os.path.join(path, folder, 'BAST-DESA-DTT.pdf'), os.path.join(path, folder, 'DTT.pdf'))

if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images