# TextRank Keyword Extraction

A Python library for extracting keywords from text using the TextRank algorithm. This implementation is based on the paper ["TextRank: Bringing Order into Texts"](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf) by Rada Mihalcea and Paul Tarau.

## Installation

```bash
pip install text-rank
```

## Quick Start

```python
from text_rank import TextRankKeywordExtractor

extractor = TextRankKeywordExtractor()

text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language. It is used to apply algorithms to identify and extract the natural language rules such that unstructured language data is converted into a form that computers can understand.
"""

keywords = extractor.extract_keywords(text)
for word, score in keywords:
    print(f"{word}: {score:.4f}")
```

Example output:
```
language: 0.1190
computers: 0.0784
natural: 0.0774
science: 0.0560
computer: 0.0558
artificial: 0.0557
linguistics: 0.0555
intelligence: 0.0555
interactions: 0.0551
rules: 0.0548
unstructured: 0.0546
human: 0.0545
algorithms: 0.0543
subfield: 0.0495
processing: 0.0434
data: 0.0430
form: 0.0374
```

## Features

- Extract keywords from text using the TextRank algorithm
- Customizable window size for co-occurrence graph construction
- Configurable parts of speech (POS) tags for keyword extraction
- Export co-occurrence graphs to Pajek format for visualization
- Built-in stopword removal and text preprocessing
- Utility functions for file handling and batch processing

## Usage

```python
from text_rank import TextRankKeywordExtractor
```

### Customizing Parameters

```python
# Initialize with custom parameters
extractor = TextRankKeywordExtractor(
    window_size=5,  # Size of the sliding window for co-occurrence
    pos_tags=('NN', 'NNS', 'JJ', 'JJR', 'JJS')  # Parts of speech to consider based in TreeBank
)

# Extract keywords
keywords = extractor.extract_keywords(text, top_n=15)  # Get top 15 keywords
```

### Working with Text Files

The library provides utility functions for working with text files:

```python
from text_rank.utils import analyze_text_file, analyze_multiple_files

# Analyze a single file (all keywords)
keywords = analyze_text_file('your_text_file.txt')

# Analyze a single file (top 10 keywords)
top_keywords = analyze_text_file('your_text_file.txt', top_n=10)

# Analyze multiple files
file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
results = analyze_multiple_files(file_paths)  # Returns all keywords for each file
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
- `top_n` (int, optional): Number of top keywords to return. If None, returns all keywords.

### Utility Functions

#### analyze_text_file
- `file_path` (str): Path to the text file
- `top_n` (int, optional): Number of top keywords to return. If None, returns all keywords.
- `window_size` (int, default=5): Size of the sliding window
- `encoding` (str, default='utf-8'): File encoding

#### analyze_multiple_files
- `file_paths` (List[str]): List of paths to text files
- `top_n` (int, optional): Number of top keywords per file. If None, returns all keywords.
- `window_size` (int, default=5): Size of the sliding window
- `encoding` (str, default='utf-8'): File encoding


## Examples

Check out the `examples` directory for more detailed examples:
- `using_text_rank.ipynb`: Basic usage examples

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
