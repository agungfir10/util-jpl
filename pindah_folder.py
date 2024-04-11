import fitz  # PyMuPDF
import os
from sys import argv
from natsort import natsorted
import shutil
import subprocess

cwd = os.path.dirname(__file__)

path = 'E:\\HASIL\\KAB. TEGAL TAMBAHAN 3'
all_folders = os.listdir(os.path.join(path))
folders = natsorted([folder for folder in all_folders if os.path.isdir(os.path.join(path, folder))])

for i,folder in enumerate(folders):
    all_sub_folders = os.listdir(os.path.join(path, folder))
    sub_folders =  natsorted([sub_folder for sub_folder in all_sub_folders if os.path.isdir(os.path.join(path,folder, sub_folder))])

    for i,sub_folder in enumerate(sub_folders):
        if 'NOV' in sub_folder:
            os.rename(os.path.join(path, folder, sub_folder), os.path.join(path, folder, folder))
            shutil.move(os.path.join(path, folder, folder), os.path.join('E:\\HASIL\\KAB. TEGAL TAMBAHAN 3 NOV'))
