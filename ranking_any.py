import pandas as pd
from Pokemon.removing_mega_and_forms import wmfMask

df = pd.read_csv('pokemon.csv')
df = df.loc[wmfMask]  # without mega and forms

num = 130
stat = 'attack'.title()
print(df[['Name', 'Total', stat, 'Legendary']].loc[df[stat] >= num].sort_values(by=stat, ascending=False))
