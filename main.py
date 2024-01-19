import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tools import P, show_ii, show_nav, show_cav, show_corr

sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

# Calculate revenue per age
sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']

# Show information about the data
show_ii(sales)

P('--' * 40, 'purple')

# Show Numerical analysis and visualization of the data
show_nav(sales, 'Revenue_per_Age')

# Show Categorical analysis and visualization of the data
show_cav(sales, 'Age_Group')

# Show Correlation analysis
show_corr(sales)

# Show descriptive statistics
print(sales.loc[sales['Country'] == 'France', 'Revenue'].describe())
