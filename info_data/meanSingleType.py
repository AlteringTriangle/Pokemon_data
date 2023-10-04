import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Pokemon.filtering_data.removeForms import raw as mask1
from Pokemon.filtering_data.removeMega import raw as mask2
from Pokemon.dataPath import datapath
from time import time

"""
Média entre tipos, um pokemon que pertence tanto aos tipos grass
e poison mudará ambas categorias grass e poison
"""


def colorize(r1, r2, g1, g2, b1, b2, n):
    colors_list = list()
    for c in range(0, n):
        r = '0' + str(hex(int(r1 - c * (r1 - r2) / n)))[2:]
        g = '0' + str(hex(int(g1 - c * (g1 - g2) / n)))[2:]
        b = '0' + str(hex(int(b1 - c * (b1 - b2) / n)))[2:]
        colors_list.append(f'#{r[-2:]}{g[-2:]}{b[-2:]}')
    return colors_list


def grayscale(min, max, n):
    colors_list = list()
    for c in range(0, n):
        # intervalos igualmente espaçados entre 0 e 0.4
        colors_list.append(str(c / (n / max) + min))
    return colors_list


df = pd.read_csv(datapath)
mask = mask1 & mask2
# mega evoluções e formas afetam e muito a contagem de lendários e principalmente
# desbalanceiam o total de muitos tipos diferentes, portanto serão filtrados
df = df.loc[mask]
# a coluna count servirá para calcular a media final
df['Count'] = 1
# statsx é apenas uma maneira mais simples de escolher os dados a serem apresentados e modificados
stats1 = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Legendary', 'Count', 'Type 1']
stats2 = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Legendary', 'Count', 'Type 2']
statsdiv = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Legendary', 'Count']

# A média da soma de duas médias, não é exatamente a média total,
# portanto será necessário a soma dos termos, a quantidade de termos
# e a soma dos dois grupos, por fim dividido pelo total.
grupo1 = df[stats1].groupby('Type 1').sum()
grupo2 = df[stats2].groupby('Type 2').sum()
mst = (grupo1 + grupo2)
# div é um dataframe que repete os valores de Count a linha toda para cada coluna de mst
div = pd.DataFrame(np.array((mst['Count'],) * len(mst.columns)).T,
                   columns=mst.columns, index=mst.index)
# a contagem de lendários é interessante sem um valor de média, portanto é substituída por 1
# para se manter neutra
div['Legendary'] = 1

# count é uma coluna que, se for diferente de 1, significa que algo deu errado,
# portanto é interessante mostrá-la no final
mst = (mst / div[statsdiv]).astype(int)
# print(mst[statsdiv].to_string())


fig, axs = plt.subplots(2, 1, facecolor='#bbb', edgecolor='white',
                        layout='tight', figsize=[6.4, 4.8], dpi=100)

r1, g1, b1 = int('20', 16), int('30', 16), int('dd', 16)
r2, g2, b2 = int('ff', 16), int('00', 16), int('ff', 16)
colors = colorize(r1, r2, g1, g2, b1, b2, 18)

axs[0].bar(mst.index, mst['Total'], color=colors)
axs[0].grid(True)
axs[0].set_xlabel('Tipos')
axs[0].set_ylabel('Stats Totais')
axs[0].set_ylim(300, 510)
axs[0].set_title("Stats totais por tipo")

r1, g1, b1 = int('ff', 16), int('a5', 16), int('00', 16)
r2, g2, b2 = int('99', 16), int('32', 16), int('cc', 16)
colors2 = colorize(r1, r2, g1, g2, b1, b2, 18)

axs[1].bar(mst.index, mst['Legendary'], color=colors2)
axs[1].grid(True)
axs[1].set_xlabel('Tipos')
axs[1].set_ylabel('Quantidade de Lendários')
axs[1].set_title("Quantidade de lendários por tipo")
plt.show()
