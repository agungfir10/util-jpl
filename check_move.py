from PyPDF2 import PdfReader, PdfWriter
import os
import shutil
from natsort import natsorted

path = "E:\\DOKUMEN DESEMBER JATENG\\KAB. KENDAL"
pathmove = "E:\\DOKUMEN DESEMBER JATENG\\KAB. KENDAL LENGKAP"
folders = natsorted(os.listdir(os.path.join(path)))

i = 0
for folder in folders:
   files = natsorted(os.listdir(os.path.join(path, folder)))
   if os.path.exists(os.path.join(path, folder, 'DTT.pdf')) and os.path.exists(os.path.join(path, folder, 'SPTJM.pdf')) and os.path.exists(os.path.join(path, folder, 'PENGGANTI.pdf')) and os.path.exists(os.path.join(path, folder, 'PERWAKILAN.pdf')):
    shutil.move(os.path.join(path, folder), os.path.join(pathmove, folder))

    # desa = folder.split('-')[2]
    # if not os.path.exists(os.path.join(path, folder, f'{desa}.pdf')):
    #     print(folder, 'ADA FILE')
      



