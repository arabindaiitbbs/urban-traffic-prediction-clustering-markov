# src/preprocessing/preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_and_encode_data(file_path):
    """Load and encode categorical data from an Excel file."""
    try:
        data = pd.read_excel(file_path)
        label_encoder = LabelEncoder()
        for column in ['Location', 'Speed Range (Km/hr)', 'Time Interval']:
            data[column] = label_encoder.fit_transform(data[column])
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except Exception as e:
        logging.error(f"Error loading or encoding data: {e}")
        return None

def prepare_data(data, features):
    """Prepare data using imputation and scaling."""
    imputer = SimpleImputer(strategy='mean')
    scaler = StandardScaler()
    try:
        data = imputer.fit_transform(data[features])
        data = scaler.fit_transform(data)
        return data
    except Exception as e:
        logging.error(f"Error preparing data: {e}")
        return None
