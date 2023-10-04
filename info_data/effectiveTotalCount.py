import pandas as pd
import matplotlib.pyplot as plt
from Pokemon.dataPath import datapath, addcolpath

df = pd.read_csv(datapath)
ac = pd.read_csv(addcolpath, usecols=['Effective Total'])
df['Effective Total'] = ac
df['Count'] = 0
# effective total count
etc = df[["Effective Total","Count"]].groupby('Effective Total').count()

print(etc)


def edit_ax(axs,_xlabel,_ylabel, grid=True):
    axs.grid(True)
    #axs.legend()
    axs.set_xlabel(_xlabel)
    axs.set_ylabel(_ylabel)
    #axs.label_outer()


fig, axs = plt.subplots(1, 2, tight_layout=True)


axs[0].hist(df['Effective Total'])
edit_ax(axs[0], "Total Efetivo","Numero de ocorrências")

axs[1].hist(df['Effective Total'], bins=50)
edit_ax(axs[1], "Total Efetivo","Numero de ocorrências")


plt.show()

