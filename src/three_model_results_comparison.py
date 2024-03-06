# This python script is for comparing the results obtained from AbbyFineReader, OCR4al model, and our model
# The AbbyFineReader results is in .docx file format, whereas the OCR4al and our model results are in .txt format
# Before running this python script, results_readability_check.py script has to be executed to identify which model results
# is best among other models. The results_readability_check.py outputed the results from AbbyFineReader is the best in terms of readability
# So, here in this script, the other model results are compared with AbbyFineReader , and calculated how much the similarity and differences.
import Levenshtein
import docx2txt
from tabulate import tabulate
import matplotlib.pyplot as plt

def read_abby_result(docx_file_path):
    return docx2txt.process(docx_file_path)

def read_ocr4al_result(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_tesseract_result(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        return file.read()

def evaluate_ocr_files(file1_path, file2_path):
    # Read OCR results from files
    if file1_path.endswith(".docx"):
        model1_result = read_abby_result(file1_path)
    else:
        model1_result = read_ocr4al_result(file1_path)

    if file2_path.endswith(".docx"):
        model2_result = read_abby_result(file2_path)
    else:
        model2_result = read_ocr4al_result(file2_path)

    # Calculate Levenshtein distance between the two OCR results
    distance = Levenshtein.distance(model1_result, model2_result)

    # Calculate similarity as a percentage
    max_length = max(len(model1_result), len(model2_result))
    similarity = 100 - (distance / max_length) * 100

    return similarity

if __name__ == "__main__":
    # Example file paths (replace these with your actual file paths)
    abby_file_path = "abby_fine_reader_result_fahr.docx"
    ocr4al_file_path = "ocr4al_results_fahr.txt"
    tesseract_file_path = "tesseract_result_fahr.txt"

    # Evaluate OCR results from Abby FineReader .docx and OCR4AL .txt files
    similarity_abby_ocr4al = evaluate_ocr_files(abby_file_path, ocr4al_file_path)

    # Evaluate OCR results from Abby FineReader .docx and Tesseract .txt files
    similarity_abby_tesseract = evaluate_ocr_files(abby_file_path, tesseract_file_path)

    # Evaluate OCR results from OCR4AL .txt and Tesseract .txt files
    similarity_ocr4al_tesseract = evaluate_ocr_files(ocr4al_file_path, tesseract_file_path)

    # Determine which OCR results give the best similarity
    best_result = max(similarity_abby_ocr4al, similarity_abby_tesseract, similarity_ocr4al_tesseract)

    # Create a table to display the results
    results_table = [
        ["Abby FineReader vs OCR4AL", f"{similarity_abby_ocr4al:.2f}%"],
        ["Abby FineReader vs Tesseract", f"{similarity_abby_tesseract:.2f}%"],
        ["OCR4AL vs Tesseract", f"{similarity_ocr4al_tesseract:.2f}%"]
    ]

    # Print the table
    table_headers = ["Comparison", "Similarity"]
    print(tabulate(results_table, headers=table_headers, tablefmt="pretty"))

    # Create a bar chart for better visualization
    comparisons = ["Abby vs OCR4AL", "Abby vs Tesseract", "OCR4AL vs Tesseract"]
    similarities = [similarity_abby_ocr4al, similarity_abby_tesseract, similarity_ocr4al_tesseract]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(comparisons, similarities, color=['blue', 'orange', 'green'])
    plt.xlabel('Comparison')
    plt.ylabel('Similarity (%)')
    plt.title('OCR Comparison Results')
    plt.ylim(0, 100)

    # Add numerical results to each bar
    for bar, similarity in zip(bars, similarities):
        plt.text(bar.get_x() + bar.get_width() / 2 - 0.15, bar.get_height() + 2, f"{similarity:.2f}%", fontsize=10,
                 color='black')

    plt.show()
