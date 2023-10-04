import pandas as pd
from Pokemon.dataPath import datapath
from Pokemon.filtering_data.removeForms import raw as mask1
from Pokemon.filtering_data.removeMega import raw as mask2

df = pd.read_csv(datapath)

# o raw contém a series booleana para selecionar os indices onde apenas formas/megas são excluidos
raw = mask1 & mask2

df = df.loc[raw]
wmfMask = df

# método 2
'''
caso as formas e as mega evoluções devam ser removidas juntas, é mais conveniente remover as entradas
duplicadas da pokedex, simbolizada pela coluna '#'
o problema é que este dataframe não possui o mesmo index que raw, portanto não pode ser utilizado
diretamente em equações booleanas, entretanto pode ser convertido valendo-se de:
A coluna True contém todos os valores de entradas não duplicadas, ou formas simples
dos pokemons, valendo true
aqui transformamos a máscara em um series booleano, que só pode entrar em equações
booleanas de indice igual, portanto é meio inútil como uma máscara que filtra
as mega-evoluções e formas
entretanto, criando uma series booleana falsa com o índice dos dados originais
e aplicando [or] em ambas, temos uma máscara true para todos os pokemons não duplicados
de maneira que selecionamos apenas formas simples, e poucos pokemons são execçao e essa
regra, como meowsticMale e meowsticFemale
'''

pre_wmfMask2 = df.drop_duplicates(keep='first', subset='#')
pre_wmfMask2['True'] = True
pre_wmfMask2 = pre_wmfMask2['True'] == True
df['False'] = False
false_df = df['False'] == True
wmfMask2 = pre_wmfMask2 | false_df

print(wmfMask2)
# print(df)
