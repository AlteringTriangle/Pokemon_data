import pandas as pd

df = pd.read_csv('pokemon.csv')
raw = ~df['Name'].str.contains('Mega ')
df = df.loc[raw]
wmMask = df.index
