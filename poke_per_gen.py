import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon.csv')

wmfMask = df.drop_duplicates(keep='first', subset='#')  # without mega and forms

df = wmfMask.groupby('Generation').count()

df['Poke Por Geração'] = df['#']
df['Multi-types'] = df['Type 2']
df = df[['Poke Por Geração', 'Multi-types']]

print(df)

