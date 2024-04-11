from PIL import Image
from natsort import natsorted
from sys import argv
import shutil
import os

path = './pdf/contoh.pdf'

def rotate(rotation, path):
    folders = natsorted(os.listdir(path))

    for folder in folders:
        all_items = os.listdir(os.path.join(path, folder))
        files = natsorted([file for file in all_items if os.path.isfile(os.path.join(path, folder, file))])

        for file in files:
            image = Image.open(os.path.join(path, folder, file))
            filename, ext = os.path.splitext(os.path.join(path, folder, file))

            image_rotated = image.rotate(rotation, expand=True)
            image_rotated.save(os.path.join(path, folder, f'{filename}-rotate.{ext}'))
            os.remove(os.path.join(path, folder, file))
            os.rename(os.path.join(path, folder, f'{filename}-rotate.{ext}'),os.path.join(path, folder, file))
            

if len(argv) >= 2:
    print('Splitted PDF...')
    rotation = int(argv[1])
    path = argv[2]
    rotate(rotation, path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images