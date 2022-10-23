import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('pokemon.csv')
plus = pd.read_csv('added_cols.csv', usecols=['Base Form']).dropna()
df['Base Form'] = plus

wmfMask = df.drop_duplicates(keep='first', subset='#')  # without mega and forms
box_1 = wmfMask.copy().loc[:, ['Name', '#', 'Total', 'HP', 'Attack', 'Defense',
                      'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Base Form']]

box_1 = box_1.head(12)
sns.barplot(x='Name', y='Total', hue='Base Form', data=box_1)
plt.show()
