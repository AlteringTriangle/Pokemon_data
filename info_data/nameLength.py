import pandas as pd
from Pokemon.dataPath import datapath
from Pokemon.filtering_data.removeMegaNForms import raw

df = pd.read_csv(datapath)
df = df.loc[raw]

df['NameLength'] = df['Name'].apply(len)
print(df['NameLength'])


