import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)

typ = 'Water'
stat = 'Attack'

# de nada adianta ranquear apenas os tipo 1, sem carregar os tipo 2 juntos
# como um pokemon só é de um tipo uma vez, ele deve ser de water no 1 ou no 2
# ou não será do tipo agua
fil_tro = (df['Type 1'] == typ) | (df['Type 2'] == typ)
# como queremos um ranque de um stat específico, iremos organizar com base nesse stat
df = df.loc[fil_tro].sort_values(by=stat, ascending=False)
# e pegar apenas os maiores valores para o ranking
data = df.head(20)

fig, ax = plt.subplots()
# como megaevoluções, como Gyaradosmega Gyarados tem nomes beeem longos,
# é necessário ajustar as margens e escrever o nome dos pokemons na diagonal
fig.subplots_adjust(left=0.125, right=0.9, top=0.9, bottom=0.235)
plt.xticks(rotation=45, ha="right")
ax.set_title(f'{typ} pokemons; ranked by {stat}')
sns.scatterplot(data=data, x='Name', y=stat, ax=ax)
plt.show()







