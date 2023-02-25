import pandas as pd
df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')

raw = ~df['Name'].str.contains('Mega ')
df = df.loc[raw]
wmMask = df