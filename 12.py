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
        # os.rename(os.path.join(path, folder, sub_folder), os.path.join(path, folder, f'KAB. SUKOHARJO-{folder}-{sub_folder}'))
        all_files = os.listdir(os.path.join(path, folder))
        files = natsorted([file for file in all_files if os.path.isfile(os.path.join(path, folder, file))])

        # pdf_merger = PdfMerger()

        for file in files:
            if '.pdf' in file:
        #         if '1' in file:
        #             pdf_merger.append(os.path.join(path, folder, sub_folder, file))
        #         if '3' in file:
        #             pdf_merger.append(os.path.join(path, folder, sub_folder, file))
                if '2' in file:
                    pdf_file = os.path.join(path, folder, file)
                    pdf_document = fitz.open(pdf_file)

                    for page_number in range(len(pdf_document)):
                        page = pdf_document[page_number]
                        
                        image_list = page.get_displaylist()    
                        mx = fitz.Matrix(2, 2)
                        image = image_list.get_pixmap(matrix = mx)
                        image.pil_save(os.path.join(path, folder, f"{page_number}.jpg"), optimize=False)

            # pdf_merger.write(os.path.join(path, folder, sub_folder, 'DTT.pdf'))
            # pdf_merger.close()


if len(argv) >= 2:
    print('Proses merge pdf...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('Tidak ada file atau direktori...')