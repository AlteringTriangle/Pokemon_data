import pandas as pd

df = pd.read_csv('pokemon.csv')

df = df.loc[df['Legendary'] == True]

print(df.sort_values(by='Total').to_string())