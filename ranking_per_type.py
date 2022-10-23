import pandas as pd
from Pokemon.removing_mega_and_forms import wmfMask

df = pd.read_csv('pokemon.csv')
df = df.loc[wmfMask]  # without mega and forms

qType = 'fire'.title()
qStat = 'sp. atk'.title()

typeMask = (df['Type 1'] == qType) | (df['Type 2'] == qType)
ranking = df.loc[typeMask].sort_values(by=qStat, ascending=False).iloc[:10]
cols = ['Name','Type 1','Type 2','HP','Attack','Sp. Atk','Defense','Sp. Def','Speed','Total']
print(ranking[cols].to_string())
