import pandas as pd
from removing_forms import raw as mask1
from removing_forms import exception
from removing_mega import raw as mask2


df = pd.read_csv('pokemon.csv')
df = df.loc[mask2 & mask1]
df = pd.concat([df, exception])
df.sort_index(inplace=True)
wmfMask = df.index

