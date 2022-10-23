import pandas as pd

df = pd.read_csv('pokemon.csv')

a = df.loc[df['Name'].str.contains('Forme')]
print(a)

