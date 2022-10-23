import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('pokemon.csv')

type2nan = df['Type 2'].copy().fillna('')

# o tipo multiplo é feito em ordem alfabetica para não repetir grupos de tipos
# ex: dark fight == fight dark
df.loc[df['Type 1'] < type2nan, 'MultiType'] = df["Type 1"] + ' ' + type2nan
df.loc[df['Type 1'] > type2nan, 'MultiType'] = type2nan + ' ' + df["Type 1"]
df['MultiType'] = df['MultiType'].str.strip()

ac = pd.read_csv('added_cols.csv')

# ac.loc.__setitem__((slice(None), 'MultiType'), df['MultiType'])
ac['MultiType'] = df['MultiType']
ac.to_csv('added_cols.csv', index=False)