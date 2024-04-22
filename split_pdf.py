import PyPDF2

def split_pdf(input_pdf_path, output_folder):
    with open(input_pdf_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(page)

            output_filename = f"{output_folder}/page_{page_num + 1}.pdf"

            with open(output_filename, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
            print(f'Page {page_num + 1} saved as {output_filename}')

# Specify the input PDF file path and output folder
input_pdf_path = 'BLANKO DOKUMEN BAPANG.pdf'
output_folder = 'output'

# Call the function to split the PDF
split_pdf(input_pdf_path, output_folder)