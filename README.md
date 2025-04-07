# TextRank Keyword Extraction

A Python library for extracting keywords from text using the TextRank algorithm. This implementation is based on the paper ["TextRank: Bringing Order into Texts"](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf) by Rada Mihalcea and Paul Tarau.

## Installation

```bash
pip install text-rank
```

## Quick Start

```python
from text_rank import TextRankKeywordExtractor

# Create an extractor with default settings
extractor = TextRankKeywordExtractor()

# Your text
text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence 
concerned with the interactions between computers and human language. It is used to apply algorithms to identify 
and extract the natural language rules such that unstructured language data is converted into a form that computers 
can understand.
"""

# Extract keywords
keywords = extractor.extract_keywords(text, top_n=10)
for word, score in keywords:
    print(f"{word}: {score:.4f}")
```

## Features

- Extract keywords from text using the TextRank algorithm
- Customizable window size for co-occurrence graph construction
- Configurable parts of speech (POS) tags for keyword extraction
- Export co-occurrence graphs to Pajek format for visualization
- Built-in stopword removal and text preprocessing
- Utility functions for file handling and batch processing

## Usage

### Basic Usage

```python
from text_rank import TextRankKeywordExtractor

# Initialize the extractor
extractor = TextRankKeywordExtractor()

# Extract keywords from text
text = "Your text here..."
keywords = extractor.extract_keywords(text, top_n=10)
```

### Customizing Parameters

```python
# Initialize with custom parameters
extractor = TextRankKeywordExtractor(
    window_size=5,  # Size of the sliding window for co-occurrence
    pos_tags=('NN', 'NNS', 'JJ', 'JJR', 'JJS')  # Parts of speech to consider
)

# Extract keywords
keywords = extractor.extract_keywords(text, top_n=15)  # Get top 15 keywords
```

### Working with Text Files

The library provides utility functions for working with text files:

```python
from text_rank.utils import analyze_text_file, analyze_multiple_files

# Analyze a single file
keywords = analyze_text_file('your_text_file.txt', top_n=10)

# Analyze multiple files
file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
results = analyze_multiple_files(file_paths, top_n=10)

# Print results for each file
for file_path, keywords in results.items():
    print(f"\nKeywords for {file_path}:")
    for word, score in keywords:
        print(f"{word}: {score:.4f}")
```

### Exporting the Co-occurrence Graph

```python
# Build and export the graph
graph = extractor.build_cooccurrence_graph(text)
extractor.export_pajek(graph, 'output_graph.net')
```

## Parameters

### TextRankKeywordExtractor

- `window_size` (int, default=5): Size of the sliding window for co-occurrence graph construction
- `pos_tags` (tuple, default=('NN', 'NNS', 'JJ', 'JJR', 'JJS')): Parts of speech tags to consider for keyword extraction
  - NN: Noun, singular
  - NNS: Noun, plural
  - JJ: Adjective
  - JJR: Adjective, comparative
  - JJS: Adjective, superlative

### extract_keywords

- `text` (str): The input text to analyze
- `top_n` (int, default=10): Number of top keywords to return

### Utility Functions

#### analyze_text_file
- `file_path` (str): Path to the text file
- `top_n` (int, default=10): Number of top keywords to return
- `window_size` (int, default=5): Size of the sliding window
- `encoding` (str, default='utf-8'): File encoding

#### analyze_multiple_files
- `file_paths` (List[str]): List of paths to text files
- `top_n` (int, default=10): Number of top keywords per file
- `window_size` (int, default=5): Size of the sliding window
- `encoding` (str, default='utf-8'): File encoding

## Dependencies

- nltk
- networkx

## Requirements

Before using the library, make sure to download the required NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
```

## Examples

Check out the `examples` directory for more detailed examples:
- `text_rank_examples.ipynb`: Comprehensive examples of using the library
- `using_text_rank.ipynb`: Basic usage examples

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
