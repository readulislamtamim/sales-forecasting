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
from sklearn.linear_model import LinearRegression

class ModelBuilder:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.model = None
    
    def train_baseline_model(self, feature_columns, target_column):
        X = self.dataframe[feature_columns]
        y = self.dataframe[target_column]

        self.model = LinearRegression()
        self.model.fit(X, y)

        return self.model

    