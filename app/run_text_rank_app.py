#!/usr/bin/env python
"""
TextRank Keyword Extractor Application Launcher
"""

import os
import sys
import subprocess

def main():
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the app script
    app_script = os.path.join(script_dir, "text_rank_app.py")
    
    # Check if the app script exists
    if not os.path.exists(app_script):
        print(f"Error: Could not find the application script at {app_script}")
        sys.exit(1)
    
    # Run the application
    try:
        subprocess.run([sys.executable, app_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running the application: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 