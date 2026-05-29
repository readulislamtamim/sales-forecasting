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
