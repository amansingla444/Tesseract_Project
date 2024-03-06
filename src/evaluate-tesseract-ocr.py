# CER and WER evaluation of our model
# Inputs :
#       1. Ground truth data ( eg. 25.gt.txt)
#       2. Recognized Text  - equivalent text from the result file

import Levenshtein
import pytesseract
from PIL import Image
from tabulate import tabulate

"""
Part #1 - Testing tesseract using our model
          Inputs :
            1. language_model : our pre-trained model 
            2. document image
"""
def ocr_image(image_path, language_model='deu-latest-u'):
    # Perform OCR on the image using pytesseract
    recognized_text = pytesseract.image_to_string(Image.open(image_path), lang=language_model)
    return recognized_text


"""
Part #2 - Evaluating CER of  model
          Inputs :
            1. Ground truth data 
            2. Result data derived from Part #1
"""
def calculate_cer(ground_truth, recognized_text):
    ground_truth = ground_truth.lower()
    recognized_text = recognized_text.lower()

    distance = Levenshtein.distance(ground_truth, recognized_text)
    cer = distance / max(len(ground_truth), len(recognized_text))

    return cer

"""
Part #3 - Evaluating WER of  model
          Inputs :
            1. Ground truth data 
            2. Result data derived from Part #1
"""
def calculate_wer(ground_truth, recognized_text):
    # Remove any leading or trailing whitespaces
    ground_truth = ground_truth.strip()
    recognized_text = recognized_text.strip()

    # Tokenize the strings into words
    ground_truth_words = ground_truth.split()
    recognized_words = recognized_text.split()

    # Compute Levenshtein distance
    distance = Levenshtein.distance(ground_truth, recognized_text)

    # Calculate Word Error Rate
    wer = distance / len(ground_truth_words)

    return wer

"""
Part #4 - Evaluating WAR of  model
          Inputs :
            1. WER derived from Part #3
"""
def calculate_war(wer):
    # Calculate Word Accuracy Rate
    war = 1 - wer
    return war


"""
Part #5 - Evaluating CAR of  model
          Inputs :
            1. WER derived from Part #2
"""
def calculate_car(cer):
    # Calculate Character Accuracy Rate
    car = 1 - cer
    return car


def evaluate_ocr(ground_truth_path, image_path):
    # Read the ground truth text from file
    with open(ground_truth_path, 'r') as file:
        ground_truth_text = file.read()

    # Perform OCR on the image
    recognized_text = ocr_image(image_path)

    # Calculate CER, WER, WAR, and CAR
    cer = calculate_cer(ground_truth_text, recognized_text)
    wer = calculate_wer(ground_truth_text, recognized_text)
    war = calculate_war(wer)
    car = calculate_car(cer)

    return wer, cer, war, car, recognized_text


# Example usage:
ground_truth_file = 'gdr_document_page_1.gt.txt'
image_path = 'gdr_document_page_1.png'

wer, cer, war, car, recognized_text = evaluate_ocr(ground_truth_file, image_path)

# Display results in a neat tabular form
results_table = [
    ["Character Error Rate (CER)", f"{cer * 100:.2f}%"],
    ["Word Error Rate (WER)", f"{wer * 100:.2f}%"],
    ["Word Accuracy Rate (WAR)", f"{war * 100:.2f}%"],
    ["Character Accuracy Rate (CAR)", f"{car * 100:.2f}%"],
]

print(tabulate(results_table, headers=["Metric", "Percentage"], tablefmt="grid"))