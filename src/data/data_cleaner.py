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

class DataCleaner:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def check_missing(self):
        missing_values = self.dataframe.isnull().sum()
        return missing_values
    
    def handle_missing(self, strategy = "fill", fill_value = 0):
        if strategy == "drop":
            self.dataframe = self.dataframe.dropna()
        elif strategy == "fill":
            self.dataframe = self.dataframe.fillna(fill_value)
        return self.dataframe
    
    def convert_types(self):
        self.dataframe["Date"] = pd.to_datetime(self.dataframe["Date"])

        self.dataframe["StateHoliday"] = self.dataframe["StateHoliday"].astype("category")

        return self.dataframe
    
    def remove_duplicates(self):

        self.dataframe = self.dataframe.drop_duplicates()
        return self.dataframe

    def normalize_columns(self):
        self.dataframe.columns = self.dataframe.columns.str.lower().str.replace(" ", "_")
        return self.dataframe