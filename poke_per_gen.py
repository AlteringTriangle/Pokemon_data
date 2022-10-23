import pandas as pd
from Pokemon.removing_mega_and_forms import wmfMask

df = pd.read_csv('pokemon.csv')
df = df.loc[wmfMask]  # without mega and forms
df = df.groupby('Generation').count()
df['Poke Por Geração'] = df['#']
df['Multi-types'] = df['Type 2']
df = df[['Poke Por Geração', 'Multi-types']]

print(df)

