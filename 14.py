import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted
import shutil
import subprocess

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_folders = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])

    for i, folder in enumerate(folders):
        print(f'{i+1}/{len(folders)}')

        if not os.path.exists(os.path.join(path, folder)):
            os.mkdir(os.path.join(path, folder))
        
        if os.path.exists(os.path.join(path, folder, 'DTT.pdf')):

            pdf_file = os.path.join(path, folder, 'DTT.pdf')

            pdf_document = fitz.open(pdf_file)
            
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]

                image_list = page.get_displaylist()
                mx = fitz.Matrix(2, 2)
                image = image_list.get_pixmap(matrix = mx)

                image.pil_save(os.path.join(path, folder, f"{page_num}.jpg"), optimize=False)
                command = f'tesseract "{os.path.join(path, folder, f"{page_num}.jpg")}" stdout -l ind+eng'

                print(command)

                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                output, _ = process.communicate()
                output_str = output.decode()

                gudang = ['GUDANG', 'BAST GUDANG', 'BASTGUDANG']
                surat_jalan = ['SURATJALAN', 'SURAT JALAN']
                pengganti = ['PENGGANTI', 'Pengganti']
                so = ['NPWP']
                dtt = [
                    'QR CODE',
                    'QRCODE',
                    'QREODE',
                    'QR',
                    'halaman:',
                    'halaman :',
                    'Saya yang bertanda tangan dibawah',
                    'Saya yang bertanda rangan dibawah', 
                    'Saya yang bertenen tangan dibawah',
                    'Alokasi :',
                    'Alokasi:',
                    ]

                if any(sub in output_str for sub in so):
                    if not os.path.exists(os.path.join(path, folder, 'SO')):
                        os.mkdir(os.path.join(path, folder, 'SO'))
                    shutil.move(os.path.join(path, folder, f"{page_num}.jpg"), os.path.join(path, folder, 'SO', f"{page_num}.jpg"))
                elif any(sub in output_str for sub in gudang):
                    if not os.path.exists(os.path.join(path, folder, 'GUDANG')):
                        os.mkdir(os.path.join(path, folder, 'GUDANG'))
                    shutil.move(os.path.join(path, folder, f"{page_num}.jpg"), os.path.join(path, folder, 'GUDANG', f"{page_num}.jpg"))
                elif any(sub in output_str for sub in surat_jalan):
                    if not os.path.exists(os.path.join(path, folder, 'SURAT JALAN')):
                        os.mkdir(os.path.join(path, folder, 'SURAT JALAN'))
                    shutil.move(os.path.join(path, folder, f"{page_num}.jpg"), os.path.join(path, folder, 'SURAT JALAN', f"{page_num}.jpg"))
                elif ('MUTLAK' in output_str):
                    if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
                        os.mkdir(os.path.join(path, folder, 'SPTJM'))
                    shutil.move(os.path.join(path,folder,  f"{page_num}.jpg"), os.path.join(path, folder, 'SPTJM', f"{page_num}.jpg"))
                elif any(sub in output_str for sub in pengganti):
                    if not os.path.exists(os.path.join(path, folder, 'PENGGANTI')):
                        os.mkdir(os.path.join(path, folder, 'PENGGANTI'))
                    shutil.move(os.path.join(path, folder, f"{page_num}.jpg"), os.path.join(path, folder, 'PENGGANTI', f"{page_num}.jpg"))
                elif 'PERWAKILAN' in output_str:
                    if not os.path.exists(os.path.join(path, folder, 'PERWAKILAN')):
                        os.mkdir(os.path.join(path, folder, 'PERWAKILAN'))
                    shutil.move(os.path.join(path, folder, f"{page_num}.jpg"), os.path.join(path, folder, 'PERWAKILAN', f"{page_num}.jpg"))
                elif 'Pendamping' in output_str:
                    if not os.path.exists(os.path.join(path, folder, 'DTT')):
                        os.mkdir(os.path.join(path, folder, 'DTT'))
                    shutil.move(os.path.join(path, folder, f"{page_num}.jpg"), os.path.join(path, folder, 'DTT', f"{page_num}.jpg"))
                elif any(sub in output_str for sub in dtt):
                    if not os.path.exists(os.path.join(path, folder, 'DTT')):
                        os.mkdir(os.path.join(path, folder, 'DTT'))
                    shutil.move(os.path.join(path, folder, f"{page_num}.jpg"), os.path.join(path, folder, 'DTT', f"{page_num}.jpg"))
                else:
                    print(output_str)
                
            pdf_document.close()
            os.remove(os.path.join(path, folder, 'DTT.pdf'))

if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images