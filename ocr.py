import fitz  # PyMuPDF
import os
import shutil
import subprocess
from sys import argv
from natsort import natsorted

cwd = os.path.dirname(__file__)

def split_pdf_to_images(index, path):
    all_items = os.listdir(os.path.join(path))
    files = natsorted([file for file in all_items if os.path.isfile(os.path.join(path, file))])

    if index >= len(files):
        print('Splitted Finish...')
    else:
        print(f'{index + 1}/ {len(files)}...')
        pdf_file = os.path.join(path, files[index])
        folder,ext = os.path.splitext(os.path.join(path, files[index]))

        pdf_document = fitz.open(pdf_file)

        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            image_list = page.get_images(full=True)
            
            for img_index, img in enumerate(image_list):
                image = pdf_document.extract_image(img[0])
                image_bytes = image["image"]
                if os.path.exists(os.path.join(path, folder)):
                    with open(os.path.join(path, folder, f"{page_number}.png"), "wb") as image_file:
                        image_file.write(image_bytes)
                else:
                    os.mkdir(os.path.join(path, folder))
                    os.mkdir(os.path.join(path, folder, 'DTT'))
                    os.mkdir(os.path.join(path, folder, 'SPTJM'))
                    os.mkdir(os.path.join(path, folder, 'PENGGANTI'))
                    os.mkdir(os.path.join(path, folder, 'PERWAKILAN'))
                    with open(os.path.join(path, folder, f"{page_number}.png"), "wb") as image_file:
                        image_file.write(image_bytes)

        image_path = natsorted(os.listdir(os.path.join(path, folder)))
        image_files = list(filter(lambda x: 'png' in x, image_path))
        
        for image in image_files:
            command = f'tesseract "{os.path.join(path, folder, image)}" stdout -l ind+eng'
            print(command)

            # Execute the command and capture the output
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            output, _ = process.communicate()
            output_str = output.decode()
            # print(output_str)

            if ('MUTLAK' in output_str):
                shutil.move(os.path.join(path,folder,  image), os.path.join(path, folder, 'SPTJM', image))
            elif 'PENGGANTI' in output_str:
                shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'PENGGANTI', image))
            elif 'PERWAKILAN' in output_str:
                shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'PENGGANTI', image))
            elif 'No Pendamping' in output_str:
                shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'DTT', image))
            else:
                shutil.move(os.path.join(path, folder, image), os.path.join(path, folder, 'DTT', image))

        pdf_document.close()
        split_pdf_to_images(index + 1, path)


if len(argv) >= 2:
    print('Splitted PDF...')
    path = argv[1]
    split_pdf_to_images(0, path)
else:
    print('No Such File or Directory...')
    
# # The command you want to execute
# command = f"tesseract ./contoh-2.jpg stdout -l ind+eng"

# # Execute the command and capture the output
# process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
# output, _ = process.communicate()

# # Decode the output from bytes to string
# output_str = output.decode()

# print(output_str)