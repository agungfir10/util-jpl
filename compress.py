from subprocess import Popen
import os
from natsort import natsorted
from sys import argv

cwd = os.path.dirname(__file__)
compress_arg = argv[1] if len(argv) >= 2 else 'default'
path = argv[2]
files = natsorted(os.listdir(os.path.join(path)))

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
    if len(files) == 0:
        print('File PDF kosong')
    else:
        if index >= len(files):
            print('Selesai...')
        else:
            file = files[index]
            input_file = os.path.join(cwd, 'compress', file)
            type = type_compress(compress_arg)
            output_folder = os.path.join(cwd, 'compressed', file)
            command = f'gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS={type} -dPageRotation=180 -dNOPAUSE -dQUIET -dBATCH -sOutputFile={output_folder} {input_file}'
            process = Popen(command)
            output, error = process.communicate()
            if error:
                print(error)
            else:
                print(f"Compressed... {index + 1}/{len(files)}")
                compress_pdf(index + 1)


print('Compress PDF Processing...')
print(f'Level : {type_compress(compress_arg)}')
compress_pdf(0)