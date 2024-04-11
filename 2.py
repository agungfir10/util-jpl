# menjadikan pdf dari semua file yang sudah di pilah di masing-masing desa
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from natsort import natsorted
import os
from sys import argv

cwd = os.path.dirname(__file__)

def merge_images_to_pdf(path):
    
    folders = natsorted(os.listdir(os.path.join(path)))

    for i,folder in enumerate(folders):
        if i >= 0:
            if os.path.isdir(os.path.join(path, folder)):
                    folder_images = natsorted(os.listdir(os.path.join(path, folder)))
                    
                    for folder_image in folder_images:
                        if os.path.isdir(os.path.join(path, folder, folder_image)):
                            
                            if 'DTT' in folder_image or 'SPTJM' in folder_image or 'PENGGANTI' in folder_image or 'PERWAKILAN' in folder_image:
                                output_pdf = os.path.join(path, folder, folder_image + '.pdf')
                                image_files = natsorted(os.listdir(os.path.join(path, folder, folder_image)))
                                c = canvas.Canvas(output_pdf, pagesize=letter)
                                if len(image_files) != 0:
                                    print(os.path.join(path, folder, folder_image + '.pdf'))
                                    for image_file in image_files:
                                        c.drawImage(os.path.join(path, folder, folder_image, image_file), 0, 0, width=letter[0], height=letter[1])
                                        c.showPage()  # Start a new page for each image
                                    c.setTitle(f"{folder}-{folder_image}")
                                    c.save()

if len(argv) >= 2:
    path = argv[1]
    print('PDF Processing...')
    merge_images_to_pdf(path)
else:
    print('No such file or directory...')    