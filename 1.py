import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(index, path):
    all_items = os.listdir(os.path.join(path))
    files = natsorted([file for file in all_items if os.path.isfile(os.path.join(path, file))])

    if index >= len(files):
        print('Splitted Finish...')
    else:
        print(f'{index + 1}/ {len(files)}...')
        pdf_file = os.path.join(path, files[index])
        folder,ext = os.path.splitext(os.path.join(path, files[index]))

        pdf_document = fitz.open(pdf_file)

        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            
            image_list = page.get_displaylist()    
            mx = fitz.Matrix(2, 2)
            image = image_list.get_pixmap(matrix = mx)

            if not os.path.exists(os.path.join(path, folder)):
                os.mkdir(os.path.join(path, folder))
            image.pil_save(os.path.join(path, folder, f"{page_number}.jpg"), optimize=False)

        split_pdf_to_images(index + 1, path)


if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(0, path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images