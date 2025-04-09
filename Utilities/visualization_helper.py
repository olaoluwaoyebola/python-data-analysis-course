# Visualization Helper Functions
# This file contains helper functions for creating visualizations

def set_plotting_style():
    """
    Set consistent plotting style for the course
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set(font_scale=1.2)
    sns.set_palette('viridis')
    
    # Font settings
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial']
    
    # Grid settings
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.linestyle'] = '--'
    
    # Figure size
    plt.rcParams['figure.figsize'] = [12, 8]
    
    return plt, sns

def plot_numeric_distribution(df, column, bins=30, kde=True):
    """
    Plot the distribution of a numeric column
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing the data
    column : str
        Name of the column to plot
    bins : int, default=30
        Number of bins in the histogram
    kde : bool, default=True
        Whether to plot the kernel density estimate
    """
    plt, sns = set_plotting_style()
    
    plt.figure(figsize=(12, 6))
    ax = sns.histplot(df[column].dropna(), bins=bins, kde=kde)
    
    # Add title and labels
    plt.title(f'Distribution of {column}', fontsize=16)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    # Add summary statistics as text
    stats_text = (
        f"Mean: {df[column].mean():.2f}\n"
        f"Median: {df[column].median():.2f}\n"
        f"Std Dev: {df[column].std():.2f}\n"
        f"Min: {df[column].min():.2f}\n"
        f"Max: {df[column].max():.2f}"
    )
    plt.annotate(stats_text, xy=(0.95, 0.95), xycoords='axes fraction',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
                 ha='right', va='top', fontsize=12)
    
    plt.tight_layout()
    plt.show()

def plot_categorical_distribution(df, column, top_n=None, sort_by_value=True):
    """
    Plot the distribution of a categorical column
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing the data
    column : str
        Name of the column to plot
    top_n : int, optional
        If provided, show only the top N categories
    sort_by_value : bool, default=True
        Whether to sort bars by frequency (True) or by category name (False)
    """
    plt, sns = set_plotting_style()
    
    # Count values and convert to DataFrame for easier manipulation
    value_counts = df[column].value_counts()
    
    if top_n is not None and top_n < len(value_counts):
        if sort_by_value:
            # Get the top N most frequent categories
            data = value_counts.head(top_n)
        else:
            # Get the top N most frequent categories, then sort alphabetically
            data = value_counts.head(top_n).sort_index()
    else:
        if sort_by_value:
            data = value_counts
        else:
            data = value_counts.sort_index()
    
    plt.figure(figsize=(12, 8))
    
    # Create the bar plot
    ax = sns.barplot(x=data.index, y=data.values)
    
    # Add title and labels
    plt.title(f'Distribution of {column}' + 
              (f' (Top {top_n})' if top_n is not None and top_n < len(value_counts) else ''), 
              fontsize=16)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Count', fontsize=12)
    
    # Rotate x-axis labels if there are many categories
    if len(data) > 10 or data.index.str.len().max() > 10:
        plt.xticks(rotation=45, ha='right')
    
    # Add count on top of each bar
    for i, v in enumerate(data.values):
        ax.text(i, v + 0.1, str(v), ha='center')
    
    plt.tight_layout()
    plt.show()

def plot_time_series(df, date_column, value_column, freq='M', agg_func='mean'):
    """
    Plot a time series with resampling
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing the data
    date_column : str
        Name of the date column
    value_column : str
        Name of the value column to plot
    freq : str, default='M'
        Frequency for resampling ('D' for daily, 'W' for weekly, 'M' for monthly, etc.)
    agg_func : str, default='mean'
        Aggregation function for resampling ('mean', 'sum', 'count', etc.)
    """
    import pandas as pd
    plt, sns = set_plotting_style()
    
    # Make sure the date column is in datetime format
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column])
    
    # Set the date as index for resampling
    df_ts = df.set_index(date_column)[[value_column]]
    
    # Resample the data
    if agg_func == 'mean':
        resampled = df_ts.resample(freq).mean()
    elif agg_func == 'sum':
        resampled = df_ts.resample(freq).sum()
    elif agg_func == 'count':
        resampled = df_ts.resample(freq).count()
    else:
        raise ValueError(f"Unsupported aggregation function: {agg_func}")
    
    plt.figure(figsize=(14, 7))
    
    # Plot the time series
    ax = sns.lineplot(x=resampled.index, y=value_column, data=resampled, marker='o')
    
    # Add title and labels
    freq_map = {'D': 'Daily', 'W': 'Weekly', 'M': 'Monthly', 'Q': 'Quarterly', 'Y': 'Yearly'}
    freq_label = freq_map.get(freq, freq)
    plt.title(f'{freq_label} {agg_func.title()} of {value_column}', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel(f'{agg_func.title()} {value_column}', fontsize=12)
    
    # Format the y-axis to include commas for thousands
    import matplotlib.ticker as ticker
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.show()