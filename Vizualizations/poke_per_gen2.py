import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='darkgrid')

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')
fig, ax = plt.subplots()
t = sns.histplot(data=df,x='Generation',hue='Generation',ax=ax)

plt.show()
