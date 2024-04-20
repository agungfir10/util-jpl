import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images( path):
    all_folders = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])

    for i,folder in enumerate(folders):
        print(f'{i+1}/{len(folders)}')

        if os.path.exists(os.path.join(path, folder, 'SPTJM&PENGGANTI.pdf')):
            pdf_file = os.path.join(path, folder, 'SPTJM&PENGGANTI.pdf')
            pdf_document = fitz.open(pdf_file)

            for page_number in range(len(pdf_document)):
                page = pdf_document[page_number]
                
                image_list = page.get_displaylist()    
                mx = fitz.Matrix(2, 2)
                image = image_list.get_pixmap(matrix = mx)

                if os.path.exists(os.path.join(path, folder)):
                    image.pil_save(os.path.join(path, folder, f"{page_number}.jpg"), optimize=False)
                else:
                    image.pil_save(os.path.join(path, folder, f"{page_number}.jpg"), optimize=False)

if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images