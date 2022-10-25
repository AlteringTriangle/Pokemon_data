import pandas as pd
from removing_forms import raw as mask1
from removing_forms import exception
from removing_mega import raw as mask2


df = pd.read_csv('pokemon.csv')
raw = mask1 & mask2
df = df.loc[raw]
df = pd.concat([df, exception])
df.sort_index(inplace=True)
wmfMask = df.index

