import pandas as pd
from Pokemon.dataPath import datapath, addcolpath
"""
Média entre tipos duplos, um pokemon que pertence tanto aos tipos grass
e poison mudará a categoria específica grass/poison
"""

df = pd.read_csv(datapath)
ac = pd.read_csv(addcolpath, usecols=['MultiType'])

# a coluna multi-type é adiciona e uma coluna especial de valor sempre 1 é criada para
# poder contar a frequência das ocorrencias
df['MT'] = ac
df['Count'] = 1

# Apenas os valores numéricos, agrupando pelo tipo multiplo em comum, é feito uma média
mdt = df.groupby('MT').mean(numeric_only=True)
# arredonda para 1 casa decimal
mdt = round(mdt, 1)
# exclui colunas com informações sem significado
mdt.drop(['#', 'Generation'],axis=1, inplace=True)
print(mdt.to_string())


