import pandas as pd

df = pd.read_csv('pokemon.csv')

bol =df['Name'] == 'volcarona'.title()
print(df.loc[bol].to_string())