
#%%
import os
import sys

PROJECT_NAME = 'sales-forecasting'

try:

    from google.colab import drive
    drive.mount('/content/drive')

    PROJECT_ROOT = f'/content/drive/My Drive/Data Science/Personal/{PROJECT_NAME}'

    print("Running in Google Colab.")

except:

    PROJECT_ROOT = rf'D:/Data-Science/Projects/Personal/{PROJECT_NAME}'

    print("Running in local environment.")

# Move to project root
os.chdir(PROJECT_ROOT)

print("Current working directory:", os.getcwd())

# Add project root to Python path
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

#%%

import pandas as pd

class DataLoader:
    """
    This is responsible to read the raw data file and load it into memory as a Panda DataFrame
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.dataFrame = None

    def load_data(self):
        self.dataFrame = pd.read_csv(self.file_path)
        return self.dataFrame

print(pd.__version__)

