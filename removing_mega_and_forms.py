import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('pokemon.csv')
wmMask = ~df['Name'].str.contains('Mega ')
wfMask = ~df['Name'].str.contains('Forme|Unbound| Size| Kyurem|Zen Mode|'
                                  ' Rotom|Sandy Cloak|Trash Cloak')

exception = df.loc[[428, 750, 751, 716, 715, 713, 714, 544, 784, 780,
                    545, 550, 551, 702, 703, 704, 705, 708, 709]]

df = df.loc[wfMask & wmMask]
df = pd.concat([df, exception])
df.sort_index(inplace=True)
print(df)