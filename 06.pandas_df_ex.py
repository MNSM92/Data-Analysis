import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tools import P

P(pd.__version__, 'purple')

# Create an empty pandas DataFrame
df = pd.DataFrame()
P(df, 'green')

# Create a marvel_df pandas DataFrame with the given marvel data
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]

marvel_df = pd.DataFrame(marvel_data)
P(marvel_df, 'green')

# Add column names to the marvel_df
marvel_df.columns = ['name', 'sex', 'first_appearance']
P(marvel_df, 'purple')

# Add index names to the marvel_df (use the character name as index)
marvel_df.index = marvel_df['name']
P(marvel_df, 'blue')

# Drop the name column as it's now the index
marvel_df = marvel_df.drop(columns=['name'])
P(marvel_df, 'yellow')

# Drop 'Namor' and 'Hank Pym' rows
marvel_df = marvel_df.drop(index=['Namor', 'Hank Pym'])
P(marvel_df, 'white')

# Show the first 5 elements on marvel_df
marvel_df = marvel_df.head()
marvel_df = marvel_df.loc[['Spider-Man', 'Captain America', 'Wolverine', 'Iron Man', 'Thor'], :]
marvel_df = marvel_df.loc['Spider-Man': 'Thor', :]
marvel_df = marvel_df.iloc[0:5, :]
marvel_df = marvel_df.iloc[0:5,]
marvel_df = marvel_df.iloc[:5,]
P(marvel_df, 'green')

# Show just the sex of the first 5 elements on marvel_df
marvel_df = marvel_df['sex'].to_frame()
P(marvel_df, 'purple')

# Show the first and last elements on marvel_df
marvel_df = marvel_df.iloc[[0, -1]]
P(marvel_df, 'purple')

# Given the marvel_df pandas DataFrame, make a mask showing the female characters
mask = marvel_df['sex'] == 'female'
P(mask, 'purple')

# Given the marvel_df pandas DataFrame, make a mask showing the female characters
mask = marvel_df['sex'] == 'female'
marvel_df = marvel_df[mask]
P(marvel_df, 'purple')