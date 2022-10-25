import pandas as pd
from Pokemon.removing_mega_and_forms import wmfMask

df = pd.read_csv('pokemon.csv')

search = df.set_index('Name').loc['Spinarak']
print(search)
