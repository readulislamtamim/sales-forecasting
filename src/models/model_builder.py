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
from sklearn.model_selection import train_test_split

class ModelBuilder:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.model = None
    
    def train_test_split(self, feature_columns, target_column, test_size = 0.2, random_state = 42):
        X = self.dataframe[feature_columns]
        y = self.dataframe[target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state = random_state)

        return X_train, X_test, y_train, y_test

    def train_baseline_model(self, X_train, y_train):
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        return self.model

    