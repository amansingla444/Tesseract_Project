# CER and WER evaluation of AbbyFineReader and OCR4al model results
# Inputs :
#       1. Ground truth data ( eg. 25.gt.txt)
#       2. Recognized Text  - equivalent text from the result file
import Levenshtein

def calculate_cer(ground_truth, recognized_text):
    ground_truth = ground_truth.lower()
    recognized_text = recognized_text.lower()

    distance = Levenshtein.distance(ground_truth, recognized_text)
    cer = distance / max(len(ground_truth), len(recognized_text))

    return cer

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
    

def evaluate_ocr(ground_truth_path, recognized_text):
    # Read the ground truth text from file
    with open(ground_truth_path, 'r') as file:
        ground_truth_text = file.read()

    # Calculate CER
    cer = calculate_cer(ground_truth_text, recognized_text)
    wer = calculate_wer(ground_truth_text, recognized_text)

    return wer, cer

# Example usage:
ground_truth_file = 'gdr_document_page_1.gt.txt'                   # Gives the ground truth data , which we defined.
                                                  # This cannot say that the exact ground truth data used by the respective model
                                                  # developers for their evaluation

recognized_text = 'This is the recognized text.'  # Gives the equivalent result data from the results.


wer, cer = evaluate_ocr(ground_truth_file, recognized_text)

print(f"Character Error Rate (CER): {cer}")
print(f"Word Error Rate (CER): {wer}")
print(f"Ground Truth Text (from file): {ground_truth_file}")
print(f"Recognized Text (manual input): {recognized_text}")
