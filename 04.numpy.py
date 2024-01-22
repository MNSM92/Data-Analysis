import sys
import numpy as np
from tools import P

# create a numpy array
a = np.arange(5)
P(f'This is an array: {a}', 'white')

# create an array with randint
a = np.random.randint(10, size=6)
P(f'This is a random array: {a}', 'white')

# create a numpy array
a = np.array([1, 2, 3, 4])
P(f'This is an array: {a}', 'white')

# create a subset of array
a = np.array([1, 2, 3, 4])
P(f'This is a subset of array: {a[1:3]}', 'white')

# Array Types
P(f'This is an array of type: {a.dtype}', 'blue')

# change the data type
a = a.astype('float64')
P(f'This is an array of type: {a.dtype}', 'red')

# shape, dimension and size
P(f'This is shape: {a.shape}', 'green')
P(f'This is dimension: {a.ndim}', 'purple')
P(f'This is size: {a.size}', 'yellow')

# sum, mean, std and var
P(f'This is sum: {a.sum()}', 'cyan')
P(f'This is mean: {a.mean()}', 'cyan')
P(f'This is std: {a.std()}', 'cyan')
P(f'This is var: {a.var()}', 'cyan')

# create a 2D array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
P(f'This is a 2D array: {a}', 'white')

# sum, mean, std and var with axis
P(f'This is sum: {a.sum(axis=1)}', 'blue')
P(f'This is mean: {a.mean(axis=0)}', 'blue')
P(f'This is std: {a.std(axis=1)}', 'blue')
P(f'This is var: {a.var(axis=0)}', 'blue')

# Broadcasting and Vectorized operations
P(f'This is a: {a}', 'red')
P(f'This is a + 1: {a + 1}', 'green')
P(f'This is a * 2: {a * 2}', 'yellow')


# filter array
a = np.array([1, 2, 3, 4, 5, 6, 7])
P(f'This is a: {a}', 'red')
P(f'This is a > 2: {a > 2}', 'green')
P(f'This is a[a > 2]: {a[a > 2]}', 'yellow')

# Linear Algebra
P(f'This is a: {a}', 'red')
P(f'This is a.T: {a.T}', 'green')
P(f'This is np.dot(a, a.T): {np.dot(a, a.T)}', 'yellow')

# Size of objects in Memory
a_size = sys.getsizeof(a)
print(f"The size of 'a' array is: {a_size} bytes")

element_size = a.itemsize
print(f"The size of each element in 'a' array is: {element_size} bytes")

total_size = a_size - a.nbytes
print(f"The total size of 'a' array elements is: {total_size} bytes")

# Useful Numpy functions
# random, arrange, reshape, linspace, zeros. ones, empty, identity and eye


