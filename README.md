# KSH Earnings Data Analysis Tool

A Python application for analyzing Hungarian KSH (Central Statistical Office) earnings data with visualization and statistical analysis.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Common Setup Steps (All Platforms)

1. **Download/clone the project files** to your local machine
2. **Navigate to the project directory** using your terminal/command prompt
3. **Ensure the data file** `stadat-mun0206-20.2.2.9-hu.xlsx` is in the project folder

## Platform-Specific Installation

### Windows

**Open Command Prompt or PowerShell:**

```cmd
# Navigate to project directory
cd "path\to\your\project\directory"

# Create virtual environment
python -m venv venv

# Activate virtual environment
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
venv\Scripts\activate

# Install dependencies
python -m pip install -r requirements.txt

# Run the analysis
python main.py
```

### Linux / Ubuntu

**Open Terminal:**

```bash
# Navigate to project directory
cd /path/to/your/project/directory

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python main.py
```

### macOS

**Open Terminal:**

```bash
# Navigate to project directory
cd /path/to/your/project/directory

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python main.py
```

## Alternative: Using conda (All Platforms)

If you prefer using conda package manager:

```bash
# Create conda environment
conda create -n ksh-analysis python=3.9

# Activate environment
conda activate ksh-analysis

# Install packages
conda install pandas matplotlib seaborn scikit-learn numpy openpyxl

# Run analysis
python main.py
```

## Project Structure

The project is organized into modular components:

```
├── main.py              # Main execution script
├── config.py            # Configuration settings
├── data_processor.py    # Data loading and preprocessing
├── visualizer.py        # Chart creation and plotting
├── analyzer.py          # Statistical analysis functions
├── utils.py             # Utility functions
├── requirements.txt     # Package dependencies
└── diagrams/            # Output folder (created automatically)
```

## Expected Output

The analysis generates the following files in the `diagrams/` folder:
- **County charts**: Individual earning trend charts for each region
- **National line chart**: Overall country earnings trend
- **Regression plot**: Scatter plot with trend line analysis
- **Console output**: Statistical summary and regression results

## Post-Analysis Cleanup

When finished working with the project:

```bash
# Deactivate virtual environment
deactivate
```