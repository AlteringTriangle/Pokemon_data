import pandas as pd
import numpy as np


df = pd.read_csv('pokemon.csv')

mask1 = df.set_index('Type 1')
mask1.index.name = 'tipo'
mask2 = df.loc[df['Type 2'] != np.NaN]
mask2.index.name = 'tipo'
print(mask2.to_string())

