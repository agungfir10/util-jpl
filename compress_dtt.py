from subprocess import Popen
import os
from natsort import natsorted
from sys import argv
import shutil

cwd = os.path.dirname(__file__)
compress_arg = argv[1] if len(argv) >= 2 else 'default'
path = os.path.join(argv[2])
folders = natsorted(os.listdir(os.path.join(path)))
max_file_size = 19000000

def type_compress(type):
    if type == 'extreme':
        return '/screen'
    elif type == 'high':
        return '/ebook'
    elif type == 'medium':
        return '/printer'
    elif type == 'low':
        return '/prepress'
    else:
        return '/default'
    
def compress_pdf(index):
    if len(folders) == 0:
        print('File PDF kosong')
    else:
        if index >= len(folders):
            print('Selesai...')
        else:
            file = os.path.join(path, folders[index], 'DTT.pdf')    
            if os.path.exists(file) :

                file_size = os.path.getsize(file)

                if file_size > max_file_size:

                    input_file = os.path.join(path, folders[index], 'DTT.pdf')
                    print('FILENAME', input_file)
                    type = type_compress(compress_arg)
                    output_folder = os.path.join(path, folders[index], 'DTT-compressed.pdf')
                    command = f'gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS={type} -dPageRotation=180 -dNOPAUSE -dQUIET -dBATCH -sOutputFile="{output_folder}" "{input_file}"'
                    process = Popen(command)
                    output, error = process.communicate()
                    if error:
                        print(error)
                    else:
                        print(f"Compressed... {index + 1}/{len(folders)}")
                        os.remove(os.path.join(path, folders[index], 'DTT.pdf'))
                        os.rename(os.path.join(path, folders[index], 'DTT-compressed.pdf'), os.path.join(path, folders[index], 'DTT.pdf'))
                        compress_pdf(index + 1)
                else:
                    compress_pdf(index + 1)
            else:
                compress_pdf(index + 1)


print('Compress PDF Processing...')
print(f'Level : {type_compress(compress_arg)}')
compress_pdf(0)