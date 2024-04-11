import shutil
import os
from natsort import natsorted

cwd = os.path.dirname(__file__)
imageFiles = natsorted(os.listdir(os.path.join(cwd, 'move')))

for folder in imageFiles:
    img = natsorted(os.listdir(os.path.join(cwd,'move', folder)))[0]
    ext = img.split('.')[len(img.split('.')) -1 ]
    shutil.copy(os.path.join(cwd, 'move', folder, img),os.path.join(cwd, 'moved', folder + '.' + ext))