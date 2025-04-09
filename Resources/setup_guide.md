# Google Colab Setup Guide

## Getting Started with Google Colab

1. **Access Google Colab**
   - Go to [colab.research.google.com](https://colab.research.google.com/)
   - Sign in with your Google account

2. **Opening Course Notebooks**
   - Click on 'File' > 'Open notebook'
   - Select the 'GitHub' tab
   - Enter the repository URL: https://github.com/autom8or-com/python-data-analysis-course
   - Choose the notebook you want to open

3. **Saving Your Work**
   - Click 'File' > 'Save a copy in Drive' to save to your Google Drive
   - All your work should be done in your own copies of the notebooks

## Working with Data Files

1. **Accessing Sample Data**
   - Sample data files are available in the Resources/data folder
   - Use the following code to load data directly from GitHub:

```python
import pandas as pd

# Load directly from GitHub
url = 'https://raw.githubusercontent.com/autom8or-com/python-data-analysis-course/main/Resources/data/sample_customers.csv'
df = pd.read_csv(url)
```

2. **Working with the Full Olist Dataset**
   - The full dataset needs to be uploaded to your Google Colab session
   - Download the dataset from Kaggle and upload using the code below:

```python
from google.colab import files
uploaded = files.upload()  # This will open a file picker dialog

# Read the uploaded file
import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['filename.csv']))
```

## Submitting Assignments

1. Download your completed notebook: 'File' > 'Download .ipynb'
2. Rename according to the assignment guidelines
3. Submit through the course portal