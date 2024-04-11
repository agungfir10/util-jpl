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
        folder, ext = os.path.splitext(os.path.join(path, files[index]))

        pdf_document = fitz.open(pdf_file)

        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            image_list = page.get_images(full=True)
            
            if os.path.exists(os.path.join(path, folder)):
                os.mkdir(os.path.join(path, folder))
            else:
                for img_index, img in enumerate(image_list):
                    image = pdf_document.extract_image(img[0])
                    image_bytes = image["image"]
                    # os.mkdir(os.path.join(path, folder, 'DTT'))
                    # os.mkdir(os.path.join(path, folder, 'SPTJM'))
                    # os.mkdir(os.path.join(path, folder, 'PENGGANTI'))
                    # os.mkdir(os.path.join(path, folder, 'PERWAKILAN'))
                    with open(os.path.join(path, f"{folder}-{page_number + 1 }.png"), "wb") as image_file:
                        image_file.write(image_bytes)

        pdf_document.close()
        split_pdf_to_images(index + 1, path)


if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(0, path)
else:
    print('No Such File or Directory...')