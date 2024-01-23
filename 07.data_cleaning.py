import numpy as np
import pandas as pd
from tools import P

# Create an empty numpy array
falsy_values = np.array([1, 2, 3, np.nan, np.inf, 4])
a = falsy_values[~np.isnan(falsy_values)]
print(np.isnan(a))

