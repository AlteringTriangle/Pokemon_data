import pandas as pd
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)

raw = ~df['Name'].str.contains('Forme|Unbound| Size| Kyurem|Zen Mode|'
                               ' Rotom|Sandy Cloak|Trash Cloark|Primal')

# alguns pokemon tem formas bases explicitas, então devem haver exeções
exception = df.loc[[428, 750, 751, 716, 715, 713, 714, 544, 784, 780,
                    545, 550, 551, 702, 703, 704, 705, 708, 709]]
raw_e = exception['Name'] == exception['Name']
raw_f = pd.Series(True, index=exception.index)

# adding exception to the raw filter
raw = raw | raw_e

wfMask = df.loc[raw]

