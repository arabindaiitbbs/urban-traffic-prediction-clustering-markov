
# Urban Traffic Prediction and Clustering with Markov Models
This project focuses on analyzing urban traffic patterns using clustering, Markov models, and Weibull distribution. The data, preprocessed from video footage, is used to predict congestion levels and traffic patterns.





## Table of Contents
1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Data Processing & Analysis](#data-processing--analysis)
6. [Visualization](#visualization)
7. [Results](#results)
8. [Contributing](#contributing)
9. [License](#license)

## Project Structure
```plaintext
urban-traffic-prediction-clustering-markov/
├── data/                    
│   └── processed/           # Contains preprocessed traffic data (Excel files)
├── src/
│   ├── data/
│   │   └── data_manager.py  # Manages loading of data paths and configuration
│   ├── preprocessing/
│   │   └── preprocessing.py # Preprocessing functions like encoding and scaling
│   ├── models/
│   │   └── analysis.py      # Main analysis script for clustering and Markov chain calculations
│   ├── visualization/
│   │   ├── visualization.py # Clustering, transition matrix, stationary distribution plotting
│   │   ├── weibull_distribution.py # Weibull distribution visualization
│   │   └── distribution_smooth_curve.py # Smooth distribution plotting for states
├── config.yaml              # Configuration file for data paths and features
└── README.md                # Project documentation

## Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```
## Installation
git clone https://github.com/arabindaiitbbs/urban-traffic-prediction-clustering-markov.git
cd urban-traffic-prediction-clustering-markov


## Installation

install the requirements from the requirements.txt file

```bash
  pip install -r requirements.txt

```
    

    
## Configuration
Update the config.yaml file with paths to the data files and any specific feature columns to include in your analysis.
## Run Clustering and Markov Analysis
python src/models/analysis.py

## Generate Weibull Distribution Visualizations
python src/visualization/weibull_distribution.py

## Smooth Distribution Curve Visualization
python src/visualization/distribution_smooth_curve.py

## Data Processing & Analysis
1. DataManager (data_manager.py): Loads data paths and configuration settings from config.yaml.
2. Preprocessing (preprocessing.py): Prepares the data, including encoding, scaling, and imputing missing values.
3. Clustering and Markov Chain Analysis (analysis.py): Performs clustering analysis using PCA and KMeans and Generates transition matrices and stationary distributions based on LOS data for Markov chain analysis.
## Visualization
1. plot_clusters: Visualizes clustered PCA data.
2. plot_transition_matrix: Generates a heatmap of the Markov transition matrix.
3. plot_stationary_distribution: Bar plot of stationary distributions.
4. weibull_distribution.py: Weibull distribution analysis for different locations in morning and afternoon sessions.
5. distribution_smooth_curve.py: Smooth curve plotting for morning and afternoon stationary distributions.
## Results
1. Clustering Plots: Generated for both morning and afternoon sessions, showing optimal clusters for each.
2. Transition Matrices: Heatmaps representing state transitions for each session.
3. Stationary Distributions: Bar plots visualizing the stable traffic distribution across different states.
4. Weibull Distributions: PDFs showing the probability density across time intervals for each location.
5. Smooth Distribution Curves: Continuous smooth curves for stationary distributions, facilitating comparisons.

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## License

[MIT](https://choosealicense.com/licenses/mit/)

