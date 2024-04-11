from pdf2image import convert_from_path
import os
from sys import argv, setrecursionlimit
from natsort import natsorted
setrecursionlimit(9999999)

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_folders = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])

    for i, folder in enumerate(folders):
        all_items = os.listdir(os.path.join(path, folder))
        files = natsorted([file for file in all_items if os.path.isfile(os.path.join(path, folder, file))])

        for i,file in enumerate(files):

            filepath = os.path.join(path, folder, file)
            print(f"{i+1}/{len(files)}")
            if 'SPTJM' in file:
                images = convert_from_path(filepath)
                for i, image in enumerate(images):
                    # ROTATE IMAGE
                    if os.path.exists(os.path.join(path, folder)):
                        if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
                            os.mkdir(os.path.join(path, folder, 'SPTJM'))
                        if not os.path.exists(os.path.join(path, folder, 'PENGGANTI')):
                            os.mkdir(os.path.join(path, folder, 'PENGGANTI'))
                        image.save(os.path.join(path, folder, f'{i}.png'))
                    else:
                        if not os.path.exists(os.path.join(path, folder)):
                            os.mkdir(os.path.join(path, folder))
                        if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
                            os.mkdir(os.path.join(path, folder, 'SPTJM'))
                        if not os.path.exists(os.path.join(path, folder, 'PENGGANTI')):
                            os.mkdir(os.path.join(path, folder, 'PENGGANTI'))
                        image.save(os.path.join(path, folder, f'{i}.png'))
    print('Done...')



if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images