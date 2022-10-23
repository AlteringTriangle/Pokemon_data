import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('..\\pokemon.csv')
tt = pd.read_csv('..\\added_cols.csv', usecols=['Total Tier','Base Form'])
df[tt.columns] = tt

fig, ax = plt.subplots(1,2)
# full dist
full_dist = df[['#','Total Tier']].groupby('Total Tier').count()
full_dist = full_dist.loc[full_dist.index[:-2].sort_values(ascending=False).append(full_dist.index[-2:])]

ax[0].grid()
sns.barplot(x=full_dist.index, y=full_dist['#'], ax=ax[0])
ax[0].set_yticks(np.arange(0, 161, 20))
ax[0].set_title('Full tier distribuition')


# wmf dist
wmfMask = df.drop_duplicates(keep='first', subset='#')
wmf_dist = wmfMask[['#','Total Tier']].groupby('Total Tier').count()
wmf_dist = wmf_dist.loc[wmf_dist.index[:-2].sort_values(ascending=False).append(wmf_dist.index[-2:])]

ax[1].grid()
sns.barplot(x=wmf_dist.index, y=wmf_dist['#'], ax=ax[1])
ax[1].set_yticks(np.arange(0, 161, 20))
ax[1].set_title('Without mega/forms distribuition')


# gen 1 ff only

# ff dist
fig, ax = plt.subplots(1,2)

ffMask = df.drop_duplicates(keep='last', subset='Base Form').reset_index(drop=True)  # FF -> Final Forms
ff_dist = ffMask[['#','Total Tier']].groupby('Total Tier').count()
ff_dist = ff_dist.loc[ff_dist.index[:-2].sort_values(ascending=False).append(ff_dist.index[-2:])]

ax[0].grid()
sns.barplot(x=ff_dist.index, y=ff_dist['#'], ax=ax[0])
ax[0].set_yticks(np.arange(0, 36, 5))
ax[0].set_title('final forms')

# wmf ff
wmfMask = df.drop_duplicates(keep='first', subset='#')  # WMF -> without mega and forms
wmf_ff_mask = wmfMask.drop_duplicates(keep='last', subset='Base Form').reset_index(drop=True)  # FF -> Final Forms
wmf_ff_dist = wmf_ff_mask[['#','Total Tier']].groupby('Total Tier').count()
wmf_ff_dist = wmf_ff_dist.loc[wmf_ff_dist.index[:-2].sort_values(ascending=False).append(wmf_ff_dist.index[-2:])]

ax[1].grid()
sns.barplot(x=wmf_ff_dist.index, y=wmf_ff_dist['#'], ax=ax[1])
ax[1].set_yticks(np.arange(0, 36, 5))
ax[1].set_title('final forms without mega')

plt.show()
