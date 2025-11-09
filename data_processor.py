# Data loading, preprocessing, and transformation functions

import pandas as pd
import numpy as np
from config import DEBUG, MAX_ROWS, REQUIRED_COLUMNS

def load_and_preprocess_data(file_path):
    # Load Excel data and perform initial preprocessing
    try:
        # Read Excel file with specific parameters for KSH data format
        data_raw = pd.read_excel(
            file_path,
            sheet_name=0,  # First worksheet
            engine='openpyxl',  # Excel engine for .xlsx files
            header=1  # Row 1 contains column headers (skip title row)
        )
        data_raw = data_raw.iloc[1:]  # Skip first data row (category description)
        data_raw = data_raw.iloc[:MAX_ROWS]  # Keep only first rows (exclude percentile data)
        
        if DEBUG:
            print("Columns from the data_raw:", data_raw.columns)
            print("First 5 rows of the data_raw:\n", data_raw.head())
        
        # Validate required columns exist
        if not all(col in data_raw.columns for col in REQUIRED_COLUMNS):
            print("Error: The required columns does not exist in the 'data_raw'")
            exit()
            
        return data_raw
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' is not found.")
        exit()
    except Exception as e:
        print(f"Error during the reading: {e}")
        exit()

def transform_data_to_long_format(data_raw):
    # Transform wide format data to long format using melt operation
    try:
        # Reshape data: columns become rows for easier analysis
        data_long = data_raw.melt(
            id_vars=['Területi egység neve', 'Területi egység szintje'],  # Keep as identifiers
            var_name='Idoszak',  # Column name for time periods
            value_name='Atlagkereset'  # Column name for earnings values
        )
        return data_long
    except KeyError:
        print("Error: Columns 'Területi egység neve' or 'szintje' is not found.")
        return None

def clean_earnings_data(data):
    # Clean and prepare earnings data for analysis
    data = data.copy()  # Avoid pandas SettingWithCopyWarning
    
    # Clean earnings values: remove spaces (thousands separators) and handle missing data
    data['Atlagkereset'] = data['Atlagkereset'].replace(' ', '', regex=True)
    data['Atlagkereset'] = data['Atlagkereset'].replace('...', np.nan, regex=False)
    data = data.dropna(subset=['Atlagkereset'])
    data['Atlagkereset'] = pd.to_numeric(data['Atlagkereset'])
    
    # Extract year from time period string (e.g., "2020. I–IV. negyedév" -> 2020)
    data['Ev'] = data['Idoszak'].str.split('.').str[0].astype(int)
    
    return data

def process_national_data(data_long):
    # Extract and clean national level data for country-wide analysis
    data_orszagos = data_long[data_long['Területi egység neve'] == 'Ország összesen'].copy()
    data_eves = data_orszagos[data_orszagos['Idoszak'].str.contains('I–IV. negyedév')].copy()
    
    if DEBUG:
        print("data_eves before cleaning:\n", data_eves.head())
    
    data_eves = clean_earnings_data(data_eves)
    data_final = data_eves[['Ev', 'Atlagkereset']].sort_values(by='Ev').reset_index(drop=True)
    
    print("--- Cleaned, annual national data ---")
    print(data_final)
    
    if data_final.empty:
        print("Error: The cleaned DataFrame is empty. Check the data and the filtering conditions.")
        exit()
    
    return data_final