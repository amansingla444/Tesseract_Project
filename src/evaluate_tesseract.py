from pytesseract import image_to_string
from difflib import SequenceMatcher

def calculate_metrics(ground_truth, recognized_text):
    """
    Calculate accuracy, precision, recall, and F1 score.
    """
    correct_chars = sum(a == b for a, b in zip(ground_truth, recognized_text))
    total_chars = len(ground_truth)
    recognized_chars = len(recognized_text)

    accuracy = (correct_chars / total_chars) * 100
    precision = (correct_chars / recognized_chars) * 100 if recognized_chars > 0 else 0
    recall = (correct_chars / total_chars) * 100
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return accuracy, precision, recall, f1_score

def evaluate_tesseract_model(test_images, ground_truth_transcriptions):
    for image_path, ground_truth in zip(test_images, ground_truth_transcriptions):
        # Perform OCR on the test image
        recognized_text = image_to_string(image_path, lang='/best/deu-latest-u')  # Replace 'your_language'

        # Calculate metrics
        accuracy, precision, recall, f1_score = calculate_metrics(ground_truth, recognized_text)

        # Print results for each image
        print(f"Image: {image_path}")
        print(f"Ground Truth: {ground_truth}")
        print(f"Recognized Text: {recognized_text}")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Precision: {precision:.2f}%")
        print(f"Recall: {recall:.2f}%")
        print(f"F1 Score: {f1_score:.2f}%\n")

if __name__ == "__main__":
    # Provide paths to your test images and ground truth transcriptions
    test_images = ["Fahrzeugschlosser_24219 Spezialisierungsrichtungen 01-09-1977.pdf_page_6.png", "Fahrzeugschlosser_24219 Spezialisierungsrichtungen 01-09-1977.pdf_page_77.png", "Fahrzeugschlosser_24219 Spezialisierungsrichtungen 01-09-1977.pdf_page_87.png"]
    ground_truth_transcriptions = ["Fahrzeugschlosser_24219 Spezialisierungsrichtungen 01-09-1977.pdf_page_77.gt.txt", "Fahrzeugschlosser_24219 Spezialisierungsrichtungen 01-09-1977.pdf_page_6.gt.txt", "Fahrzeugschlosser_24219 Spezialisierungsrichtungen 01-09-1977.pdf_page_87.gt.txt"]

    evaluate_tesseract_model(test_images, ground_truth_transcriptions)
