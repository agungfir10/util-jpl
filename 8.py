import fitz  # PyMuPDF
import os
import shutil
import subprocess
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_items = os.listdir(os.path.join(path))
    folders = natsorted([folder for folder in all_items if os.path.isdir(os.path.join(path, folder))])

    for folder in folders:
        print(folder)

        image_items = os.listdir(os.path.join(path, folder))
        images = natsorted([image for image in image_items if os.path.isfile(os.path.join(path, folder, image))])

        for image in images:
            if '.jpg' in image or '.png' in image:
                if os.path.exists(os.path.join(path, folder, image)):
                    command = f'tesseract "{os.path.join(path, folder, image)}" stdout -l ind+eng'
                    print(folder, image)
                    # Execute the command and capture the output
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
                    output, _ = process.communicate()
                    output_str = output.decode()
                    # print(output_str)

                    output, _ = process.communicate()
                    output_str = output.decode()
                    # print(output_str)
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
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SO', image))
                    elif any(sub in output_str for sub in gudang):
                        if not os.path.exists(os.path.join(path, folder, 'GUDANG')):
                            os.mkdir(os.path.join(path, folder, 'GUDANG'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'GUDANG', image))
                    elif any(sub in output_str for sub in surat_jalan):
                        if not os.path.exists(os.path.join(path, folder, 'SURAT JALAN')):
                            os.mkdir(os.path.join(path, folder, 'SURAT JALAN'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SURAT JALAN', image))
                    elif ('MUTLAK' in output_str):
                        if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
                            os.mkdir(os.path.join(path, folder, 'SPTJM'))
                        shutil.move(os.path.join(path,folder,  image), os.path.join(path, folder, 'SPTJM', image))
                    elif any(sub in output_str for sub in pengganti):
                        if not os.path.exists(os.path.join(path, folder, 'PENGGANTI')):
                            os.mkdir(os.path.join(path, folder, 'PENGGANTI'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'PENGGANTI', image))
                    elif 'PERWAKILAN' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'PERWAKILAN')):
                            os.mkdir(os.path.join(path, folder, 'PERWAKILAN'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'PERWAKILAN', image))
                    elif 'Pendamping' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'DTT')):
                            os.mkdir(os.path.join(path, folder, 'DTT'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'DTT', image))
                    elif any(sub in output_str for sub in dtt):
                        if not os.path.exists(os.path.join(path, folder, 'DTT')):
                            os.mkdir(os.path.join(path, folder, 'DTT'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'DTT', image))
                    else:
                        print(output_str)


if len(argv) >= 2:
    print('OCR Ready...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')