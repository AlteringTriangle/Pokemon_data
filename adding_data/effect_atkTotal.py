import pandas as pd
from Pokemon.dataPath import datapath


def stringHead(data, n=8):
    return print(data.head(n).to_string())

# parte 1 carregando dados
df = pd.read_csv(datapath)

# parte 2 modificando os dados

# para saber qual o tipo de atk mais forte, um é subtraido do outro
t = df['Sp. Atk'] - df['Attack']
# portanto t é um dataframe do qual contém numeros positivos, onde sp atk é maior
# e números negativos onde atk é maior

# quando attack for maior, ou seja t <= 0, a coluna de ataque efetivo ganhará o valor
# de atk
higher_atk = df['Attack'].loc[t <= 0]
# E quando sp atk for maior, t > 0, de sp atk
higher_spatk = df['Sp. Atk'].loc[t > 0]

# Para criar o total efeitvo, precisamos somar todos os status, exceto o atk menor
# ou podemos criar uma coluna do atk menor, e subtrai-la do total atual
low_atk = df['Attack'].loc[t >= 0]
low_spatk = df['Sp. Atk'].loc[t < 0]

# A coluna de atk efeivo então será a concatenação de dos maiores ataques
# Por serem complementares, ou seja, se o atk é maior, o sp atk não é naquela linha e vice-versa
# elas completam os indices que estão faltando um no outro
effective_atk = pd.concat([higher_atk, higher_spatk])
# Análogo para o ataque menor, só que agora com os menores ataques
lower_atk = pd.concat([low_atk, low_spatk])

# dessa forma as colunas podem ser adicionadas como
df['Lower Atk'] = lower_atk
df['Effective Atk'] = effective_atk
effective_total = df[['HP','Defense','Sp. Def','Speed','Effective Atk']].sum(axis=1)
df['Effective Total'] = effective_total
# total check é uma verificação se o valor de effective total tem significado, por isso ele
# é feito duas vezes e comparado
total_check = df['Effective Total'] + df['Lower Atk']

if __name__ == '__main__':
    # verificação de salvamento
    if input('save?') == 'save':
        ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv')
        ac[['Effective Atk', 'Effective Total']] = df[['Effective Atk','Effective Total']]
        ac.to_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv', index=False)
        print('saved')
