import pandas as pd
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)


raw = ~df['Legendary'] == True
df = df.loc[raw]
lMask = df
