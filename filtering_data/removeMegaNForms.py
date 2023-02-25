import pandas as pd
from Pokemon.filtering_data.removeForms import raw as mask1
from Pokemon.filtering_data.removeMega import raw as mask2

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')

# o raw contém a series booleana para selecionar os indices onde apenas formas/megas são excluidos
raw = mask1 & mask2

df = df.loc[raw]
wmfMask = df
print(df)


