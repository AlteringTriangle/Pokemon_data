import pandas as pd
"""
Média entre tipos duplos, um pokemon que pertence tanto aos tipos grass
e poison mudará a categoria específica grass/poison
"""

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')
ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv', usecols=['MultiType'])

df['MT'] = ac
df['Count'] = 1

mdt = df.groupby('MT').sum()
div = mdt['Count']
div = pd.DataFrame(div, columns=mdt.columns).fillna(method='bfill',axis=1)
div['Count'] = 1
mdt = round(mdt/div, 2)
print(mdt)


