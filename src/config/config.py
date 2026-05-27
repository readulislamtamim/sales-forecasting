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

    PROJECT_ROOT = rf'G:/My Drive/Data Science/Personal/{PROJECT_NAME}'

    print("Running in local environment.")

# Move to project root
os.chdir(PROJECT_ROOT)

print("Current working directory:", os.getcwd())

# Add project root to Python path
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


#%%

class ProjectConfig:

    """
    This for storing project-wide settings such as file paths.
    
    """
    def __init__(self, project_name, raw_data_path, processed_data_path):
        self.project_name = project_name
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path
    
    def show_project_name(self):
        print(f"Project Name: {self.project_name}")
    
    def show_data_paths(self):
         print(f"Raw Data Path: {self.raw_data_path}")
         print(f"Processed Data Path: {self.processed_data_path}")

