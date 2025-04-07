import nltk
import os

def ensure_nltk_data():
    """Ensure NLTK data is downloaded"""
    required_data = {
        'stopwords': 'corpora/stopwords',
        'averaged_perceptron_tagger_eng': 'taggers/averaged_perceptron_tagger_eng',
        'universal_tagset': 'taggers/universal_tagset'
    }
    
    for resource, path in required_data.items():
        try:
            nltk.data.find(path)
        except LookupError:
            print(f"Downloading {resource}...")
            nltk.download(resource, quiet=True)

# Run the check when the module is imported
ensure_nltk_data()

from .core import TextRankKeywordExtractor

__all__ = ['TextRankKeywordExtractor']