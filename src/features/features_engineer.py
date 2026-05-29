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
    
    def day_of_week(self):
        self.dataframe.rename(columns = {"dayofweek":"day_of_week"}, inplace = True)
        return self.dataframe
    
    def add_holiday_flags(self):
        def map_state_holiday(value):
            if value == "0":
                return 0
            else:
                return 1
        
        self.dataframe["is_state_holiday"] = self.dataframe["stateholiday"].apply(map_state_holiday)
        self.dataframe["is_school_holiday"] = self.dataframe["schoolholiday"]
        return self.dataframe
    
    def add_interaction_features(self):
        self.dataframe["promo_weekday_interaction"] = self.dataframe["promo"] * self.dataframe["day_of_week"]
        self.dataframe["promo_stateholiday_interaction"] = self.dataframe["promo"] * self.dataframe["is_state_holiday"]
        return self.dataframe
    
    def add_lag_features(self):
        self.dataframe = self.dataframe.sort_values("date")
        self.dataframe["sales_lag_1"] = self.dataframe["sales"].shift(1)
        return self.dataframe