import pandas as pd
from Pokemon.filtering_data.removeMega import raw as rm

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')
ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv', usecols=['Base Form'])

df['Base Form'] = ac
df['Old id'] = df.index

with_mega = df.copy().sort_values(by=['Base Form','Total'])
# because eevee and multi path evolutions
ex = with_mega.copy()  # copy() for safe
each_max = ex.groupby(['Base Form'])['Total'].max()

# ex já está sorteado por base form\total
ex = ex.set_index('Base Form')

# bom... ta ai... e funciona...
# tirando o máximo de cada base form de todos os que pertence ao indice base form 'abra' por exemplo
ex = ex.loc[:]['Total']-(each_max[:])*.9
ex = ex.reset_index()

with_mega = with_mega.reset_index(drop=True)
pre_raw1 = ex['Total'] > 0
with_mega = with_mega.loc[pre_raw1]

old_id = with_mega.set_index('Old id').index
s1 = pd.Series(False, index=range(0,len(df)))
s2 = pd.Series(True, index=old_id)
raw1 = s1 | s2


# final forms without mega mask

without_mega = df.copy().loc[rm].sort_values(by=['Base Form','Total'])

ex = without_mega.copy()
each_max = ex.groupby(['Base Form'])['Total'].max()
ex = ex.set_index('Base Form')
ex = ex.loc[:]['Total']-(each_max[:])*.90
ex = ex.reset_index()

without_mega = without_mega.reset_index(drop=True)
pre_raw2 = ex['Total'] > 0
without_mega = without_mega.loc[pre_raw2]

old_id2 = without_mega.set_index('Old id').index
s1 = pd.Series(False, index=range(0,len(df)))
s2 = pd.Series(True, index=old_id2)
raw2 = s1 | s2


df.drop(columns='Old id',inplace=True)

# Relevant info
# print(df.loc[raw2].sort_values(by='Base Form').to_string())
# print(df.loc[raw1].sort_values(by='Base Form').to_string())

