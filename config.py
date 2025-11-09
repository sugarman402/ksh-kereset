# Configuration settings for KSH earnings analysis

# File paths and directories
INPUT_FILE = 'stadat-mun0206-20.2.2.9-hu.xlsx'
DIAGRAMS_DIR = 'diagrams'

# Debug mode - set to True for additional diagnostic output
DEBUG = False

# Data processing parameters
MAX_ROWS = 30  # Keep only first 30 rows (exclude percentile data)
REQUIRED_COLUMNS = ['Területi egység neve', 'Területi egység szintje']

# Chart configuration
FIGURE_SIZE = (10, 6)
POINT_SIZE = 50
LINE_WIDTH = 2
GRID_ALPHA = 0.6

# Regression analysis thresholds
HIGH_R_SQUARED = 0.9
GOOD_R_SQUARED = 0.7