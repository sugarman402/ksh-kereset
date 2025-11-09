# Main execution script for KSH earnings analysis

from config import INPUT_FILE, DIAGRAMS_DIR, DEBUG
from utils import setup_output_directory, print_program_info
from data_processor import load_and_preprocess_data, transform_data_to_long_format, process_national_data
from visualizer import process_county_data, create_line_chart, create_regression_plot
from analyzer import perform_regression_analysis, print_regression_results, print_descriptive_statistics

def main():
    # Main function to orchestrate the complete earnings analysis workflow
    
    # Display program information
    print_program_info()
    
    if DEBUG:
        print("Debug mode is ON")
        print("Reading data from:", INPUT_FILE)
    
    # Setup output directory and clear existing files
    setup_output_directory(DIAGRAMS_DIR)
    
    # STEP 1: Load and validate raw data from Excel file
    data_raw = load_and_preprocess_data(INPUT_FILE)
    
    # STEP 2: Transform data structure from wide to long format
    data_long = transform_data_to_long_format(data_raw)
    if data_long is None:
        print("The melt process is not finished. The data could not be processed.")
        exit()
    
    # STEP 3: Generate individual charts for each county/region
    process_county_data(data_long, DIAGRAMS_DIR)
    
    # STEP 4: Extract and clean national-level data
    data_final = process_national_data(data_long)
    
    # STEP 5: Display descriptive statistics for national earnings
    print_descriptive_statistics(data_final)
    
    # STEP 6: Create national earnings trend visualization
    create_line_chart(data_final, DIAGRAMS_DIR)
    
    # STEP 7: Perform regression analysis to quantify trend
    model, slope, intercept, r_squared = perform_regression_analysis(data_final)
    create_regression_plot(data_final, DIAGRAMS_DIR)  # Create scatter plot with regression line
    print_regression_results(slope, intercept, r_squared)  # Display regression results
    
    print("\nAnalysis completed.")

# Execute main function only when script is run directly (not imported)
if __name__ == "__main__":
    main()  # Start the analysis workflow