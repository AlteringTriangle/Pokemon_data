import pandas as pd


df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')

# como as colunas type 1 e 2 serão concatenadas, os nan de type 2
# virarão um caractere vazio

type2nan = df['Type 2'].copy().fillna('')

# O tipo múltiplo é feito em ordem alfabética para evitar repetir
# tipos múltiplos redundantes como dark fightning e fightning dark

# Posições no dataframe onde o tipo 1 vem primeiro em ordem alfabética
# o multitype receberá \/
df.loc[df['Type 1'] < type2nan, 'MultiType'] = df['Type 1'] + ' ' + type2nan
# Posições no dataframe onde o tipo 2 vem primeiro em ordem alfabética...
df.loc[df['Type 1'] > type2nan, 'MultiType'] = type2nan + ' ' + df['Type 1']


if __name__ == '__main__':
    save = input('save?')
    if save == 'save':
        # primeiro carrega as informações já obtidas, adiciona a coluna e então salva
        ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv')
        ac['MultiType'] = df['MultiType']
        ac.to_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv', index=False)





