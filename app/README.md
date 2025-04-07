# TextRank Keyword Extractor - Windows Application

This is a simple Windows application for extracting keywords from text using the TextRank algorithm.

![TextRank Application Screenshot](text_rank_app.png)

## Features

- Upload text files or paste text directly
- Extract keywords with customizable number of results
- Simple and intuitive user interface
- Displays keyword scores

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

2. **Configure Extraction**:
   - Set the number of keywords you want to extract (default is 10)

3. **Extract Keywords**:
   - Click the "Extract Keywords" button
   - The extracted keywords and their scores will appear in the output area

4. **Clear**:
   - Click the "Clear" button to reset both input and output areas

## Troubleshooting

If you encounter any issues:

1. Make sure you have installed all required dependencies
2. Check that the text_rank library is properly installed
3. Ensure you have sufficient text in the input area before extraction

## License

This application is part of the TextRank project and is licensed under the same terms as the main project. 