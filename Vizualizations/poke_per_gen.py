import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Pokemon.filtering_data.removeMegaNForms import raw as mask
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)
df = df.loc[mask]
df = df[['#', 'Generation']].groupby('Generation').count().reset_index()

fig, ax = plt.subplots(facecolor='#bbb')
sns.barplot(data=df, y='#', x='Generation', ax=ax, palette='viridis')

# para plots com hue, cada container deve ser preenchido separadamente
for i in ax.containers:
    ax.bar_label(i,)

# ax.bar_label(ax.containers[0]) # sem palette funciona para o primeiro exemplo,
# com palette um hue é implicitamente introduzido


plt.bar_label()

plt.show()

