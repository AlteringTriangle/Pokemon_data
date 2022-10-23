import pandas as pd
'''
Aqui a média entre os tipos, um pokemon do tipo grass e poison
vai ser considerado tanto para o tipo grass, quanto para o poison
'''

df = pd.read_csv('pokemon.csv')

g1 = df.groupby('Type 1').sum()
g1['Count'] = df[['Type 1','Total']].groupby('Type 1').count()
g2 = df.groupby('Type 2').sum()
g2['Count'] = df[['Type 2','Total']].groupby('Type 2').count()

g3 = g1 + g2
g3 = g3[['Total', 'HP','Attack','Sp. Atk','Defense','Sp. Def','Speed','Count']]
ct = g3['Count']
rdf = g3.copy()

for c in range(0, g3.shape[0]):
    rdf.loc[g3.index[c]] = g3.iloc[c]/g3['Count'].iloc[c]

int64sel = ['Total', 'HP','Attack','Sp. Atk','Defense','Sp. Def','Speed']
rdf = rdf[int64sel].astype('int64')
rdf['Occurrences'] = ct
print(rdf.sort_values('Occurrences', ascending=False))

