import numpy as np
import pandas as pd
from tools import P

P(pd.__version__, 'purple')

# Create an empty pandas Series
a = pd.Series()
P(a, 'green')

# Given the X python list convert it to an Y pandas Series
X = [1, 2, 3, 4, 5]
Y = pd.Series(X)
P(Y, 'green')

# Given the X pandas Series, name it 'My letters'
X = pd.Series(['a', 'b', 'c', 'd', 'e'])
X.name = 'My letters'
P(X, 'purple')

# Given the X pandas Series, show its values
P(X.values, 'red')

# Assign index names to the given X pandas Series
X.index = ['A', 'B', 'C', 'D', 'E']
P(X, 'purple')

# Given the X pandas Series, show its first element
P(X[0], 'green')
P(X.iloc[0], 'green')

# Given the X pandas Series, show its last element
P(X[-1], 'green')
P(X.iloc[-1], 'green')

# Given the X pandas Series, show its first 3 elements
P(X[:3], 'green')

# Convert the given integer pandas Series to float
X = pd.Series([1, 2, 3, 4, 5])
X = X.astype(float)
P(X, 'green')