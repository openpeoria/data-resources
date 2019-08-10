import os
from pathlib import Path
import pandas as pd
import pandas_profiling

#%% Setup paths
script_dir = str(Path(__file__).parents[0]) 
project_dir =  str(Path(__file__).parents[1])
data_dir = os.path.join(project_dir, 'data')

#%%
df = pd.read_csv(os.path.join(data_dir,"USA - Eviction Lab","all_original.csv"))
df.drop(labels=['low-flag', 'imputed', 'subbed'],axis=1,inplace=True)


profile = pandas_profiling.ProfileReport(df)
profile.to_file(outputfile="profiled_data.html")