# Local Python Setup Guide

## Overview
While Google Colab is the primary platform for this course, you may want to set up a local Python environment for offline work or more advanced projects.

## Installing Python

1. **Download Anaconda**
   - Go to [anaconda.com/download](https://www.anaconda.com/download)
   - Download the appropriate installer for your operating system
   - Follow the installation instructions

2. **Create a Virtual Environment**
   ```bash
   # Create a new environment for the course
   conda create -n pydata python=3.9
   
   # Activate the environment
   conda activate pydata
   ```

3. **Install Required Packages**
   ```bash
   # Install core data science packages
   conda install numpy pandas matplotlib seaborn scikit-learn jupyter
   
   # Install additional packages
   conda install plotly bokeh statsmodels
   ```

## Setting Up Jupyter Notebook

1. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Configure Jupyter Environment**
   - Create a folder for your course materials
   - Navigate to this folder in Jupyter
   - Create new notebooks as needed

## Working with Course Files

1. **Clone the Course Repository**
   ```bash
   git clone https://github.com/autom8or-com/python-data-analysis-course.git
   cd python-data-analysis-course
   ```

2. **Download the Olist Dataset**
   - Go to [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
   - Download the dataset files
   - Place them in the `Data` folder of your local repository

## Recommended IDE Options

If you prefer using an Integrated Development Environment (IDE) instead of Jupyter Notebook:

1. **VS Code**
   - Download from [code.visualstudio.com](https://code.visualstudio.com/)
   - Install the Python extension
   - Open a course notebook to work with it directly in VS Code

2. **PyCharm**
   - Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
   - Community Edition is free and sufficient for this course
   - Configure with your conda environment