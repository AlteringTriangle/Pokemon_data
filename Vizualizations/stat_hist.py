import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)
stat = 'Speed'

fig, ax = plt.subplots(2, 2, facecolor='#bbb')

# distribuição do stat através das gerações de pokemon
sns.scatterplot(data=df, x='#', y=stat, hue='Generation', ax=ax[0, 0], palette='Set2')

# histograma com muitos pinos
sns.histplot(data=df, x=stat, bins=60, kde=True, ax=ax[0, 1])

# histograma comum
sns.histplot(data=df, x=stat, bins=30, kde=True, ax=ax[1, 1])

# histograma cumulativo com label y em porcentagem
sns.histplot(data=df, x=stat, bins=30, kde=True, ax=ax[1, 0], cumulative=True, stat='percent')
ax[1, 0].grid(True)
plt.show()
