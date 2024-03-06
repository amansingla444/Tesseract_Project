import platform
from tempfile import TemporaryDirectory
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# The below code is for windows machines
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    path_to_poppler_exe = Path(r"C:\.....")

    out_directory = Path(r"~\Desktop").expanduser()
else:
    out_directory = Path("~").expanduser()

PDF_file = Path(r"gdr_document.pdf")  #Give the name of the PDF document used of ocr text extracting
image_file_list = []
text_file = out_directory / Path("gdr_document.txt") #Name and path of the result text file

def main():
    with TemporaryDirectory() as tempdir:
        """
        Part #1 : Converting PDF to images
        """

        if platform.system() == "Windows":
            pdf_pages = convert_from_path(
                PDF_file, 500, poppler_path=path_to_poppler_exe
            )
        else:
            pdf_pages = convert_from_path(PDF_file, 500)
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            page.save(filename, "JPEG")
            image_file_list.append(filename)

        """
        Part #2 - Recognizing text from the images using OCR
        """

        with open(text_file, "a") as output_file:
            for image_file in image_file_list:
                language_model = 'deu-latest-u'  #The language model is the trained data model created from tesstrain-best training
                text = str(((pytesseract.image_to_string(Image.open(image_file),lang=language_model))))
                text = text.replace("-\n", "")
                output_file.write(text)
if __name__ == "__main__":
    main()
