import pandas as pd
from time import time
"""
Média entre tipos, um pokemon que pertence tanto aos tipos grass
e poison mudará ambas categorias grass e poison
"""

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')
df['Count'] = 1
stats1 = ['Total', 'HP', 'Attack','Defense','Sp. Atk','Sp. Def','Speed','Legendary', 'Count','Type 1']
stats2 = ['Total', 'HP', 'Attack','Defense','Sp. Atk','Sp. Def','Speed','Legendary', 'Count','Type 2']

grupo1 = df[stats1].groupby('Type 1').sum()
grupo2 = df[stats2].groupby('Type 2').sum()
# mean single type
mst = (grupo1+grupo2)
mst2 = mst.copy()  # for method 2
div = mst['Count']

def method1(n=1):
    """
    method 1 3.86 1000x iterações
    """

    for c in range(0,n):
        for col in mst:
            mst[col] = mst[col]/div
        mst = round(mst, 2)


def method2(n=1):
    """
    # method 2 1.82 1000x iterações
    """
    for c in range(0,n):
        div = pd.DataFrame(div, columns=mst.columns).fillna(method='bfill', axis=1)
        div['Count'] = 1
        mst2 = mst2/div
        mst2 = round(mst2, 2)


'''
print('Method 1 equals method 2 for cols')
print((mst == mst2).all())
'''


