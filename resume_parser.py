from typing import List

from PyPDF2 import PdfReader
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# download nltk corpus (first time only)
# nltk.download('all')

# Extract text from pdf

def extract_text_from_pdf(pdf_path) -> str:
    """ This function extracts text from a pdf file and returns it as a string"""

    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text


def analyze_text(text) -> list:
    """ This function extracts key words from a text and returns it as a list"""

    tokens: list[str] = word_tokenize(text)
    #  Removing punctuation
    tokens = [word.lower() for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    return filtered_tokens


resume_text = extract_text_from_pdf('resume.pdf')

keywords = analyze_text(resume_text)

print(keywords)