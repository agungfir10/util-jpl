import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted
import shutil
import subprocess

cwd = os.path.dirname(__file__)

def split_pdf_to_images(index, path):
    all_folders = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])

    for i,folder in enumerate(folders):

        if os.path.exists(os.path.join(path, folder, 'DTT.pdf')):

            pdf_file = os.path.join(path, folder, 'DTT.pdf')

            pdf_document = fitz.open(pdf_file)
            page1 = pdf_document[0]
                
            image_list = page1.get_displaylist()
            mx = fitz.Matrix(2, 2)
            image = image_list.get_pixmap(matrix = mx)

            image.pil_save(os.path.join(path, folder, f"RESULT.jpg"), optimize=False)
            command = f'tesseract "{os.path.join(path, folder, 'RESULT.jpg')}" stdout -l ind+eng'

            print(command)

            # Execute the command and capture the output
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            output, _ = process.communicate()
            output_str = output.decode()

            if not 'Pendamping' in output_str:
                with open('RESULT.txt', 'a') as myfile:
                    myfile.write(folder)
                    myfile.write('\n')
                    myfile.close()
            os.remove(os.path.join(path, folder, 'RESULT.jpg'))
            pdf_document.close()

if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(0, path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images