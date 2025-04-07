import nltk
nltk.download(['punkt', 'stopwords', 'averaged_perceptron_tagger'])

from .core import TextRankKeywordExtractor

__all__ = ['TextRankKeywordExtractor']