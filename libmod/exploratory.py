import pandas as pd
import numpy as np

class DataConverters:
    def binarize(orig_series):
        """Convert to 0/1 values
        """
        series=pd.Series().reindex_like(orig_series)
        for i,val in enumerate(orig_series):
            series[i]=np.array(val>0).astype(float)
        return pd.to_numeric(series,errors="coerce")
    
class Explore:
    converters={
    "Do not convert": None,
    "Binarize" : DataConverters.binarize,
    }
    
