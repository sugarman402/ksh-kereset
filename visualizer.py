# Visualization and plotting functions

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import os
from config import FIGURE_SIZE, POINT_SIZE, LINE_WIDTH, GRID_ALPHA, DEBUG
from data_processor import clean_earnings_data
from utils import clean_text_for_filename

def create_county_diagram(county_data, county_name, county_type, diagrams_dir):
    # Create and save diagram for a specific county
    plt.figure(figsize=FIGURE_SIZE)
    plt.plot(county_data['Ev'], county_data['Atlagkereset'], 
             marker='o', linestyle='-', label=county_name)
    
    plt.title(f'Bruttó Átlagkereset Alakulása ({county_name})')
    plt.xlabel('Év')
    plt.ylabel('Bruttó Átlagkereset (Ft)')
    plt.grid(True, linestyle='--', alpha=GRID_ALPHA)
    plt.legend()
    
    # Save with county name and type in filename
    filename = f'diagram_{county_name}_{county_type}.png'
    plt.savefig(os.path.join(diagrams_dir, filename))
    print(f"Diagram saved to: {os.path.join(diagrams_dir, filename)}")
    plt.close()  # Free memory

def process_county_data(data_long, diagrams_dir):
    # Process and create diagrams for all counties in the dataset
    print("\nCreating diagrams by county...")
    counties = data_long['Területi egység neve'].unique()
    
    for county in counties:
        # Filter for current county and annual data only (I–IV. negyedév = full year)
        county_data = data_long[(data_long['Területi egység neve'] == county) &
                                (data_long['Idoszak'].str.contains('I–IV. negyedév'))].copy()
        
        if DEBUG:
            print(f"{county} county_data before cleaning:\n", county_data.head())
        
        county_data = clean_earnings_data(county_data)
        
        # Extract and clean county type for filename
        county_type = county_data['Területi egység szintje'].iloc[0] if not county_data.empty else 'Unknown'
        county_type_clean = clean_text_for_filename(county_type)
        
        create_county_diagram(county_data, county, county_type_clean, diagrams_dir)

def create_line_chart(data_final, diagrams_dir):
    # Create time series line chart showing national earnings trend
    plt.figure(figsize=FIGURE_SIZE)
    plt.plot(data_final['Ev'], data_final['Atlagkereset'], 
             marker='o', linestyle='-', color='blue')
    
    plt.title('Bruttó Átlagkereset Alakulása (Országos, Éves Adatok)')
    plt.xlabel('Év')
    plt.ylabel('Bruttó Átlagkereset (Ft)')
    plt.grid(True, linestyle='--', alpha=GRID_ALPHA)
    
    # Format y-axis with currency formatting and integer years on x-axis
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(mtick.FuncFormatter(lambda x, p: f"{x:,.0f} Ft"))
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    
    filename = 'vonaldiagram_eves_kereset.png'
    plt.savefig(os.path.join(diagrams_dir, filename))
    print(f"Line chart saved: {os.path.join(diagrams_dir, filename)}")
    plt.close()

def create_regression_plot(data_final, diagrams_dir):
    # Create scatter plot with regression line to visualize trend
    plt.figure(figsize=FIGURE_SIZE)
    
    # Use seaborn for automatic regression line calculation
    sns.regplot(x='Ev', y='Atlagkereset', data=data_final,
                scatter_kws={'s': POINT_SIZE},  # Point size
                line_kws={'color': 'red', 'lw': LINE_WIDTH})  # Red line, width 2
    
    plt.title('Bruttó Átlagkereset Trendje (Lineáris Regresszió)')
    plt.xlabel('Év')
    plt.ylabel('Bruttó Átlagkereset (Ft)')
    plt.grid(True, linestyle='--', alpha=GRID_ALPHA)
    
    # Format axes
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(mtick.FuncFormatter(lambda x, p: f"{x:,.0f} Ft"))
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    
    filename = 'pontdiagram_regresszio_trend.png'
    plt.savefig(os.path.join(diagrams_dir, filename))
    print(f"Regression scatter plot saved: {os.path.join(diagrams_dir, filename)}")
    plt.close()