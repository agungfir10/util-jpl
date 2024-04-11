# menghapus folder yang tidak diperlukan ketika selesai menjadi semua pdf
from natsort import natsorted
import shutil
import os
from sys import argv

cwd = os.path.dirname(__file__)

def merge_images_to_pdf(path):
    
    folders = natsorted(os.listdir(os.path.join(path)))

    for i,folder in enumerate(folders):
        print(f'{i+1}/{len(folders)}')

        if os.path.isdir(os.path.join(path, folder)):
            folder_images = natsorted(os.listdir(os.path.join(path, folder)))
            
            for folder_image in folder_images:
                if os.path.isdir(os.path.join(path, folder, folder_image)):
                    files = os.listdir(os.path.join(path, folder, folder_image))
                    if len(files) == 0:
                        shutil.rmtree(os.path.join(path, folder, folder_image))
                    else:
                        if 'DTT' in folder_image or 'SPTJM' in folder_image or 'PENGGANTI' in folder_image or 'PERWAKILAN' in folder_image:
                            shutil.rmtree(os.path.join(path, folder, folder_image))
                        
        else:
            os.remove(os.path.join(path, folder))

if len(argv) >= 2:
    path = argv[1]
    print('Delete Processing...')
    merge_images_to_pdf(path)
else:
    print('No such file or directory...')    