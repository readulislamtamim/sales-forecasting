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
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

import numpy as np

class ModelEvaluator:
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
    
    def evaluate_model(self, model):
        y_pred = model.predict(self.X_test)
        rmse = np.sqrt(mean_squared_error(self.y_test, y_pred))
        r2 = r2_score(self.y_test, y_pred)

        return {"RMSE" : rmse, "R2" : r2}
    
    def compare_models(self):
        results = {}

        lin_reg = LinearRegression()
        lin_reg.fit(self.X_train, self.y_train)
        results["Linear Regression"] = self.evaluate_model(lin_reg)

        tree = DecisionTreeRegressor(random_state=42)
        tree.fit(self.X_train, self.y_train)
        results["Decision Tree"] = self.evaluate_model(tree)

   
        forest = RandomForestRegressor(random_state=42)
        forest.fit(self.X_train, self.y_train)
        results["Random Forest"] = self.evaluate_model(forest)

        return results
