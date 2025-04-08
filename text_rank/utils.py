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
    # List of encodings to try if the specified one fails
    encodings_to_try = [encoding, 'latin-1', 'cp1252', 'iso-8859-1']
    
    for enc in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            # If this is the last encoding to try, re-raise the exception
            if enc == encodings_to_try[-1]:
                raise
            # Otherwise, continue to the next encoding
            continue
    # This should never be reached, but just in case
    raise UnicodeDecodeError(f"Failed to decode {file_path} with any of the attempted encodings")

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

def export_multiple_graphs_to_pajek(
    file_paths: List[str],
    output_dir: str,
    window_size: int = 5,
    encoding: str = 'utf-8',
    single_file: bool = False
) -> Dict[str, str]:
    """
    Process multiple text files and export their co-occurrence graphs to Pajek format.
    
    Args:
        file_paths: List of paths to text files
        output_dir: Directory where the Pajek files will be saved
        window_size: Size of the sliding window for co-occurrence
        encoding: File encoding (default: 'utf-8')
        single_file: If True, export all graphs to a single file with separators
        
    Returns:
        Dictionary mapping input file paths to their corresponding Pajek file paths
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize the extractor
    extractor = TextRankKeywordExtractor(window_size=window_size)
    
    # Process each file
    result = {}
    
    if single_file:
        # Export all graphs to a single file
        combined_path = os.path.join(output_dir, "combined_graphs.net")
        
        try:
            with open(combined_path, 'w', encoding=encoding) as combined_file:
                for i, file_path in enumerate(file_paths):
                    try:
                        # Read the text file
                        text = read_text_file(file_path, encoding)
                        
                        # Build the co-occurrence graph
                        graph = extractor.build_cooccurrence_graph(text)
                        
                        # Add a separator with the filename
                        base_name = os.path.basename(file_path)
                        combined_file.write(f"\n*Network {base_name}\n")
                        
                        # Write vertices
                        combined_file.write(f"*Vertices {len(graph.nodes())}\n")
                        for j, node in enumerate(graph.nodes(), 1):
                            combined_file.write(f'{j} "{node}"\n')
                        
                        # Write edges
                        combined_file.write("*Edges\n")
                        for u, v, data in graph.edges(data=True):
                            combined_file.write(f"{list(graph.nodes()).index(u)+1} {list(graph.nodes()).index(v)+1} {data['weight']}\n")
                        
                        # Store the mapping (all files map to the same combined file)
                        result[file_path] = combined_path
                    except Exception as e:
                        print(f"Warning: Could not process file {file_path}: {str(e)}")
                        continue
        except Exception as e:
            print(f"Error writing combined file: {str(e)}")
            # Fall back to writing individual files
            single_file = False
            print("Falling back to writing individual files...")
    
    if not single_file:
        # Export each graph to a separate file
        for file_path in file_paths:
            try:
                # Read the text file
                text = read_text_file(file_path, encoding)
                
                # Build the co-occurrence graph
                graph = extractor.build_cooccurrence_graph(text)
                
                # Generate output filename based on input filename
                base_name = os.path.basename(file_path)
                name_without_ext = os.path.splitext(base_name)[0]
                pajek_path = os.path.join(output_dir, f"{name_without_ext}.net")
                
                # Export the graph to Pajek format
                extractor.export_pajek(graph, pajek_path)
                
                # Store the mapping
                result[file_path] = pajek_path
            except Exception as e:
                print(f"Warning: Could not process file {file_path}: {str(e)}")
                continue
    
    return result 