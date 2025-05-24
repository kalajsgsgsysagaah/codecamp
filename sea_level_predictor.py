import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, s=20)

    # Create first line of best fit using all data
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate years from start of data to 2050 for first line
    years_extended = np.arange(df['Year'].min(), 2051)
    line_all = slope_all * years_extended + intercept_all
    ax.plot(years_extended, line_all, 'r-', label='Line of best fit (1880-2050)')

    # Create second line of best fit using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Generate years from 2000 to 2050 for second line
    years_recent = np.arange(2000, 2051)
    line_recent = slope_recent * years_recent + intercept_recent
    ax.plot(years_recent, line_recent, 'g-', label='Line of best fit (2000-2050)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Adjust layout for better appearance
    plt.tight_layout()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
