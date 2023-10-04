import pandas as pd
import matplotlib.pyplot as plt
from Pokemon.dataPath import datapath
from Pokemon.filtering_data.removeForms import raw as mask1
from Pokemon.filtering_data.removeMega import raw as mask2

def colorize(r1, r2, g1, g2, b1, b2, n):
    colors_list = list()
    for c in range(0, n):
        r = '0' + str(hex(int(r1 - c * (r1 - r2) / n)))[2:]
        g = '0' + str(hex(int(g1 - c * (g1 - g2) / n)))[2:]
        b = '0' + str(hex(int(b1 - c * (b1 - b2) / n)))[2:]
        colors_list.append(f'#{r[-2:]}{g[-2:]}{b[-2:]}')
    return colors_list


df = pd.read_csv(datapath)
rm = mask1 & mask2
df = df.loc[rm]
df = df[['#', 'Generation']].groupby('Generation').count()

fig, ax = plt.subplots(1, 1, dpi=100, facecolor='#bbb')
plt.bar(df.index, df['#'])
ax.grid(True)
ax.set_title('Pokemons por geração')
ax.set_xlabel('Geração')
ax.set_ylabel('Quantidade de pokemons (novos)')
ax.set_ylim(60, 180)
plt.show()