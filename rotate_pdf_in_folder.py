from PyPDF2 import PdfReader, PdfWriter
import os
import shutil
from sys import argv, setrecursionlimit
from natsort import natsorted


def rotate_pdf(path):
    
   folders = natsorted(os.listdir(os.path.join(path)))
   for folder in folders:
      files = natsorted(os.listdir(os.path.join(path, folder)))

      print(folder)
      for file in files:
         filename, ext = os.path.splitext(file)
         if ext == '.pdf':
            try:
               with open(os.path.join(path, folder, file), 'rb') as pdf:
                     filename, _ = os.path.splitext(file)
                     pdf_reader = PdfReader(pdf)
                     pdf_writer = PdfWriter()
                     pdf_writer.add_metadata({'/Title':f'{folder}-{filename}'})
                     for page in pdf_reader.pages:
                        page.rotate(180)
                        pdf_writer.add_page(page)
                     new_filename = f"{filename}-ROTATED-180{ext}"
                     
                     
                     with open(os.path.join(path, folder, new_filename), "wb") as output_file:
                        pdf_writer.write(output_file)
                        pdf.close()
                        output_file.close()

                        os.remove(os.path.join(path, folder, file))
                        os.rename(os.path.join(path, folder, new_filename), os.path.join(path, folder, f"{filename}{ext}"))
            except:
                  os.remove(os.path.join(path, folder, file))

if len(argv) >= 2:
    print('Rotates image...')
    path = argv[1]
    rotate_pdf(path)
else:
    print('No Such File or Directory...')