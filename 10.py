import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted
import shutil

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_items = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_items if os.path.isdir(os.path.join(path, folder))])

    for index, folder in enumerate(folders):

        all_folders = os.listdir(os.path.join(path, folder))
        sub_folders = natsorted([sub_folder for sub_folder in all_folders if os.path.isdir(os.path.join(path, folder, sub_folder))])

        for sub_folder in sub_folders:

            print(f'{index + 1}/ {len(folders)}...')
            if 'OKT' in sub_folder:
                all_files = os.listdir(os.path.join(path, folder, sub_folder))
                files = natsorted([file for file in all_files if os.path.isfile(os.path.join(path, folder, sub_folder, file))])

                for file in files:

                    if '.pdf' in file:
                        shutil.move(os.path.join(path, folder, sub_folder, file), 'F:\\KAB DEMAK TAMBAHAN III\\OKT')
                    # pdf_file = os.path.join(path, folder, file)

                    # pdf_document = fitz.open(pdf_file)

                    # for page_number in range(len(pdf_document)):
                    #     page = pdf_document[page_number]
                        
                    #     image_list = page.get_displaylist()    
                    #     mx = fitz.Matrix(2, 2)
                    #     image = image_list.get_pixmap(matrix = mx)
                    #     if page_number == 0:
                    #         image.pil_save(os.path.join(path, folder, f"1.jpg"), optimize=False)
                    #     if page_number == 1:
                    #         image.pil_save(os.path.join(path, folder, f"0.jpg"), optimize=False)

if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')