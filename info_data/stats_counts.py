import pandas as pd

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')

stats = ['Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']
# total counts
# a coluna '#' está sendo usada apenas como placeholder
tc = df[['#','Total']].groupby('Total').count().reset_index()
hc = df[['#','HP']].groupby('HP').count().reset_index()
ac = df[['#','Attack']].groupby('Attack').count().reset_index()
dc = df[['#','Defense']].groupby('Defense').count().reset_index()
sac = df[['#','Sp. Atk']].groupby('Sp. Atk').count().reset_index()
sdc = df[['#','Sp. Def']].groupby('Sp. Def').count().reset_index()
sc = df[['#','Speed']].groupby('Speed').count().reset_index()
print(hc.values)
# valueble info
# total range
tr = f'{tc.values[0, 0]}->{tc.values[-1, 0]}'
hr = f'{hc.values[0, 0]}->{hc.values[-1, 0]}'
ar = f'{ac.values[0, 0]}->{ac.values[-1, 0]}'
dr = f'{dc.values[0, 0]}->{dc.values[-1, 0]}'
sar = f'{sac.values[0, 0]}->{sac.values[-1, 0]}'
sdr = f'{sdc.values[0, 0]}->{sdc.values[-1, 0]}'
sr = f'{sc.values[0, 0]}->{sc.values[-1, 0]}'

print(tr)
print(hr)
print(ar)
print(dr)
print(sar)
print(sdr)
print(sr)


'''
190->780
10->255
10->190
10->230
15->194
23->230
10->180
'''