

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
        self.dataFrame = pd.DataFrame(self.file_path)
        return self.dataFrame