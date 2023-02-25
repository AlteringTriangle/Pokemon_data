import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Pokemon.filtering_data.finalFormOnly import raw1

df = pd.read_csv('..\\pokemon.csv')
df = df.loc[raw1]

fig = plt.subplot()
a = sns.scatterplot(data=df, x='#', y='Total',hue='Generation',palette='Set2')
a.grid()

plt.show()