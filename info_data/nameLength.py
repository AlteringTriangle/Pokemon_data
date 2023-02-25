import pandas as pd
from Pokemon.filtering_data.removeMegaNForms import raw

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')
df = df.loc[raw]
a = list()

for row in df['Name']:
    a.append(len(row))



