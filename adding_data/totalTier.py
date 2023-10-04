import pandas as pd
from Pokemon.dataPath import datapath

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
isto se baseia não só em um valor inicial, e somas sucessivas de .15, mas também do
tamanho do grupo criado, SS por exemplo deve ser um grupo seleto, e portanto conter menos
pokemons, o mesmo vale para S, que sobe um pouco mais do que .15 para reduzir um pouco mais
o grupo
'''
df = pd.read_csv(datapath)

framerows = df['Total']

# constantes que representam o valor de total que está nas posições 5%, 15%, etc...
# uc -> upper cut ou corte superior
fuc = df['Total'].quantile(.05)
euc = df['Total'].quantile(.15)
duc = df['Total'].quantile(.3)
cuc = df['Total'].quantile(.45)
buc = df['Total'].quantile(.6)
auc = df['Total'].quantile(.78)
suc = df['Total'].quantile(.95)
ssuc = df['Total'].quantile(1)


# Para cada tier, então, teremos cortes superiores ou inferiores
# as linhas do dataframe que estão abaixo do corte superior, recebem 'F' na coluna 'Total Tier'
# Devido a nenhum pokemon ter total negativo, é redundante utilizar o corte infeiror valendo 0
df.loc[framerows < fuc, 'Total Tier'] = 'F'
# linhas acima do corte superior de F e abaixo do corte superior de E recebem 'E' 
# na coluna "total tier'. o corte superior de F funciona exatamente como um corte inferior para E
df.loc[(framerows > fuc) & (framerows < euc), 'Total Tier'] = 'E'
# E assim suscecivamente...
df.loc[(framerows >= euc) & (framerows < duc), 'Total Tier'] = 'D'
df.loc[(framerows >= duc) & (framerows < cuc), 'Total Tier'] = 'C'
df.loc[(framerows >= cuc) & (framerows < buc), 'Total Tier'] = 'B'
df.loc[(framerows >= buc) & (framerows < auc), 'Total Tier'] = 'A'
df.loc[(framerows >= auc) & (framerows < suc), 'Total Tier'] = 'S'
df.loc[(framerows >= suc), 'Total Tier'] = 'SS'

# informações relevantes
# print(f'F < {fuc}\nE >= {fuc}\nD >= {euc}\nC >= {duc}\nB >= {cuc}\nA >= {buc}\nS >= {auc}\nSS >= {suc}')
# print(df[['Name','Total Tier']].groupby('Total Tier').count())

if __name__ == '__main__':
    # verificação de salvamento
    save = input('save?')
    if save == 'save':
        ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv')
        ac['Total Tier'] = df['Total Tier']
        ac.to_csv('added_cols.csv', index=False)