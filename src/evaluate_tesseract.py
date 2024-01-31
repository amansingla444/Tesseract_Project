import Levenshtein
import pytesseract
from PIL import Image

def ocr_image(image_path):
    # Perform OCR on the image using pytesseract
    language_model = '/best/deu-latest-u'
    recognized_text = pytesseract.image_to_string(Image.open(image_path), lang=language_model)
    return recognized_text

def calculate_cer(ground_truth, recognized_text):
    ground_truth = ground_truth.lower()
    recognized_text = recognized_text.lower()

    distance = Levenshtein.distance(ground_truth, recognized_text)
    cer = distance / max(len(ground_truth), len(recognized_text))

    return cer
    

def evaluate_ocr(ground_truth_path, image_path):
    # Read the ground truth text from file
    with open(ground_truth_path, 'r') as file:
        ground_truth_text = file.read()

    # Perform OCR on the image
    recognized_text = ocr_image(image_path)

    # Calculate CER
    cer = calculate_cer(ground_truth_text, recognized_text)

    return cer, recognized_text

# Example usage:
ground_truth_file = '25.gt.txt'
image_path = '25.png'

cer, recognized_text = evaluate_ocr(ground_truth_file, image_path)

print(f"Character Error Rate (CER): {cer}")
print(f"Ground Truth Text: {ground_truth_file}")
print(f"Recognized Text: {recognized_text}")
