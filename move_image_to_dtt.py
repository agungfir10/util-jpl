import shutil
import os
from natsort import natsorted

cwd = os.path.dirname(__file__)
path = "D:\\EKS KARESIDENAN PATI\\BAPANG ALOKASI NOVEMBER\\TAMBAHAN III NOVEMBER\\KAB PATI"

folders = natsorted(os.listdir(os.path.join(path)))

for folder in folders:
    if not os.path.exists(os.path.join(path, folder, 'DTT')):
        os.mkdir(os.path.join(path, folder, 'DTT'))
        
    all_items = os.listdir(os.path.join(path, folder))
    files = natsorted([file for file in all_items if os.path.isfile(os.path.join(path, folder, file))])
    for file in files:
        shutil.move(os.path.join(path, folder, file), os.path.join(path, folder, 'DTT'))