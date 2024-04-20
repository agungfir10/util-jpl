from pdf2image import convert_from_path
import os
from sys import argv, setrecursionlimit
from natsort import natsorted
from PIL import Image

setrecursionlimit(9999999)

cwd = os.path.dirname(__file__)


def split_pdf_to_images(path):
    all_folders = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])
    
    for folder in folders:

        all_items = os.listdir(os.path.join(path, folder))
        files = natsorted([file for file in all_items if os.path.isfile(os.path.join(path, folder, file))])
        for file in files:
            if '.jpg' in file or '.png' in file:
                filename, ext = os.path.splitext(file)
                image = Image.open(os.path.join(path, folder, file))
                image_rotated = image.rotate(180, expand=True)
                image_rotated.save(os.path.join(path, folder, f'{filename}-ROTATED{ext}'))
                os.remove(os.path.join(path, folder, file))
                os.rename(os.path.join(path, folder, f'{filename}-ROTATED{ext}'), os.path.join(path, folder, file))

if len(argv) >= 2:
    print('Rotates image...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')