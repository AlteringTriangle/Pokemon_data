import pandas as pd
from Pokemon.removing_mega_and_forms import wmfMask


df = pd.read_csv('pokemon.csv')
add = pd.read_csv('added_cols.csv')

df[add.columns] = add

ffMask = df.loc[wmfMask].drop_duplicates(keep='last', subset='Base Form').reset_index(drop=True)  # FF -> Final Forms
print(ffMask)

