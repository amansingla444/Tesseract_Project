import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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
doc1 = read_file('abby_fine_reader_result_fahr.docx', 'utf-8')
doc2 = read_file('ocr4al_results_fahr.txt', 'utf-8')
doc3 = read_file('tesseract_result_fahr.txt', 'utf-8')

documents = {'abby_fine_reader_result_fahr.docx': doc1,
             'ocr4al_results_fahr.txt': doc2,
             'tesseract_result_fahr.txt': doc3}

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(list(documents.values()))

# Cosine Similarity
cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# Readability Scores
readability_scores = []
for filename, doc in documents.items():
    readability_scores.append({
        'Document': filename,
        'Flesch-Kincaid Grade': textstat.flesch_kincaid_grade(doc),
        'Gunning Fog Index': textstat.gunning_fog(doc),
        'Coleman-Liau Index': textstat.coleman_liau_index(doc)
    })

# Print Results in Tabular Format
table_data = []
for i, sim in enumerate(cosine_similarities):
    table_data.append([list(documents.keys())[0], list(documents.keys())[i+1], sim])

print("\nCosine Similarity:")
print(tabulate(table_data, headers=["Document 1", "Document 2", "Cosine Similarity"], tablefmt="pretty"))

table_data = []
for score in readability_scores:
    table_data.append([score['Document'], score['Flesch-Kincaid Grade'], score['Gunning Fog Index'], score['Coleman-Liau Index']])

print("\nReadability Scores:")
print(tabulate(table_data, headers=["Document", "Flesch-Kincaid Grade", "Gunning Fog Index", "Coleman-Liau Index"], tablefmt="pretty"))