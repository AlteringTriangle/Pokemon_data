import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('..\\pokemon.csv')
tt = pd.read_csv('..\\added_cols.csv', usecols=['Total Tier','Base Form'])
df[tt.columns] = tt

fig, ax = plt.subplots(1, 2, facecolor='#bbb')
# full dist
full_dist = df[['#','Total Tier']].groupby('Total Tier').count()
# sort deixará os valores que são categóricos em ordem alfabética, entretanto, [s] e [ss] já
# estão nas suas posições certas e ficaram atrás de F de organizados juntos das outras categorias
# portanto elas são removidas na hora de organizar e recolocadas no final
full_dist = full_dist.loc[full_dist.index[:-2].sort_values(ascending=False).append(full_dist.index[-2:])]

ax[0].grid()
sns.barplot(x=full_dist.index, y=full_dist['#'], ax=ax[0], hue=full_dist.index, palette='viridis')
ax[0].set_yticks(np.arange(0, 161, 20))
ax[0].set_title('Full tier distribuition')

for i in ax[0].containers:
    ax[0].bar_label(i,)


# wmf dist
wmfMask = df.drop_duplicates(keep='first', subset='#')
wmf_dist = wmfMask[['#','Total Tier']].groupby('Total Tier').count()
wmf_dist = wmf_dist.loc[wmf_dist.index[:-2].sort_values(ascending=False).append(wmf_dist.index[-2:])]

ax[1].grid()
sns.barplot(x=wmf_dist.index, y=wmf_dist['#'], ax=ax[1], hue=wmf_dist.index, palette='rocket')
ax[1].set_yticks(np.arange(0, 161, 20))
ax[1].set_title('Without mega/forms distribuition')

for i2 in ax[1].containers:
    ax[1].bar_label(i2,)


plt.show()
