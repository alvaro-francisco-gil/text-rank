import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk, messagebox
import os
from text_rank import TextRankKeywordExtractor

class TextRankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TextRank Keyword Extractor")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Initialize the TextRank extractor with default parameters
        self.window_size = 5
        self.extractor = TextRankKeywordExtractor(window_size=self.window_size)
        
        # Create the main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create the input section
        self.create_input_section()
        
        # Create the output section
        self.create_output_section()
        
        # Create the control section
        self.create_control_section()
        
    def create_input_section(self):
        # Input frame
        input_frame = ttk.LabelFrame(self.main_frame, text="Input Text", padding="5")
        input_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Text input area
        self.text_input = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, height=10)
        self.text_input.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # File upload button
        self.upload_btn = ttk.Button(input_frame, text="Upload Text File", command=self.upload_file)
        self.upload_btn.pack(pady=5)
        
    def create_output_section(self):
        # Output frame
        output_frame = ttk.LabelFrame(self.main_frame, text="Extracted Keywords", padding="5")
        output_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Keywords display
        self.keywords_output = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, height=10)
        self.keywords_output.pack(fill=tk.BOTH, expand=True, pady=5)
        
    def create_control_section(self):
        # Control frame
        control_frame = ttk.Frame(self.main_frame)
        control_frame.pack(fill=tk.X, pady=5)
        
        # Parameters frame
        params_frame = ttk.LabelFrame(control_frame, text="Parameters", padding="5")
        params_frame.pack(fill=tk.X, pady=5)
        
        # Window size control
        window_frame = ttk.Frame(params_frame)
        window_frame.pack(fill=tk.X, pady=2)
        ttk.Label(window_frame, text="Window Size:").pack(side=tk.LEFT, padx=5)
        self.window_size_var = tk.StringVar(value=str(self.window_size))
        self.window_size_entry = ttk.Entry(window_frame, textvariable=self.window_size_var, width=5)
        self.window_size_entry.pack(side=tk.LEFT, padx=5)
        ttk.Label(window_frame, text="(Size of the sliding window for co-occurrence)").pack(side=tk.LEFT, padx=5)
        
        # Number of keywords to extract
        keywords_frame = ttk.Frame(params_frame)
        keywords_frame.pack(fill=tk.X, pady=2)
        ttk.Label(keywords_frame, text="Number of keywords:").pack(side=tk.LEFT, padx=5)
        self.top_n_var = tk.StringVar(value="10")
        self.top_n_entry = ttk.Entry(keywords_frame, textvariable=self.top_n_var, width=5)
        self.top_n_entry.pack(side=tk.LEFT, padx=5)
        
        # Buttons frame
        buttons_frame = ttk.Frame(control_frame)
        buttons_frame.pack(fill=tk.X, pady=5)
        
        # Export button
        self.export_btn = ttk.Button(buttons_frame, text="Export Graph", command=self.export_graph)
        self.export_btn.pack(side=tk.RIGHT, padx=5)
        
        # Extract button
        self.extract_btn = ttk.Button(buttons_frame, text="Extract Keywords", command=self.extract_keywords)
        self.extract_btn.pack(side=tk.RIGHT, padx=5)
        
        # Clear button
        self.clear_btn = ttk.Button(buttons_frame, text="Clear", command=self.clear_all)
        self.clear_btn.pack(side=tk.RIGHT, padx=5)
        
    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Text File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_input.delete(1.0, tk.END)
                    self.text_input.insert(tk.END, content)
            except Exception as e:
                self.show_error(f"Error reading file: {str(e)}")
    
    def extract_keywords(self):
        # Get the text from the input area
        text = self.text_input.get(1.0, tk.END).strip()
        
        if not text:
            self.show_error("Please enter some text or upload a file first.")
            return
        
        try:
            # Get the parameters
            top_n = int(self.top_n_var.get())
            window_size = int(self.window_size_var.get())
            
            # Update the extractor with the new window size
            self.extractor = TextRankKeywordExtractor(window_size=window_size)
            
            # Extract keywords
            keywords = self.extractor.extract_keywords(text, top_n=top_n)
            
            # Display the results
            self.keywords_output.delete(1.0, tk.END)
            for word, score in keywords:
                self.keywords_output.insert(tk.END, f"{word}: {score:.4f}\n")
                
        except ValueError:
            self.show_error("Please enter valid numbers for the parameters.")
        except Exception as e:
            self.show_error(f"Error extracting keywords: {str(e)}")
    
    def export_graph(self):
        # Get the text from the input area
        text = self.text_input.get(1.0, tk.END).strip()
        
        if not text:
            self.show_error("Please enter some text or upload a file first.")
            return
        
        try:
            # Get the window size parameter
            window_size = int(self.window_size_var.get())
            
            # Update the extractor with the new window size
            self.extractor = TextRankKeywordExtractor(window_size=window_size)
            
            # Build the co-occurrence graph
            graph = self.extractor.build_cooccurrence_graph(text)
            
            # Ask for the save location
            file_path = filedialog.asksaveasfilename(
                title="Save Pajek Graph",
                defaultextension=".net",
                filetypes=[("Pajek Network Files", "*.net"), ("All Files", "*.*")]
            )
            
            if file_path:
                # Export the graph
                self.extractor.export_pajek(graph, file_path)
                messagebox.showinfo("Success", f"Graph exported successfully to {file_path}")
                
        except ValueError:
            self.show_error("Please enter a valid number for the window size parameter.")
        except Exception as e:
            self.show_error(f"Error exporting graph: {str(e)}")
    
    def clear_all(self):
        self.text_input.delete(1.0, tk.END)
        self.keywords_output.delete(1.0, tk.END)
    
    def show_error(self, message):
        messagebox.showerror("Error", message)

def main():
    root = tk.Tk()
    app = TextRankApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 