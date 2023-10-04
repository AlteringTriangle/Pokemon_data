import pandas as pd
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)

raw = ~df['Name'].str.contains('Mega ')
df = df.loc[raw]
wmMask = df