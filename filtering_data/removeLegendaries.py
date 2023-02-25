import pandas as pd
df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')


raw = df['Legendary'] == True
df = df.loc[raw]
lMask = df
