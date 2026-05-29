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
class FeatureEngineer:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def add_date_part(self):
        self.dataframe["year"] = self.dataframe["date"].dt.year
        self.dataframe["month"] = self.dataframe["date"].dt.month
        self.dataframe["day"] = self.dataframe["date"].dt.day
        return self.dataframe