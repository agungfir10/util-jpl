import os
from PIL import Image, ImageDraw, ImageFont
from natsort import natsorted
from sys import argv

upper_perc = float(argv[1]) if len(argv) >= 2 else 0
right_perc = float(argv[2]) if len(argv) >= 2 else 0
bottom_perc = float(argv[3]) if len(argv) >= 2 else 0
left_perc = float(argv[4]) if len(argv) >= 2 else 0

cwd = os.path.dirname(__file__)
files = natsorted(os.listdir(os.path.join(cwd, 'crop')))

def crop_image_with_percentage(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Get image dimensions
    width, height = img.size
    
    # Calculate cropping box
    upper = int(height * upper_perc)
    right = int(width * right_perc)
    lower = int(height * bottom_perc)
    left = int(width * left_perc)
    
    # Crop the image
    cropped_img = img.crop((left, upper, right, lower))
    
    return cropped_img

def convert_to_img_cropped(index):
    print(index)
    img = crop_image_with_percentage(os.path.join(cwd, 'crop', files[index]))
    # img = crop_image_with_percentage(os.path.join(cwd, 'cropped', files[index]), 0.2, 1, 0.5, 0.4)
    draw =  ImageDraw.Draw(img)

    font = ImageFont.truetype('arial.ttf', size=40)

    position= (0,0)

    text_color= (0, 0, 0)
    draw.text(position, files[index], fill=text_color, font=font)

    img.save(os.path.join(cwd, 'cropped', files[index]))
    convert_to_img_cropped(index+1)

convert_to_img_cropped(0)