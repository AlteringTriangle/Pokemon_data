import pandas as pd

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')
ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv', usecols=['Effective Total'])
df['Effective Total'] = ac
df['Count'] = 0
# effective total count
etc = df[["Effective Total","Count"]].groupby('Effective Total').count()

print(etc)



