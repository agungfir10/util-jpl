import fitz  # PyMuPDF
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
        print(folder)

        image_items = os.listdir(os.path.join(path, folder))
        images = natsorted([image for image in image_items if os.path.isfile(os.path.join(path, folder, image))])

        for image in images:
            if '.jpg' in image or '.png' in image:
                if os.path.exists(os.path.join(path, folder, image)):
                    command = f'tesseract "{os.path.join(path, folder, image)}" stdout -l ind+eng'
                    print(command)
                    # Execute the command and capture the output
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
                    output, _ = process.communicate()
                    output_str = output.decode()
                    # print(output_str)

                    output, _ = process.communicate()
                    output_str = output.decode()
                    # print(output_str)
                    sep = ['SEPTEMBER', 'September', 'september']
                    okt = ['OKTOBER', 'Oktober', 'oktober']
                    nov = ['NOVEMBER', 'November', 'november']

                    if any(sub in output_str for sub in sep):
                        if not os.path.exists(os.path.join(path, folder, 'SEP')):
                            os.mkdir(os.path.join(path, folder, 'SEP'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SEP', image))
                    elif any(sub in output_str for sub in okt):
                        if not os.path.exists(os.path.join(path, folder, 'OKT')):
                            os.mkdir(os.path.join(path, folder, 'OKT'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'OKT', image))
                    elif any(sub in output_str for sub in nov):
                        if not os.path.exists(os.path.join(path, folder, 'NOV')):
                            os.mkdir(os.path.join(path, folder, 'NOV'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'NOV', image))
                    else:
                        print(output_str)


if len(argv) >= 2:
    print('OCR Ready...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')