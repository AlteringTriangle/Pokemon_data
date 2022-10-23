import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon.csv')
poMask = df[(df['Total'] <= 600) | ((df['Total'] > 600) & (df['Legendary'] == False))]  # Poke One Mask
wmfMask = poMask.drop_duplicates(keep='first', subset='#')  # without mega and forms
df = df

num = 130
stat = 'attack'.capitalize()
print(df[['Name', 'Total', stat, 'Legendary']].loc[df[stat] >= num])
