import pandas as pd
from removeMega import raw as mask1


df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')

# Considerando que Mew é capturável no jogo, > 600 será ignorado
legendary_mask = df['Legendary'] == True
bt600Mask = df['Total'] > 600  # bigger than 600 (total) mask
l_lt600Mask = ~(legendary_mask & bt600Mask)  # legendaries lower than 600

raw = l_lt600Mask & mask1
poMask = df.loc[raw]
print(poMask)
