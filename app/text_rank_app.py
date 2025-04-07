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
        
        # Initialize the TextRank extractor
        self.extractor = TextRankKeywordExtractor(window_size=5)
        
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
        
        # Number of keywords to extract
        ttk.Label(control_frame, text="Number of keywords:").pack(side=tk.LEFT, padx=5)
        self.top_n_var = tk.StringVar(value="10")
        self.top_n_entry = ttk.Entry(control_frame, textvariable=self.top_n_var, width=5)
        self.top_n_entry.pack(side=tk.LEFT, padx=5)
        
        # Extract button
        self.extract_btn = ttk.Button(control_frame, text="Extract Keywords", command=self.extract_keywords)
        self.extract_btn.pack(side=tk.RIGHT, padx=5)
        
        # Clear button
        self.clear_btn = ttk.Button(control_frame, text="Clear", command=self.clear_all)
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
            # Get the number of keywords to extract
            top_n = int(self.top_n_var.get())
            
            # Extract keywords
            keywords = self.extractor.extract_keywords(text, top_n=top_n)
            
            # Display the results
            self.keywords_output.delete(1.0, tk.END)
            for word, score in keywords:
                self.keywords_output.insert(tk.END, f"{word}: {score:.4f}\n")
                
        except ValueError:
            self.show_error("Please enter a valid number for the number of keywords.")
        except Exception as e:
            self.show_error(f"Error extracting keywords: {str(e)}")
    
    def clear_all(self):
        self.text_input.delete(1.0, tk.END)
        self.keywords_output.delete(1.0, tk.END)
    
    def show_error(self, message):
        tk.messagebox.showerror("Error", message)

def main():
    root = tk.Tk()
    app = TextRankApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 