import os
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFPageCountError

# Path to the folder containing multiple PDF files
pdf_folder = '/input_folder'
output_folder = '/output_folder'  # Specify your desired output folder

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over all PDF files in the folder
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, pdf_file)

        try:
            # Convert PDF pages to images
            pages = convert_from_path(pdf_path, dpi=300)  # Adjust dpi as needed

            # Save each image in the output folder
            for i, page in enumerate(pages):
                image_path = os.path.join(output_folder, f'{pdf_file}_page_{i + 1}.png')
                page.save(image_path, 'PNG')
                print(f'Saved {image_path}')

        except PDFPageCountError as e:
            print(f"Error processing {pdf_file}: {e}")
            continue


# In[ ]:




