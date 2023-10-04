import pandas as pd
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)


# O tipo multiplo será uma concatenação de strings entre o tipo 1 e o tipo 2
# Nem todos os pokemons possuem tipo 2, e NaNs não podem ser concatenados com strings
# por isso os valores ausentes serão preenchidos com fillna(''), não adicionando sequer
# um caractere a mais em pokemons que já são single type

type2nan = df['Type 2'].copy().fillna('')

# O tipo múltiplo é feito em ordem alfabética para evitar repetir
# tipos múltiplos redundantes como dark fightning e fightning dark
# Entre dark e fightning, por exemplo, o número que representa a letra d
# é menor que o número que representa a letra f, quanto a ordem alfabética, o
# dark vem primeiro, portanto:

# Posições no dataframe onde o tipo 1 vem primeiro em ordem alfabética
df.loc[df['Type 1'] < type2nan, 'MultiType'] = df['Type 1'] + ' ' + type2nan
#/\ se o tipo 1 for menor que o tipo 2, o tipo 1 ganha em ordem alfabética

#\/ caso contrário, o tipo 2 ganha em ordem alfabética
# Posições no dataframe onde o tipo 2 vem primeiro em ordem alfabética...
df.loc[df['Type 1'] > type2nan, 'MultiType'] = type2nan + ' ' + df['Type 1']


if __name__ == '__main__':
    save = input('save?')
    if save == 'save':
        # primeiro carrega as informações já obtidas, adiciona a coluna e então salva
        ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv')
        ac['MultiType'] = df['MultiType']
        ac.to_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv', index=False)





