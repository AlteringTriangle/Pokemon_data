import pandas as pd


df = pd.read_csv('pokemon.csv')
raw = df.loc[df['Legendary'] == False]
df = df.loc[raw]
df.sort_index(inplace=True)
wlMask = df.index
