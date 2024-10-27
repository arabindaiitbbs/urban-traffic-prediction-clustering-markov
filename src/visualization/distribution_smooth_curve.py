# src/visualization/distribution_smooth_curve.py
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

# Adjust import path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.data.data_manager import DataManager  # After adjusting sys.path

def plot_smooth_distributions(states, morning_distribution, afternoon_distribution, title, filename):
    """
    Plot smooth distributions for morning and afternoon stationary data.

    Args:
        states (list): List of states.
        morning_distribution (list or np.ndarray): Morning distribution data.
        afternoon_distribution (list or np.ndarray): Afternoon distribution data.
        title (str): Title for the plot.
        filename (str): Name of the file to save the plot.
    """
    # Normalize distributions to proportions
    morning_distribution = np.array(morning_distribution) / 100
    afternoon_distribution = np.array(afternoon_distribution) / 100

    # State indices for interpolation
    state_indices = np.arange(len(states))

    # Create smooth curves for both distributions
    morning_interpolator = PchipInterpolator(state_indices, morning_distribution)
    afternoon_interpolator = PchipInterpolator(state_indices, afternoon_distribution)

    morning_smooth = np.linspace(state_indices.min(), state_indices.max(), 500)
    morning_smooth_distribution = morning_interpolator(morning_smooth)

    afternoon_smooth = np.linspace(state_indices.min(), state_indices.max(), 500)
    afternoon_smooth_distribution = afternoon_interpolator(afternoon_smooth)

    # Plot
    plt.figure(figsize=(6, 6))
    plt.plot(morning_smooth, morning_smooth_distribution, label='Morning', color='red')
    plt.plot(afternoon_smooth, afternoon_smooth_distribution, label='Afternoon', color='blue')
    plt.xticks(state_indices, states)
    plt.xlabel('States', fontsize=20)
    plt.ylabel('Distribution', fontsize=20)
    plt.ylim(0, 0.9)
    plt.legend(fontsize=18)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()

def main():
    # Initialize DataManager and load config for distributions
    data_manager = DataManager()
    states = ['A', 'B', 'C', 'D', 'E']
    
    # Example morning and afternoon distributions (in percentages) for testing
    morning_distribution = [0.00, 4.55, 63.64, 29.55, 2.27]
    afternoon_distribution = [10.53, 84.21, 5.26, 0.0, 0.0]

    plot_smooth_distributions(
        states,
        morning_distribution,
        afternoon_distribution,
        title="Stationary Distributions for L1",
        filename="L1_distribution.png"
    )

if __name__ == "__main__":
    main()
