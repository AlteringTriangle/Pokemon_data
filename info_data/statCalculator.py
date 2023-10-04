import pandas as pd
import numpy as np
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)
col_sel = ['Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']
df = df[col_sel].set_index('Name')


def sta_cal(name, iv=..., ev=252, level=100, nature=...):
    if iv is ...:
        iv = pd.Series([31, 31, 31, 31, 31, 31], index=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    elif len(iv) != 1 and len(iv) != 6:
        raise ValueError('O iv do pokemon deve ser fixo ou ter 6 valores distintos')
    elif len(iv) == 1:
        iv = iv[0]
        iv = pd.Series([iv,iv,iv,iv,iv,iv], index=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    else:
        iv = pd.Series(iv, index=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])

    if nature is ...:
        nature = pd.Series([1.1, 1.1, 1.1, 1.1, 1.1], index=['Attack', 'Defense','Sp. Atk', 'Sp. Def', 'Speed'])
    elif len(nature) != 5:
        raise ValueError('A nature deve carregar 5 valores distintos')
    else:
        nature = pd.Series(nature, index=['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])

    poke = df.loc[name].copy()
    iv_ev = iv + (ev / 4)
    def f1(stat):
        poke.loc[stat] = np.floor((((2*poke.loc[stat]+iv_ev[stat])*level/100) + 5) * nature[stat])

    def f2(stat):
        poke.loc[stat] = np.floor(((2*poke.loc[stat]+iv_ev[stat])*level/100) + level + 10)

    f1('Attack')
    f1('Defense')
    f1('Sp. Atk')
    f1('Sp. Def')
    f1('Speed')
    f2('HP')

    return poke

# order ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
# nature buff = 1.1, nature debuff =0.9, normal=1, for ['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']


print(sta_cal('MewtwoMega Mewtwo Y', level=113, iv=[31], ev=252))
print(sta_cal('Accelgor', level=100, iv=[31], ev=252))
