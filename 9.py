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
        all_sub_folders = os.listdir(os.path.join(path, folder, 'SEP'))
        sub_folders = natsorted([sub_folder for sub_folder in all_sub_folders if os.path.isdir(os.path.join(path, folder, 'SEP', sub_folder))])
        # all_sub_folders = os.listdir(os.path.join(path, folder))
        # sub_folders = natsorted([sub_folder for sub_folder in all_sub_folders if os.path.isdir(os.path.join(path, folder, sub_folder))])

        for sub_folder in sub_folders:
            # new_name = f'{sub_folder.replace('SEP ', '')}'
            # new_name = f'KAB. KENDAL-{folder}-{sub_folder}'
            # os.rename(os.path.join(path, folder, 'SEP', sub_folder), os.path.join(path, folder, 'SEP', new_name ))
            # pErintah baru
            # if not os.path.exists(os.path.join(path, folder, 'SEP')):
            #     os.mkdir(os.path.join(path, folder, 'SEP'))

            # if 'SEP' in sub_folder:
            #     shutil.move(os.path.join(path, folder, sub_folder), os.path.join(path, folder, 'SEP'))

            shutil.move(os.path.join(path, folder, 'SEP', sub_folder), 'E:\\HASIL\\KOTA SEMARANG TAMBAHAN 1 SEP')
            # os.rename(os.path.join(path, folder, 'SEP', sub_folder), os.path.join(path, folder, 'SEP', f'KOTA SEMARANG-{folder}-{sub_folder}'))


if len(argv) >= 2:
    print('Proses memindah...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('Tidak ada file atau direktori...')