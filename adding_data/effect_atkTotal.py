import pandas as pd


def stringHead(data, n=8):
    return print(data.head(n).to_string())


df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')
t = df['Sp. Atk'] - df['Attack']

higher_atk = df['Attack'].loc[t <= 0]
higher_spatk = df['Sp. Atk'].loc[t > 0]
low_atk = df['Attack'].loc[t >= 0]
low_spatk = df['Sp. Atk'].loc[t < 0]

effective_atk = pd.concat([higher_atk, higher_spatk])
lower_atk = pd.concat([low_atk, low_spatk])

df['Lower Atk'] = lower_atk
df['Effective Atk'] = effective_atk

effective_total = df[['HP','Defense','Sp. Def','Speed','Effective Atk']].sum(axis=1)
df['Effective Total'] = effective_total
total_check = df['Effective Total'] + df['Lower Atk']

if __name__ == '__main__':
    print(df.to_string())
    print(df.loc[df['#'] == 555].to_string())
    print('Total Check == Total ?')
    print((total_check == df['Total']).all())
    if input('save?') == 'save':
        ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv')
        ac[['Effective Atk', 'Effective Total']] = df[['Effective Atk','Effective Total']]
        ac.to_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv', index=False)
        print('saved')
