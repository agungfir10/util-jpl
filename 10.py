import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_items = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_items if os.path.isdir(os.path.join(path, folder))])

    for index, folder in enumerate(folders):
        print(f'{index + 1}/ {len(folders)}...')
        all_files = os.listdir(os.path.join(path, folder))
        files = natsorted([file for file in all_files if os.path.isfile(os.path.join(path, folder, file))])
        
        for file in files:

            if '.pdf' in file and 'DTT' in file:
                pdf_file = os.path.join(path, folder, file)

                pdf_document = fitz.open(pdf_file)

                for page_number in range(len(pdf_document)):
                    page = pdf_document[page_number]
                    
                    image_list = page.get_displaylist()    
                    mx = fitz.Matrix(2, 2)
                    image = image_list.get_pixmap(matrix = mx)
                    if page_number == 0:
                        image.pil_save(os.path.join(path, folder, f"1.jpg"), optimize=False)
                    if page_number == 1:
                        image.pil_save(os.path.join(path, folder, f"0.jpg"), optimize=False)

if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')