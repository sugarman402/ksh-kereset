# Statistical analysis and regression functions

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from config import HIGH_R_SQUARED, GOOD_R_SQUARED

def perform_regression_analysis(data_final):
    # Perform linear regression analysis to determine earnings trend
    X_data = data_final[['Ev']]  # Independent variable (years) - must be 2D
    y_data = data_final['Atlagkereset']  # Dependent variable (earnings)
    
    if X_data.empty or y_data.empty:
        print("Error: X_data or y_data is empty. Regression cannot be performed.")
        exit()
    
    # Fit linear regression model and calculate metrics
    model = LinearRegression()
    model.fit(X_data, y_data)
    y_pred = model.predict(X_data)
    
    slope = model.coef_[0]  # Rate of change (HUF per year)
    intercept = model.intercept_  # Y-intercept
    r_squared = r2_score(y_data, y_pred)  # Model fit quality (0-1)
    
    return model, slope, intercept, r_squared

def print_regression_results(slope, intercept, r_squared):
    # Display regression analysis results with statistical interpretation
    
    print("\n--- Linear Regression Results (Trend) ---")
    
    # Show the mathematical equation of the fitted line
    print(f"Model equation: Average Earnings = {intercept:,.2f} + {slope:,.2f} * Year")
    
    # Display R-squared value (coefficient of determination) 
    print(f"R-squared value: {r_squared:.4f}")
    
    # Interpret R-squared value for user understanding
    if r_squared > HIGH_R_SQUARED:
        print("The R-squared value is very high. This means that the average earnings growth in this short period followed an almost perfectly linear trend.")
    elif r_squared > GOOD_R_SQUARED:
        print("The R-squared value is strong. Time explains well the earnings growth.")
    else:
        print("The R-squared value is moderate or weak. The earnings change was not clearly linear.")

def print_descriptive_statistics(data_final):
    # Display descriptive statistics for national earnings
    print("--- Descriptive Statistics (National Annual Average Earnings) ---")
    print(data_final['Atlagkereset'].describe().apply(lambda x: f"{x:,.0f} Ft"))  # Currency formatting