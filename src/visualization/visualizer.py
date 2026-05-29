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
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def plot_sales_trend(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.dataframe["date"], self.dataframe["sales"], color = "blue")
        plt.title("Sales Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.show()
    
    def plot_sales_by_weekday(self):
        weekday_sales = self.dataframe.groupby("day_of_week")["sales"].mean()
        plt.figure(figsize=(12, 6))
        plt.plot(weekday_sales.index, weekday_sales.values, color = "blue")
        plt.title("Average Sales by Weekday")
        plt.xlabel("Day of week (1=Mon, 7=Sun)")
        plt.ylabel("Average Sales")
        plt.show()
    
    def plot_sales_by_promo(self):
        promo_sales = self.dataframe.groupby("promo")["sales"].mean()
        plt.figure(figsize=(6,4))
        plt.bar(promo_sales.index, promo_sales.values, color = ["skyblue", "coral"])
        plt.title("Average Sales by Promotion Status")
        plt.xticks([0, 1], ["No Promo", "Promo"])
        plt.xlabel("Promotion Status")
        plt.ylabel("Average Sales")
        plt.show()
    
    def plot_sales_by_holiday(self):
        holiday_sales = self.dataframe.groupby("is_state_holiday")["sales"].mean()
        plt.figure(figsize=(6,4))
        plt.bar(holiday_sales.index, holiday_sales.values, color = ["skyblue", "coral"])
        plt.xticks([0,1], ["Non-holiday", "Holiday"])
        plt.title("Average Sales by Holiday Status")
        plt.xlabel("Holiday Status")
        plt.ylabel("Average Sales")
        plt.show()