import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import textstat
from tabulate import tabulate

def read_file(filename, encoding):
    try:
        with open(filename, 'r', encoding=encoding) as f:
            return f.read()
    except UnicodeDecodeError:
        print(f"Error reading {filename} with encoding {encoding}")
        return ""

# Load documents
doc1 = read_file('../abby_fine_reader_result_fahr.docx', 'utf-8')
doc2 = read_file('../ocr4al_results_fahr.txt', 'utf-8')
doc3 = read_file('../tesseract_result_fahr.txt', 'utf-8')

documents = {'abby_fine_reader_result_fahr.docx': doc1,
             'ocr4al_results_fahr.txt': doc2,
             'tesseract_result_fahr.txt': doc3}

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(list(documents.values()))

# Readability Scores
readability_scores = []
for filename, doc in documents.items():
    readability_scores.append({
        'Document': filename,
        'Flesch-Kincaid Grade': textstat.flesch_kincaid_grade(doc),
        'Gunning Fog Index': textstat.gunning_fog(doc)
    })

# Print Results in Tabular Format
table_data = []
for score in readability_scores:
    table_data.append([score['Document'], score['Flesch-Kincaid Grade'], score['Gunning Fog Index']])

print("\nReadability Scores:")
print(tabulate(table_data, headers=["Document", "Flesch-Kincaid Grade", "Gunning Fog Index"], tablefmt="pretty"))