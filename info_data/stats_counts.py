import pandas as pd
import matplotlib.pyplot as plt
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)


def calcula_freq(data, stat):
    # Se baseando em um stat específico, ele será agrupado e contado
    # quantas vezes ele, como por exemplo 680 de total stat, aparece
    # na base de dados. (no caso, foram 13 vezes para total = 680)
    frequency = data[['#', stat]].groupby(stat).count()
    return frequency


stats = ['Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']
# a coluna '#' está sendo usada apenas para contar os casos
# cada stat tem uma distribuição de frequencia diferente com valores
# diferentes
status = 'Speed'


freq = calcula_freq(df, status)
freq_info = freq.reset_index()
maxf = freq_info.sort_values(by="#", ascending=False)
print(f'\nMínimo {status} [{min(freq_info[status])}]'
      f'\nMáximo {status} [{max(freq_info[status])}]'
      f'\nMáxima frequencia [{maxf.iloc[0,1]}],'
      f'{status} = {maxf.iloc[0,0]}')

fig, ax = plt.subplots(1, 2)
ax[0].bar(freq.index, freq['#'])
# a função do plt.hist já faz o trabalho de calcular as frequências
# mas apesar de agrupar os dados e tornar a vizualização mais simples
# os dados desta forma dificultam encontrar a maior frequência e o
# menor e maior no ranking de stats
ax[1].hist(df[status], bins=20)
plt.show()

