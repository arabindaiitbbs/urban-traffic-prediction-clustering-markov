# src/models/weibull_distribution.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
from src.data.data_manager import DataManager

def load_data(filepath):
    """ Load data from an Excel file. """
    return pd.read_excel(filepath)

def filter_data_by_location_and_interval(data, location, time_intervals):
    """ Filter data for a specific location and time intervals. """
    return data[(data['Location'] == location) & (data['Time Interval'].isin(time_intervals))]

def fit_weibull_distribution(data):
    """ Fit the Weibull distribution to data and return the PDF x and y values. """
    shape, loc, scale = weibull_min.fit(data)
    x = np.linspace(0, max(data), 1000)
    pdf = weibull_min.pdf(x, shape, loc, scale)
    return x, pdf

def plot_distribution(x, pdf, label, linestyle, linewidth):
    """ Plot the Weibull PDF for given data. """
    plt.plot(x, pdf, label=label, linestyle=linestyle, linewidth=linewidth)

def process_and_plot(filepath, session_label, time_intervals, locations, line_styles, line_thickness):
    """ Process data and plot the Weibull distribution for each location. """
    df = load_data(filepath)
    plt.figure(figsize=(12, 8))

    for i, location in enumerate(locations):
        df_filtered = filter_data_by_location_and_interval(df, location, time_intervals)
        level_of_service = np.concatenate([
            df_filtered[df_filtered['Time Interval'] == interval]['Level of Service Calculation'].values
            for interval in time_intervals
        ])
        if len(level_of_service) > 0:
            x, pdf = fit_weibull_distribution(level_of_service)
            plot_distribution(x, pdf, f'{location} - {session_label} Weibull Distribution', line_styles[i], line_thickness[i])
        else:
            print(f"No data available for {location} during {session_label} in specified intervals.")

    plt.xlabel('Level of Service Calculation', fontsize=22)
    plt.ylabel('Probability Density', fontsize=22)
    plt.legend(fontsize=22)
    plt.grid(True)
    plt.tick_params(axis='y', labelsize=18)
    plt.tick_params(axis='x', labelsize=18)
    plt.tight_layout()
    plt.savefig(f'{session_label.lower()}_weibull_density_plots.png', dpi=300)  # Save the plot as PNG with higher resolution
    plt.show()

def main():
    data_manager = DataManager()
    morning_path, afternoon_path = data_manager.get_data_paths()
    
    time_intervals = {
        "morning": ['9.00-9.15', '9.15-9.30', '9.30-9.45', '9.45-10.00', '10.00-10.15', '10.15-10.30', '10.30-10.45', '10.45-11.00'],
        "afternoon": ['1.00-1.15', '1.15-1.30', '1.30-1.45', '1.45-2.00']
    }
    locations = ['L1', 'L2', 'L3']
    line_styles = ['-', '--', ':']
    line_thickness = [2, 2, 2]

    # Process and plot for morning and afternoon
    process_and_plot(morning_path, 'Morning', time_intervals['morning'], locations, line_styles, line_thickness)
    process_and_plot(afternoon_path, 'Afternoon', time_intervals['afternoon'], locations, line_styles, line_thickness)

if __name__ == "__main__":
    main()
