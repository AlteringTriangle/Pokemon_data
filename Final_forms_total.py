import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('pokemon.csv')
add = pd.read_csv('added_cols.csv')

df[add.columns] = add

wmfMask = df.drop_duplicates(keep='first', subset='#')  # WMF -> without mega and forms
ffMask = wmfMask.drop_duplicates(keep='last', subset='Base Form').reset_index(drop=True)  # FF -> Final Forms

