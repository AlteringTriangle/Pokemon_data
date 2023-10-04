import pandas as pd
from Pokemon.dataPath import datapath

df = pd.read_csv(datapath)

# apenas uma vizualização dos dados sendo utilizados
print(df)