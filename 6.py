import fitz  # PyMuPDF
import os
import shutil
import subprocess
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(index, path):
    all_items = os.listdir(os.path.join(path))
    files = natsorted([file for file in all_items if os.path.isfile(os.path.join(path, file))])

    if index >= len(files):
        print('Splitted Finish...')
    else:
        print(f'{index + 1}/ {len(files)}...')
        folder,ext = os.path.splitext(os.path.join(path, files[index]))

        image_path = natsorted(os.listdir(os.path.join(path, folder)))
        image_files = list(filter(lambda x: 'png' in x, image_path))
        
        for image, i in image_files:
            print(i)

            command = f'tesseract "{os.path.join(path, folder, image)}" stdout -l ind+eng'
            print(command)

            # Execute the command and capture the output
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            output, _ = process.communicate()
            output_str = output.decode()
            # print(output_str)
            gudang = ['GUDANG', 'BAST GUDANG', 'BASTGUDANG']
            surat_jalan = ['SURATJALAN', 'SURAT JALAN']
            so = ['NPWP']
            dtt = ['QR CODE', 'QRCODE', 'halaman:']

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
                shutil.move(os.path.join(path,folder,  image), os.path.join(path, folder, 'SPTJM', image))
            elif 'PENGGANTI' in output_str:
                shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'PENGGANTI', image))
            elif 'PERWAKILAN' in output_str:
                shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'PERWAKILAN', image))
            elif 'Pendamping' in output_str:
                shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'DTT', image))
            elif any(sub in output_str for sub in dtt):
                shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'DTT', image))

        split_pdf_to_images(index + 1, path)


if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(0, path)
else:
    print('No Such File or Directory...')
    
# # The command you want to execute
# command = f"tesseract ./contoh-2.jpg stdout -l ind+eng"

# # Execute the command and capture the output
# process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
# output, _ = process.communicate()

# # Decode the output from bytes to string
# output_str = output.decode()

# print(output_str)