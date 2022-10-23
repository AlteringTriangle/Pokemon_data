import pandas as pd

df = pd.read_csv('pokemon.csv')
# in case of a pokémon haven't a base form, both forms will be displayed

raw = ~df['Name'].str.contains('Forme|Unbound| Size| Kyurem|Zen Mode|'
                               ' Rotom|Sandy Cloak|Trash Cloak|Primal ')

exception = df.loc[[428, 750, 751, 716, 715, 713, 714, 544, 784, 780,
                    545, 550, 551, 702, 703, 704, 705, 708, 709]]

df = pd.concat([df.loc[raw], exception])
df.sort_index(inplace=True)
wfMask = df.index
