import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='darkgrid')

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')
df = df[['#', 'Generation']].groupby('Generation').count().reset_index()
fig, ax = plt.subplots()

sns.barplot(data=df, y='#', x='Generation',ax=ax)
ax.set_label


plt.show()

