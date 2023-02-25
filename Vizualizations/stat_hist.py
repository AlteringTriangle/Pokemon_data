import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')


fig,ax = plt.subplots(2,2)

sns.histplot(data=df,x='Total',bins=200,kde=True,ax=ax[0,1])

sns.histplot(data=df,x='Total',bins=30,kde=True, ax=ax[1,1])

sns.histplot(data=df,x='Total',bins=30,kde=True, ax=ax[1,0], cumulative=True)
plt.show()






