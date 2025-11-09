# Utility functions for file operations and text processing

import os
import glob
import unicodedata
import warnings

# Suppress pandas warnings for cleaner output
warnings.filterwarnings('ignore', category=FutureWarning)

def setup_output_directory(diagrams_dir):
    # Create output directory and clear existing files
    os.makedirs(diagrams_dir, exist_ok=True)
    
    # Clean up existing files to ensure fresh analysis results
    existing_files = glob.glob(os.path.join(diagrams_dir, '*'))
    for file_path in existing_files:
        if os.path.isfile(file_path):
            os.remove(file_path)
    
    if existing_files:
        file_count = len([f for f in existing_files if os.path.isfile(f)])
        print(f"Cleared {file_count} existing files from diagrams directory")

def clean_text_for_filename(text):
    # Remove accents and special characters for safe filename
    # Remove accents using Unicode normalization
    cleaned = unicodedata.normalize('NFD', text)
    cleaned = ''.join(c for c in cleaned if unicodedata.category(c) != 'Mn')
    
    # Replace spaces and commas with underscores
    cleaned = cleaned.replace(' ', '').replace(',', '_')
    
    return cleaned

def print_program_info():
    # Display program information to user
    print("Project assignment for Programming Basics course")
    print("Created by Tamás Németh - FGCBKF")
    print("Analyzing gross average earnings in Hungary based on KSH data")