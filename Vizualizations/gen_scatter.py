import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Pokemon.filtering_data.finalFormOnly import raw1, raw2
from Pokemon.filtering_data.removeLegendaries import raw as legendary_off

df = pd.read_csv('..\\pokemon.csv')
# raw1 -> formas finais incluindo mega evoluções
# raw2 -> formas finais sem mega evoluções
# legendary_off desconsidera os pokemons lendários
# raw1 e raw2 não podem ser misturados booleanamente pois perderemos dados das formas
# anteriores dos pokemons
df = df.loc[raw1 & legendary_off]

fig = plt.subplot()
# distribuição de stats por geração
a = sns.scatterplot(data=df, x='#', y='Total',hue='Generation',palette='Set2')
a.grid()

plt.show()