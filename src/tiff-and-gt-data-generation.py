import os
from PIL import Image
import pytesseract

# Path to the Tesseract executable (default location on Mac)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

def image_to_text(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image)

    return text

# Specify the input folder containing PNG files
input_folder = '/input_folder'

# Specify the output folder for saving gt.txt and TIF files
output_folder = '/output_folder'

# Ensure the output folder exists, create it if necessary
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Counter for page numbers
page_number = 1

# Process each PNG file in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.png'):
        # Full path to the input PNG file
        input_image_path = os.path.join(input_folder, filename)

        # Get the text from the image
        result_text = image_to_text(input_image_path)

        # Replace newline characters with spaces
        result_text_single_line = result_text.replace('\n', ' ')

        # Open the image using Pillow for saving in TIF format
        image = Image.open(input_image_path)

        # Create the output TIF file path with '.tif' extension
        output_tif_path = os.path.join(output_folder, f'{page_number}.tif')

        # Convert the image to TIF format and save
        image.save(output_tif_path, format='TIFF')

        # Create the output text file path with '.gt.txt' extension
        output_text_path = os.path.join(output_folder, f'{page_number}.gt.txt')

        # Save the result to a text file with '.gt.txt' extension and specified encoding
        with open(output_text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(result_text_single_line)

        print(f"Text saved to: {output_text_path}")
        print(f"TIF image saved to: {output_tif_path}")

        # Increment the page number for the next iteration
        page_number += 1


# In[ ]:




