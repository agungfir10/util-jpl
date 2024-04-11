import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(index, path):
    all_items = os.listdir(os.path.join(path))
    folders = natsorted([file for file in all_items if not os.path.isfile(os.path.join(path, file))])

    if index >= len(folders):
        print('Splitted Finish...')
    else:
        print(f'{index + 1}/ {len(folders)}...')
        pdf_file = os.path.join(path, folders[index], 'DTT.pdf')
        filename, ext = os.path.splitext(os.path.join(path, folders[index], 'DTT.pdf'))

        pdf_document = fitz.open(pdf_file)

        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            image_list = page.get_images(full=True)
            
            for img_index, img in enumerate(image_list):
                image = pdf_document.extract_image(img[0])
                image_bytes = image["image"]
                with open(os.path.join(path, folders[index], f"{page_number}.png"), "wb") as image_file:
                    image_file.write(image_bytes)
        os.mkdir(os.path.join(path, folders[index], 'DTT'))
        os.mkdir(os.path.join(path, folders[index], 'SPTJM'))
        os.mkdir(os.path.join(path, folders[index], 'PENGGANTI'))
        os.mkdir(os.path.join(path, folders[index], 'PERWAKILAN'))
        os.mkdir(os.path.join(path, folders[index], 'GUDANG'))
        os.mkdir(os.path.join(path, folders[index], 'SURAT JALAN'))
        os.mkdir(os.path.join(path, folders[index], 'DO'))
        os.mkdir(os.path.join(path, folders[index], 'SPM'))


        pdf_document.close()
        split_pdf_to_images(index + 1, path)


if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(0, path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images