"""Utility functions for text file handling."""

import os
from typing import List, Tuple, Union, Dict, Optional
from .core import TextRankKeywordExtractor

def read_text_file(file_path: str, encoding: str = 'utf-8') -> str:
    """
    Read text from a file.
    
    Args:
        file_path: Path to the text file
        encoding: File encoding (default: 'utf-8')
        
    Returns:
        str: Content of the file
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()

def analyze_text_file(
    file_path: str,
    top_n: Optional[int] = None,
    window_size: int = 5,
    encoding: str = 'utf-8'
) -> List[Tuple[str, float]]:
    """
    Analyze a text file and extract keywords.
    
    Args:
        file_path: Path to the text file
        top_n: Number of top keywords to return. If None, returns all keywords.
        window_size: Size of the sliding window for co-occurrence
        encoding: File encoding (default: 'utf-8')
        
    Returns:
        List of tuples containing (word, score) pairs, sorted by score in descending order
    """
    text = read_text_file(file_path, encoding)
    extractor = TextRankKeywordExtractor(window_size=window_size)
    return extractor.extract_keywords(text, top_n)

def analyze_multiple_files(
    file_paths: List[str],
    top_n: Optional[int] = None,
    window_size: int = 5,
    encoding: str = 'utf-8'
) -> Dict[str, List[Tuple[str, float]]]:
    """
    Analyze multiple text files and extract keywords from each.
    
    Args:
        file_paths: List of paths to text files
        top_n: Number of top keywords to return per file. If None, returns all keywords.
        window_size: Size of the sliding window for co-occurrence
        encoding: File encoding (default: 'utf-8')
        
    Returns:
        Dictionary mapping file paths to their keyword lists
    """
    results = {}
    for file_path in file_paths:
        results[file_path] = analyze_text_file(
            file_path,
            top_n=top_n,
            window_size=window_size,
            encoding=encoding
        )
    return results 