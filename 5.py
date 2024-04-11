from pdf2image import convert_from_path
import os
from sys import argv, setrecursionlimit
from natsort import natsorted
setrecursionlimit(9999999)

cwd = os.path.dirname(__file__)

def split_pdf_to_images(path):
    all_items = os.listdir(os.path.join(path))
    files = natsorted([file for file in all_items if os.path.isfile(os.path.join(path, file))])

    for i, file in enumerate(files):
        filepath = os.path.join(path, file)
        print(f"{i+1}/{len(files)}")
        folder,ext = os.path.splitext(os.path.join(path, file))
        images = convert_from_path(filepath)
        for i, image in enumerate(images):
            # ROTATE IMAGE
            rotated_image = image.rotate(0, expand=True)
            if os.path.exists(os.path.join(path, folder)):
                rotated_image.save(os.path.join(path, folder, f'{i}.jpg'))
                if not os.path.exists(os.path.join(path, folder, 'DTT')):
                    os.mkdir(os.path.join(path, folder, 'DTT'))
                if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
                    os.mkdir(os.path.join(path, folder, 'SPTJM'))
                if not os.path.exists(os.path.join(path, folder, 'PENGGANTI')):
                    os.mkdir(os.path.join(path, folder, 'PENGGANTI'))
                if not os.path.exists(os.path.join(path, folder, 'PERWAKILAN')):
                    os.mkdir(os.path.join(path, folder, 'PERWAKILAN'))
                if not os.path.exists(os.path.join(path, folder, 'GUDANG')):
                    os.mkdir(os.path.join(path, folder, 'GUDANG'))
                if not os.path.exists(os.path.join(path, folder, 'SURAT JALAN')):
                    os.mkdir(os.path.join(path, folder, 'SURAT JALAN'))
                if not os.path.exists(os.path.join(path, folder, 'DO')):
                    os.mkdir(os.path.join(path, folder, 'DO'))
                if not os.path.exists(os.path.join(path, folder, 'SPM')):
                    os.mkdir(os.path.join(path, folder, 'SPM'))
            else:
                if not os.path.exists(os.path.join(path, folder)):
                    os.mkdir(os.path.join(path, folder))
                if not os.path.exists(os.path.join(path, folder, 'DTT')):
                    os.mkdir(os.path.join(path, folder, 'DTT'))
                if not os.path.exists(os.path.join(path, folder, 'SPTJM')):
                    os.mkdir(os.path.join(path, folder, 'SPTJM'))
                if not os.path.exists(os.path.join(path, folder, 'PENGGANTI')):
                    os.mkdir(os.path.join(path, folder, 'PENGGANTI'))
                if not os.path.exists(os.path.join(path, folder, 'PERWAKILAN')):
                    os.mkdir(os.path.join(path, folder, 'PERWAKILAN'))
                if not os.path.exists(os.path.join(path, folder, 'GUDANG')):
                    os.mkdir(os.path.join(path, folder, 'GUDANG'))
                if not os.path.exists(os.path.join(path, folder, 'SURAT JALAN')):
                    os.mkdir(os.path.join(path, folder, 'SURAT JALAN'))
                if not os.path.exists(os.path.join(path, folder, 'DO')):
                    os.mkdir(os.path.join(path, folder, 'DO'))
                if not os.path.exists(os.path.join(path, folder, 'SPM')):
                    os.mkdir(os.path.join(path, folder, 'SPM'))
                rotated_image.save(os.path.join(path, folder, f'{i}.jpg'))
    print('Done...')



if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(path)
else:
    print('No Such File or Directory...')
# Split the PDF file into images