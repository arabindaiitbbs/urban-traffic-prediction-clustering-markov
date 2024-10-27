# import matplotlib.pyplot as plt
# import numpy as np
# import logging
# import seaborn as sns

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def plot_clusters(data_pca, clusters, kmeans, title, filename, session):
#     """Plot clusters with custom labels for morning and afternoon sessions."""
#     plt.figure(figsize=(10, 8))
#     unique_clusters = np.unique(clusters)
    
#     # Define labels and colors based on the session
#     labels = [f"MC{i}" for i in unique_clusters] if session == "Morning" else [f"AC{i}" for i in unique_clusters]
#     colors = ['#FF5733', '#33D7FF', '#D433FF', '#33FF57'] if session == "Morning" else ['#FFD700', '#00BFFF']
    
#     for i, cluster in enumerate(unique_clusters):
#         cluster_data = data_pca[clusters == cluster]
#         plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=labels[i], color=colors[i % len(colors)], alpha=0.7, edgecolor='k')
    
#     # Plot centroids
#     for i, center in enumerate(kmeans.cluster_centers_):
#         plt.scatter(center[0], center[1], marker='x', s=100, color='black', edgecolor='k')

#     plt.xlabel('PC1 (Principal Component 1)', fontsize=18)
#     plt.ylabel('PC2 (Principal Component 2)', fontsize=18)
#     plt.title(title)
#     plt.legend(title='Cluster Label', title_fontsize='16', fontsize=14)
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig(filename, dpi=300)
#     plt.show()

# def plot_transition_matrix(transition_matrix, states, title="Transition Matrix", filename="transition_matrix.png"):
#     """
#     Plots the transition matrix with annotations for each cell value.
    
#     Parameters:
#         transition_matrix (np.ndarray): The transition matrix.
#         states (list): List of state names.
#         title (str): Title for the plot.
#         filename (str): Filename for saving the plot.
#     """
#     plt.figure(figsize=(8, 6))
#     sns.heatmap(
#         transition_matrix,
#         annot=True,              # Enables cell annotations
#         fmt=".2f",               # Format to show values with two decimal places
#         cmap="Blues",            # Color map for better visibility
#         xticklabels=states,
#         yticklabels=states,
#         cbar_kws={'label': 'Transition Probability'}
#     )
#     plt.title(title, fontsize=16)
#     plt.xlabel("Next State", fontsize=14)
#     plt.ylabel("Current State", fontsize=14)
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.savefig(filename, dpi=300)
#     plt.show()

# def plot_stationary_distribution(stationary_distribution, states, title, filename):
#     """Plot the stationary distribution with unique colors for each state."""
#     plt.figure(figsize=(8, 6))
#     colors = plt.cm.viridis(np.linspace(0, 1, len(states)))  # Unique color for each state
#     plt.bar(states, stationary_distribution, color=colors, alpha=0.7, edgecolor='k')
#     plt.xlabel('States', fontsize=16)
#     plt.ylabel('Probability', fontsize=16)
#     plt.title(title)
#     plt.tight_layout()
#     plt.savefig(filename, dpi=300)
#     plt.show()


# src/visualization/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

# Plotting Clusters
def plot_clusters(data_pca, clusters, kmeans, title, filename, session):
    """Plots KMeans clusters with cluster centers."""
    plt.figure(figsize=(10, 8))
    cluster_labels = [f"{session[0]}C{i}" for i in range(kmeans.n_clusters)]
    for i, label in enumerate(cluster_labels):
        plt.scatter(data_pca[clusters == i, 0], data_pca[clusters == i, 1], label=label, alpha=0.6)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='black', marker='X', s=100)
    plt.title(title)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.savefig(filename, dpi=300)
    plt.show()

# Plotting Transition Matrix
def plot_transition_matrix(transition_matrix, states, title, filename):
    """Plots the transition matrix as a heatmap."""
    plt.figure(figsize=(8, 6))
    sns.heatmap(transition_matrix, annot=True, fmt=".2f", cmap="Blues", xticklabels=states, yticklabels=states)
    plt.title(title)
    plt.xlabel('To State')
    plt.ylabel('From State')
    plt.savefig(filename, dpi=300)
    plt.show()

# Plotting Stationary Distribution
def plot_stationary_distribution(stationary_distribution, states, title, filename):
    """Plots stationary distribution as a bar chart."""
    plt.figure(figsize=(8, 6))
    colors = sns.color_palette("Set3", len(states))
    plt.bar(states, stationary_distribution, color=colors)
    plt.title(title)
    plt.xlabel('State')
    plt.ylabel('Probability')
    plt.savefig(filename, dpi=300)
    plt.show()

# Plotting Weibull Distribution
def plot_weibull_distribution(x, pdf, title, filename):
    """Plots Weibull PDF for a given location and session."""
    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf, label='Weibull PDF', color='purple', linewidth=2)
    plt.xlabel('Level of Service Calculation')
    plt.ylabel('Probability Density')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()
