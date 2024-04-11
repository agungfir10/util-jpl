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
                    perwakilan = ['PERWAKILAN', 'Perwakilan', 'DIWAKILKAN', 'Diwakilkan']
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

                    if any(sub in output_str for sub in so) and 'SEPTEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER', 'SO')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER', 'SO'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SEPTEMBER', 'SO', image))
                    elif any(sub in output_str for sub in gudang) and 'SEPTEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'GUDANG')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER', 'GUDANG'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SEPTEMBER', 'GUDANG', image))
                    elif any(sub in output_str for sub in surat_jalan) and 'SEPTEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'SURAT JALAN')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER', 'SURAT JALAN'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SEPTEMBER', 'SURAT JALAN', image))
                    elif ('MUTLAK' in output_str) and 'SEPTEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER', 'SPTJM'))
                        shutil.move(os.path.join(path,folder,  image), os.path.join(path, folder, 'SEPTEMBER', 'SPTJM', image))
                    elif any(sub in output_str for sub in pengganti) and 'SEPTEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'PENGGANTI')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER', 'PENGGANTI'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SEPTEMBER', 'PENGGANTI', image))
                    elif any(sub in output_str for sub in perwakilan) and 'SEPTEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'PERWAKILAN')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER', 'PERWAKILAN'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SEPTEMBER', 'PERWAKILAN', image))
                    elif 'Pendamping' in output_str and 'SEPTEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER', 'DTT')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER', 'DTT'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SEPTEMBER', 'DTT', image))
                    elif any(sub in output_str for sub in dtt) and 'SEPTEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'SEPTEMBER', 'DTT')):
                            os.mkdir(os.path.join(path, folder, 'SEPTEMBER', 'DTT'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'SEPTEMBER', 'DTT', image))
                    elif any(sub in output_str for sub in so) and 'OKTOBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER'))
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER', 'SO')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER', 'SO'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'OKTOBER', 'SO', image))
                    elif any(sub in output_str for sub in gudang) and 'OKTOBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER'))
                        if not os.path.exists(os.path.join(path, folder, 'GUDANG')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER', 'GUDANG'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'OKTOBER', 'GUDANG', image))
                    elif any(sub in output_str for sub in surat_jalan) and 'OKTOBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER'))
                        if not os.path.exists(os.path.join(path, folder, 'SURAT JALAN')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER', 'SURAT JALAN'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'OKTOBER', 'SURAT JALAN', image))
                    elif ('MUTLAK' in output_str) and 'OKTOBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER'))
                        if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER', 'SPTJM'))
                        shutil.move(os.path.join(path,folder,  image), os.path.join(path, folder, 'OKTOBER', 'SPTJM', image))
                    elif any(sub in output_str for sub in pengganti) and 'OKTOBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER'))
                        if not os.path.exists(os.path.join(path, folder, 'PENGGANTI')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER', 'PENGGANTI'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'OKTOBER', 'PENGGANTI', image))
                    elif any(sub in output_str for sub in perwakilan) and 'OKTOBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER'))
                        if not os.path.exists(os.path.join(path, folder, 'PERWAKILAN')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER', 'PERWAKILAN'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'OKTOBER', 'PERWAKILAN', image))
                    elif 'Pendamping' in output_str and 'OKTOBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER'))
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER', 'DTT')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER', 'DTT'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'OKTOBER', 'DTT', image))
                    elif any(sub in output_str for sub in dtt) and 'OKTOBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER'))
                        if not os.path.exists(os.path.join(path, folder, 'OKTOBER', 'DTT')):
                            os.mkdir(os.path.join(path, folder, 'OKTOBER', 'DTT'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'OKTOBER', 'DTT', image))
                    elif any(sub in output_str for sub in so) and 'NOVEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER', 'SO')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER', 'SO'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'NOVEMBER', 'SO', image))
                    elif any(sub in output_str for sub in gudang) and 'NOVEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'GUDANG')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER', 'GUDANG'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'NOVEMBER', 'GUDANG', image))
                    elif any(sub in output_str for sub in surat_jalan) and 'NOVEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'SURAT JALAN')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER', 'SURAT JALAN'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'NOVEMBER', 'SURAT JALAN', image))
                    elif ('MUTLAK' in output_str) and 'NOVEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER', 'SPTJM'))
                        shutil.move(os.path.join(path,folder,  image), os.path.join(path, folder, 'NOVEMBER', 'SPTJM', image))
                    elif any(sub in output_str for sub in pengganti) and 'NOVEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'PENGGANTI')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER', 'PENGGANTI'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'NOVEMBER', 'PENGGANTI', image))
                    elif any(sub in output_str for sub in perwakilan) and 'NOVEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'PERWAKILAN')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER', 'PERWAKILAN'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'NOVEMBER', 'PERWAKILAN', image))
                    elif 'Pendamping' in output_str and 'NOVEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER', 'DTT')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER', 'DTT'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'NOVEMBER', 'DTT', image))
                    elif any(sub in output_str for sub in dtt) and 'NOVEMBER' in output_str:
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER'))
                        if not os.path.exists(os.path.join(path, folder, 'NOVEMBER', 'DTT')):
                            os.mkdir(os.path.join(path, folder, 'NOVEMBER', 'DTT'))
                        shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'NOVEMBER', 'DTT', image))
                    else:
                        print(output_str)


if len(argv) >= 2:
    print('OCR Ready...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')