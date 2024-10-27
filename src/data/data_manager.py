# src/data/data_manager.py

import os
import yaml
import pandas as pd

class DataManager:
    def __init__(self, config_path="config.yaml"):
        """Initialize DataManager with configuration settings from the YAML config file."""
        self.config = self.load_config(config_path)
        
    def load_config(self, config_path):
        """Loads configuration settings from the YAML config file."""
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def get_data_paths(self):
        """Returns paths for morning and afternoon data files from the configuration file."""
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, 'data', 'processed')
        
        # Retrieve paths from config or set default
        morning_path = self.config["data_paths"].get("morning_data", os.path.join(data_dir, "Morning_Combined.xlsx"))
        afternoon_path = self.config["data_paths"].get("afternoon_data", os.path.join(data_dir, "Afternoon_Combined.xlsx"))
        
        return morning_path, afternoon_path

    def load_data(self, file_path):
        """Loads and returns data from a specified Excel file path."""
        try:
            data = pd.read_excel(file_path)
            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None

    def get_features(self):
        """Returns feature sets for clustering and Markov analysis."""
        clustering_features = self.config["features"].get("clustering", [])
        markov_features = self.config["features"].get("markov", [])
        return clustering_features, markov_features
