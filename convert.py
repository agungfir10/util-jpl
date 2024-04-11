import os
from natsort import natsorted
from PIL import Image, ImageDraw, ImageFont

cwd = os.path.dirname(__file__)
files = natsorted(os.listdir(os.path.join(cwd, 'split')))

def convert(index):
    try:
        print(files[index])
        image = Image.open(os.path.join(cwd, 'images', 'so', files[index]))
        image.save(os.path.join(cwd, 'splitted', files[index].split('.')[0]+'.pdf'), 'PDF',optimize=True)
        convert(index+1)
    except ValueError:
        convert(index)

convert(0)
