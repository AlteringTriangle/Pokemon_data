import pandas as pd
from Pokemon.filtering_data.removeMega import raw as rm
from Pokemon.dataPath import datapath, addcolpath

df = pd.read_csv(datapath)
ac = pd.read_csv(addcolpath, usecols=['Base Form'])

df['Base Form'] = ac


# Até onde eu sei, quando há ramificações de evoluções, uma característica dos pokemons
# é de manter o total de stats, portanto ela será definitiva para remover formas
# bases duplicadas sem afetar ramificações.

# [ramific] é um DataFrame contendo as informações de forma base e da última forma do pokemon,
# ou seja, aquela mais forte, que tem a maior soma de stats base.
ramific = df[['Base Form', 'Total']].groupby(by=['Base Form']).max()
# o índice de with mega é mudado para que este possa receber os valores máximos da coluna total
# de ramific
with_mega = df.copy().set_index('Base Form')
with_mega['ramific'] = ramific['Total']
# o índice volta ao normal para a coluna ramific, que contem os valores totais máximos para cada
# forma base, concatene com o nome da forma base, para que assim possamos remover as duplicatas
# por cada espécie separada de pokemon
with_mega.reset_index(inplace=True)
with_mega['ramific'] = with_mega['ramific'].apply(str) + with_mega['Base Form']

raw1 = with_mega.drop_duplicates(subset='ramific', keep='last').sort_values(by='#')
# rau1['#'] > 0 faz com que o raw seja um dataframe booleano com valores sempre true
raw1 = raw1['#'] > 0
# df['#'] não pode ser menor que zero, portanto isto gera um dataframe booleano do tamanho
# de df, com todos os valores sendo falsos
false = df['#'] < 0
# raw1 agora é um dataframe booleano, com o mesmo indice que df, portanto pode ser utilizado
# rawx & rawy entre outras algebras booleanas
raw1 = raw1 | false

# rm -> raw remove mega
# infelizmente, podemos facilmente remover os megas sem qlqr mudança brusca, entretanto
# os dados da forma anterior a mega evolução em questão já foi perdida,
# portanto é necessário refazer o precedimento
df2 = df.copy().loc[rm] # df2 → dados sem mega evoluções
ramific = df2[['Base Form', 'Total']].groupby(by=['Base Form']).max()
without_mega = df2.copy().set_index('Base Form')
without_mega['ramific'] = ramific['Total']
without_mega.reset_index(inplace=True)
without_mega['ramific'] = without_mega['ramific'].apply(str) + without_mega['Base Form']
raw2 = without_mega.drop_duplicates(subset='ramific', keep='last').sort_values(by='#')
raw2 = raw2['#'] > 0
raw2 = raw2 | false

# Relevant info
# print(df.loc[raw2].reset_index().to_string())
# print(df.loc[raw1].reset_index().to_string())



