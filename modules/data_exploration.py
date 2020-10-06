
from IPython.display import display

def data_exploration(df):
    display((df.head(),
             df.shape,
             df.info(),
             df.describe()))
