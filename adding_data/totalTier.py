import pandas as pd

#'C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv'
#'C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv'

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
df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')

framerows = df['Total']
fuc = df['Total'].quantile(.05)
euc = df['Total'].quantile(.15)
duc = df['Total'].quantile(.3)
cuc = df['Total'].quantile(.45)
buc = df['Total'].quantile(.6)
auc = df['Total'].quantile(.78)
suc = df['Total'].quantile(.95)
ssuc = df['Total'].quantile(1)


# as linhas do dataframe que estão abaixo do upper cut, recebem 'F' na coluna 'Total Tier'
df.loc[framerows < fuc, 'Total Tier'] = 'F'
# linhas acima de F upper cut e abaixo de E upper cut recebem 'E' na coluna "total tier'
df.loc[(framerows > fuc) & (framerows < euc), 'Total Tier'] = 'E'
# etc..
df.loc[(framerows >= euc) & (framerows < duc), 'Total Tier'] = 'D'
df.loc[(framerows >= duc) & (framerows < cuc), 'Total Tier'] = 'C'
df.loc[(framerows >= cuc) & (framerows < buc), 'Total Tier'] = 'B'
df.loc[(framerows >= buc) & (framerows < auc), 'Total Tier'] = 'A'
df.loc[(framerows >= auc) & (framerows < suc), 'Total Tier'] = 'S'
df.loc[(framerows >= suc), 'Total Tier'] = 'SS'

# relevant info
# print(f'F < {fuc}\nE >= {fuc}\nD >= {euc}\nC >= {duc}\nB >= {cuc}\nA >= {buc}\nS >= {auc}\nSS >= {suc}')
# print(df[['Name','Total Tier']].groupby('Total Tier').count())

if __name__ == '__main__':
    save = input('save?')
    if save == 'save':
        ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv')
        ac['Total Tier'] = df['Total Tier']
        ac.to_csv('added_cols.csv', index=False)