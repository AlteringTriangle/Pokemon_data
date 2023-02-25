import pandas as pd

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')


df['Count'] = 0
# total count
tc = df[['Total','Count']].groupby(['Total']).count()
print(tc)
