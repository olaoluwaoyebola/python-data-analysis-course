# Colab Helper Functions
# This file contains helper functions for working with Google Colab

def load_github_data(file_path):
    """
    Load data directly from GitHub repository
    
    Parameters:
    -----------
    file_path : str
        Path to the file in the repository (e.g., 'Resources/data/sample_customers.csv')
    
    Returns:
    --------
    pandas.DataFrame or str
        Loaded data, as DataFrame for CSV files or string for text files
    """
    import pandas as pd
    import requests
    from io import StringIO
    
    base_url = 'https://raw.githubusercontent.com/autom8or-com/python-data-analysis-course/main/'
    full_url = base_url + file_path
    
    response = requests.get(full_url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    if file_path.endswith('.csv'):
        return pd.read_csv(StringIO(response.text))
    else:
        return response.text

def setup_colab():
    """
    Set up Colab environment with common imports and display settings
    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # Display settings
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.precision', 2)
    
    # Plot settings
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set(font_scale=1.2)
    
    # Return common packages for use
    return pd, np, plt, sns

def save_work():
    """
    Remind students how to save their work
    """
    print("Remember to save your work!")
    print("Go to File > Save a copy in Drive to keep your own copy of this notebook.")
    print("You can also download the notebook using File > Download > .ipynb")