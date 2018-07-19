import pandas as pd

class Frames:
    """Static class containing methods for pandas dataframes
    
    Methods:
        smart_sample: Avoid pandas' spitting errors when using sample function
    """
    def smart_sample(dataframe,rows):
        """Avoid pandas' spitting errors when using sample function
        """
        if dataframe.shape[0]>=rows:
            return dataframe.sample(rows)
        else:
            return dataframe