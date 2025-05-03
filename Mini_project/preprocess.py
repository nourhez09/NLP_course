import re
import nltk
from nltk.corpus import stopwords

def preprocess_text(text, remove_stopwords=False):
    """
    Preprocess a single text string.
    Steps:
    - Lowercasing
    - Removing HTML tags
    - Removing punctuation and numbers
    - Optionally removing stopwords
    """
    # Lowercase
    text = text.lower()
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove punctuation and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    if remove_stopwords:
        # Remove stopwords if specified
        nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words('english'))
        text = ' '.join([word for word in text.split() if word not in stop_words])
    
    return text
