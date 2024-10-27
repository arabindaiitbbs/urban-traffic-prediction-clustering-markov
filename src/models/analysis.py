import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import logging
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from src.data.data_manager import DataManager
from src.preprocessing.preprocessing import load_and_encode_data, prepare_data
from src.visualization.visualization import plot_clusters, plot_transition_matrix, plot_stationary_distribution

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Clustering Analysis
def perform_clustering_analysis(file_path, features, n_clusters):
    """Loads, preprocesses data, and performs PCA and KMeans clustering."""
    logging.info(f"Loading and preparing data for clustering from {file_path}")
    data = load_and_encode_data(file_path)
    if data is None:
        return None, None, None

    prepared_data = prepare_data(data, features)
    if prepared_data is None:
        return None, None, None

    # Perform PCA
    pca = PCA(n_components=2)
    data_pca = pca.fit_transform(prepared_data)
    logging.info(f"PCA Variance Ratio: {pca.explained_variance_ratio_}")

    # Perform KMeans Clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    clusters = kmeans.fit_predict(data_pca)
    logging.info(f"Cluster centers: {kmeans.cluster_centers_}")
    return data_pca, clusters, kmeans

# Markov Chain Analysis
def calculate_transition_matrix(data):
    """Calculate transition matrix for LOS states."""
    states = sorted(data['LOS'].unique())
    transition_matrix = np.zeros((len(states), len(states)), dtype=float)
    for state, next_state in zip(data['LOS'], data['LOS'][1:]):
        i, j = states.index(state), states.index(next_state)
        transition_matrix[i][j] += 1
    transition_matrix /= transition_matrix.sum(axis=1, keepdims=True)
    return transition_matrix, states

def calculate_stationary_distribution(transition_matrix):
    """Calculate stationary distribution for the transition matrix."""
    eigvals, eigvecs = np.linalg.eig(transition_matrix.T)
    stationary = np.real(eigvecs[:, np.argmax(np.abs(eigvals - 1) < 1e-8)])
    return stationary / stationary.sum()

# Running Analysis for Morning and Afternoon Sessions
def main_analysis():
    data_manager = DataManager(config_path="C:/Users/arabi/OneDrive/Desktop/New folder/Objective 1/ICPR-2024/urban-traffic-project/config.yaml")
    features_clustering, features_markov = data_manager.get_features()
    morning_path, afternoon_path = data_manager.get_data_paths()

    # Define optimal clusters for each session
    cluster_settings = {'Morning': 4, 'Afternoon': 2}

    for session, path in zip(['Morning', 'Afternoon'], [morning_path, afternoon_path]):
        logging.info(f"Starting clustering analysis for {session} session.")
        data_pca, clusters, kmeans = perform_clustering_analysis(path, features_clustering, n_clusters=4 if session == "Morning" else 2)
        if data_pca is not None:
            plot_clusters(data_pca, clusters, kmeans, title=f"{session} Clustering", filename=f"{session.lower()}_clustering.png", session=session)
        
        logging.info(f"Starting Markov analysis for {session} session.")
        data = load_and_encode_data(path)
        if data is not None:
            transition_matrix, states = calculate_transition_matrix(data)
            stationary_distribution = calculate_stationary_distribution(transition_matrix)
            logging.info(f"{session} Transition Matrix:\n{transition_matrix}")
            logging.info(f"{session} Stationary Distribution:\n{stationary_distribution}")

            # Plotting Transition Matrix and Stationary Distribution
            plot_transition_matrix(transition_matrix, states, title=f"{session} Transition Matrix", filename=f"{session.lower()}_transition_matrix.png")
            plot_stationary_distribution(stationary_distribution, states, title=f"{session} Stationary Distribution", filename=f"{session.lower()}_stationary_distribution.png")

if __name__ == "__main__":
    main_analysis()




