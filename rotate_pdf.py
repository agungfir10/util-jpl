from PyPDF2 import PdfReader, PdfWriter
import os
import shutil
from sys import argv, setrecursionlimit
from natsort import natsorted


def rotate_pdf(path):
    
      files = natsorted(os.listdir(os.path.join(path, )))

      for index,file in enumerate(files):
         print(index, '/', len(files), file)
         filename, ext = os.path.splitext(file)
         if ext == '.pdf':
            try:
               with open(os.path.join(path, file), 'rb') as pdf:
                     filename, _ = os.path.splitext(file)
                     pdf_reader = PdfReader(pdf)
                     pdf_writer = PdfWriter()
                     pdf_writer.add_metadata({'/Title':f'{filename}'})
                     for page in pdf_reader.pages:
                        page.rotate(-90)
                        pdf_writer.add_page(page)
                     new_filename = f"{filename}-ROTATED-180{ext}"
                     
                     
                     with open(os.path.join(path , new_filename), "wb") as output_file:
                        pdf_writer.write(output_file)
                        pdf.close()
                        output_file.close()

                        os.remove(os.path.join(path, file))
                        os.rename(os.path.join(path, new_filename), os.path.join(path, f"{filename}{ext}"))
            except:
                  os.remove(os.path.join(path, file))

if len(argv) >= 2:
    print('Rotasi PDF dimulai...')
    path = argv[1]
    rotate_pdf(path)
else:
    print('Tidak ada file PDF pada direktori...')