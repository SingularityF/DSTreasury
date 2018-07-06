import pandas as pd
import numpy as np
import tempfile

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
    

def is_factor(series):
    return False if np.issubdtype(series.dtype,np.number) else True

# Avoid pandas' spitting errors when using sample function
def smart_sample(dataframe,rows):
    if dataframe.shape[0]>=rows:
        return dataframe.sample(rows)
    else:
        return dataframe

# Excel report heading
def make_heading(colid,rowid,content,workbook,worksheet):
    heading_format=workbook.add_format({'bold': True,'font_size':20})
    worksheet.write('{}{}'.format(colid,rowid), content,heading_format)

# Excel report plot
# Temp files not deleted
# May cause leak for small tmp space
def make_plot(colid,rowid,fig,worksheet):
    _,path2file=tempfile.mkstemp(suffix=".png")
    fig.set_size_inches(6.4*.7,4.8*.7)
    fig.savefig(path2file,dpi=300)
    worksheet.insert_image('{}{}'.format(colid,rowid), path2file)

# Excel report change line
def adv_ptr_var(df,amount):
# Add blank row after df
    if df.shape[0]>=amount:
        return amount+2
    else:
        return df.shape[0]+2
    