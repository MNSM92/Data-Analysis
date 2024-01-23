import pandas as pd
import numpy as np
from tools import P

# Create a pandas series
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
g7_pop.name = 'G7 Population in millions'
P(g7_pop.index, 'red')
P(g7_pop.values, 'green')

# Create a pandas dataframe
g7_pop_dict = {'Canada': 35.467, 'France': 63.951, 'Germany': 80.940, 'Italy': 60.665, 'Japan': 127.061, 'United Kingdom': 64.511, 'United States': 318.523}
g7_pop = pd.Series(g7_pop_dict)
P(g7_pop.index, 'purple')
P(g7_pop.values, 'blue')

# Create a pandas dataframe
a = g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)]
P(a, 'yellow')

# use iloc
a = g7_pop.iloc[0]
P(a, 'green')
