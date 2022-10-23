import pandas as pd


'''
Aqui a média entre os tipos duplos, um pokemon do tipo grass
e poison, não pertencerá somente ao grass, ou ao poison, mas
sim a categoria grass-poison
'''

df = pd.read_csv('pokemon.csv')
extra = pd.read_csv('added_cols.csv',usecols=['MultiType'])
df['MultiType'] = extra

df = df[['Total', 'HP', 'Attack', 'Sp. Atk', 'Defense', 'Sp. Def', 'Speed', 'MultiType']]
ct = df.groupby('MultiType').count()
ct = ct['Total']
ct.name = 'Count'
print(ct)
df = df.groupby('MultiType').mean().astype('int64')
df['Occurrences'] = ct
print(df.sort_values('Occurrences', ascending=False).to_string())
