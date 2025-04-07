# TextRank Keyword Extractor - Windows Application

This is a simple Windows application for extracting keywords from text using the TextRank algorithm.

![TextRank Application Screenshot](text_rank_app.png)

## Features

- Upload text files or paste text directly
- Extract keywords with customizable number of results
- Adjust the window size parameter to control co-occurrence graph construction
- Export co-occurrence graphs in Pajek format for visualization
- View keyword scores in a user-friendly interface

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - tkinter (usually comes with Python)
  - text_rank library

## Installation

1. Make sure you have Python installed on your system
2. Install the text_rank library:
   ```
   pip install git+https://github.com/alvaro-francisco-gil/text-rank.git
   ```

## Running the Application

There are two ways to run the application:

### Method 1: Using the launcher script

Simply double-click on the `run_text_rank_app.py` file or run it from the command line:

```
python run_text_rank_app.py
```

### Method 2: Running the application directly

```
python text_rank_app.py
```

## Usage

1. **Input Text**: 
   - Type or paste text directly into the input area, or
   - Click "Upload Text File" to select a text file from your computer

2. **Configure Parameters**:
   - Set the window size (default is 5) - This controls the size of the sliding window for co-occurrence graph construction
   - Set the number of keywords you want to extract (default is 10)

3. **Extract Keywords**:
   - Click the "Extract Keywords" button
   - The extracted keywords and their scores will appear in the output area

4. **Export Graph**:
   - Click the "Export Graph" button to save the co-occurrence graph in Pajek format
   - Choose a location to save the .net file
   - The graph can be visualized using network visualization tools like Pajek, Gephi, or Cytoscape

5. **Clear**:
   - Click the "Clear" button to reset both input and output areas

## Parameters

### Window Size

The window size parameter controls how many words to consider as co-occurring in the text. A larger window size will:
- Capture more distant relationships between words
- Result in a denser co-occurrence graph
- Potentially identify more general keywords

A smaller window size will:
- Focus on more immediate word relationships
- Result in a sparser co-occurrence graph
- Potentially identify more specific keywords

The default value is 5, which is a good balance for most texts.

## Graph Export

The application allows you to export the co-occurrence graph in Pajek format (.net file). This graph represents the relationships between words in your text, where:

- Nodes represent words
- Edges represent co-occurrence relationships
- Edge weights indicate the strength of the relationship

You can visualize this graph using network analysis tools like:
- [Pajek](http://vlado.fmf.uni-lj.si/pub/networks/pajek/)
- [Gephi](https://gephi.org/)
- [Cytoscape](https://cytoscape.org/)

This visualization can help you understand the structure of your text and identify clusters of related terms.

## Troubleshooting

If you encounter any issues:

1. Make sure you have installed all required dependencies
2. Check that the text_rank library is properly installed
3. Ensure you have sufficient text in the input area before extraction

## License

This application is part of the TextRank project and is licensed under the same terms as the main project. 