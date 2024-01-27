import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tools import P, show_df_info, show_nav, show_cav, show_corr

sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']

show_df_info(sales)

P('--' * 40, 'purple')

# Show Numerical & Categorical & Correlation analysis
show_nav(sales, 'Revenue_per_Age')
show_cav(sales, 'Age_Group')
show_corr(sales)

# Show descriptive statistics
print(sales.loc[sales['Country'] == 'France', 'Revenue'].describe())
