import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


'''
Aqui vou assumir eu mesmo que o tier da soma dos
status totais de um pokemon será:
    - F < quantile(0.05)
    - E >= quantile(0.05)
    - D >= quantile(0.15)
    - C >= quantile(0.3)
    - B >= quantile(0.45)
    - A >= quantile(0.6)
    - S >= quantile(0.78)
    - SS >= quantile(0.95)
'''
df = pd.read_csv('pokemon.csv')

# INCLUDING END
def between(first, last):
    return df['Total'].loc[((df['Total'] >= first) & (df['Total'] <= last))].index


bt = between

df.loc[bt(0, df['Total'].quantile(.05)), 'Total Tier'] = 'F'
df.loc[bt(df['Total'].quantile(.05), df['Total'].quantile(.15)), 'Total Tier'] = 'E'
df.loc[bt(df['Total'].quantile(.15), df['Total'].quantile(.3)), 'Total Tier'] = 'D'
df.loc[bt(df['Total'].quantile(.3), df['Total'].quantile(.45)), 'Total Tier'] = 'C'
df.loc[bt(df['Total'].quantile(.45), df['Total'].quantile(.6)), 'Total Tier'] = 'B'
df.loc[bt(df['Total'].quantile(.6), df['Total'].quantile(.78)), 'Total Tier'] = 'A'
df.loc[bt(df['Total'].quantile(.78), df['Total'].quantile(.95)), 'Total Tier'] = 'S'
df.loc[bt(df['Total'].quantile(.95), df['Total'].quantile(1)), 'Total Tier'] = 'SS'

print(df[['Name', 'Total', 'Total Tier']])
print(df[['Name','Total Tier']].groupby('Total Tier').count())

f = df['Total'].quantile(0.05)
e = df['Total'].quantile(0.05)
d = df['Total'].quantile(0.15)
c = df['Total'].quantile(0.3)
b = df['Total'].quantile(0.45)
a = df['Total'].quantile(0.6)
s = df['Total'].quantile(0.78)
ss = df['Total'].quantile(0.95)
print(f'F < {f}\nE >= {e}\nD >= {d}\nC >= {c}\n'
      f'B >= {b}\nA >= {a}\nS >= {s}\nSS >= {ss}')

tier_id = df.copy().set_index('Total Tier')
d = 2
starters = [1 + d, 4 + d, 7 + d, 152 + d, 155 + d, 158 + d, 252 + d, 255 + d, 258 + d,
            387 + d, 390 + d, 393 + d, 495 + d, 498 + d, 501 + d, 650 + d, 653 + d, 656 + d]
print(tier_id.loc['D'])
print(df.set_index('#').loc[starters].sort_values(by='Total').to_string())

'''
# saving
ac = pd.read_csv('added_cols.csv')
ac['Total Tier'] = df['Total Tier']
ac.to_csv('added_cols.csv', index=False)
'''