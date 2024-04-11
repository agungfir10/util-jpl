from subprocess import Popen
import os
from natsort import natsorted
from sys import argv, setrecursionlimit
import shutil
setrecursionlimit(99999999)

cwd = os.path.dirname(__file__)
compress_arg = argv[1] if len(argv) >= 2 else 'default'
path = os.path.join(argv[2])
folders = natsorted(os.listdir(os.path.join(path)))
max_file_size = 19048576

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


def total_pdf_length(root_dir, max_depth=3):
    total_length = 0

    for root, _, files in os.walk(root_dir):
        depth = root[len(root_dir) + 1:].count(os.sep)
        if depth <= max_depth:
            for file in files:
                if file.lower().endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    total_length += os.path.getsize(file_path)

    return total_length

def compress_pdf():
    for folder in folders:
        files = natsorted(os.listdir(os.path.join(path, folder)))
        for file in files:
            if os.path.exists(os.path.join(path, folder, file)) :

                file_size = os.path.getsize(os.path.join(path, folder, file))

                if file_size > max_file_size:

                    input_file = os.path.join(path, folder, file)
                    type = type_compress(compress_arg)
                    filename, ext = os.path.splitext(os.path.join(path, folder, file))
                    if ext == '.pdf':
                        output_folder = os.path.join(path, folder, f"{filename}-compressed.{ext}")
                        command = f'gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS={type} -dPageRotation=180 -dNOPAUSE -dQUIET -dBATCH -sOutputFile="{output_folder}" "{input_file}"'
                        process = Popen(command)
                        output, error = process.communicate()
                        if error:
                            print(error)
                        else:
                            print(f"Compressed... {os.path.join(folder, file)}")
                            os.remove(os.path.join(path, folder, file))
                            os.rename(os.path.join(path, folder, f"{filename}-compressed.{ext}"), os.path.join(path, folder, file))



print('Compress PDF Processing...')
print(f'Level : {type_compress(compress_arg)}')
compress_pdf()