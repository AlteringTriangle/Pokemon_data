import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")

# works better with dash

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')

typ = 'Water'
stat = 'Attack'

fil_tro = (df['Type 1'] == typ) | (df['Type 2'] == typ)
df = df.loc[fil_tro].sort_values(by=stat,ascending=False)
data = df.head(20)
data['#'] = data['#'].astype('str')

fig, ax = plt.subplots()
ax.set_title(f'{typ} pokemons; ranked by {stat}')
sns.scatterplot(data=data, x='#', y=stat,ax=ax)
plt.show()







