from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from natsort import natsorted
import os
from sys import argv

cwd = os.path.dirname(__file__)

def merge_images_to_pdf(index, path):
    print(index)
    
    path_images = natsorted(os.listdir(os.path.join(path)))
    image_files = natsorted(os.listdir(os.path.join(path, path_images[index])))

    output_pdf = os.path.join(path, path_images[index] + '.pdf')
    
    c = canvas.Canvas(output_pdf, pagesize=letter)

    for image_file in image_files:
        c.drawImage(os.path.join(path, path_images[index], image_file), 0, 0, width=letter[0], height=letter[1])
        c.showPage()  # Start a new page for each image

    c.save()
    merge_images_to_pdf(index + 1, path)

if len(argv) >= 2:
    path = argv[1]
    print(path)
    merge_images_to_pdf(0, path)
else:
    print('No such file or directory...')    