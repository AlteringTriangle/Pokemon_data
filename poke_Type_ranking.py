import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('pokemon.csv')

pType = 'fire'.capitalize()
pStat = 'speed'.capitalize()

ranking = df.loc[(df['Type 1'] == pType) | (df['Type 2'] == pType)].sort_values(by=pStat, ascending=False)

wmf = df.drop_duplicates(subset='#', keep='first')  # Without mega and forms
df = wmf
def do_ranking(pType, pStat, n=10):
    pType = pType.title()
    pStat = pStat.title()
    ranking = df.loc[(df['Type 1'] == pType) | (df['Type 2'] == pType)].sort_values(by=pStat, ascending=False)
    slct = ['Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Sp. Atk', 'Defense', 'Sp. Def', 'Speed']
    print(ranking[slct].iloc[:n].to_string())




print(f'[A] é igual a [a]? {"A" == "a"}')
print('fire SPEED'.upper())
print('fire SPEED'.capitalize())
print('fire SPEED'.title())
print('fire SPEED'.lower())
do_ranking('fire', 'attack')
do_ranking('fire', 'speed')
do_ranking('fire', 'sp. atk')
do_ranking('fire', 'defense')
do_ranking('fire', 'sp. def')





