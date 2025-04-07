#!/usr/bin/env python
"""
Script to build the TextRank application executable using PyInstaller
"""

import os
import subprocess
import sys

def main():
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the app script
    app_script = os.path.join(script_dir, "text_rank_app.py")
    
    # Check if the app script exists
    if not os.path.exists(app_script):
        print(f"Error: Could not find the application script at {app_script}")
        sys.exit(1)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("PyInstaller is installed.")
    except ImportError:
        print("PyInstaller is not installed. Installing it now...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Build the executable
    print("Building the executable...")
    try:
        # Create a spec file for the application
        spec_file = os.path.join(script_dir, "text_rank_app.spec")
        
        # Prepare PyInstaller command
        pyinstaller_cmd = [
            "pyinstaller",
            "--name=TextRank_App",
            "--onefile",
            "--windowed",
            "--add-data", f"{os.path.join(script_dir, 'text_rank_app.png')};."
        ]
        
        # Add icon if it exists
        icon_path = os.path.join(script_dir, "icon.ico")
        if os.path.exists(icon_path):
            pyinstaller_cmd.extend(["--icon", icon_path])
        
        # Add the app script
        pyinstaller_cmd.append(app_script)
        
        # Run PyInstaller to build the executable
        subprocess.run(pyinstaller_cmd, check=True)
        
        print("\nBuild completed successfully!")
        print(f"The executable is located in the 'dist' directory.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error building the executable: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 