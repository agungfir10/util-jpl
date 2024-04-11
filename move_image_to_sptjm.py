import shutil
import os
from natsort import natsorted

cwd = os.path.dirname(__file__)
path = "E:\\DOKUMEN OKTOBER JATENG\\IMAGES TO SPTJM"

folders = natsorted(os.listdir(os.path.join(path)))

for folder in folders:
    if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
        os.mkdir(os.path.join(path, folder, 'SPTJM'))
    files = natsorted(os.listdir(os.path.join(path, folder)))
    for file in files:
        shutil.move(os.path.join(path, folder, file), os.path.join(path, folder, 'SPTJM'))