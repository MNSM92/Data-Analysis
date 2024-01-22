import numpy as np

from tools import P, show_ii, show_nav, show_cav, show_corr

P(np.__version__, 'purple')

# Create a numpy array of size 10, filled with zeros.
a = np.zeros(10)
P(a, 'green')

# Create a numpy array with values ranging from 10 to 49
# Create a numpy array with the odd numbers
# Create a numpy array with numbers from 1 to 10, in descending order.
a = np.arange(10, 50)
P(a, 'green')
a = np.arange(10, 50, 2)    
P(a, 'green')
a = np.arange(50, 10)[::-1]
P(a, 'green')


# Create a numpy matrix of 2*2 integers, filled with ones.
# Create a numpy matrix of 4*4 integers, filled with fives.
a = np.ones((2, 2))
b = np.ones((4, 4)) * 5
P(a, 'green')

# Create a numpy matrix of 3*2 float numbers, filled with ones.
a = np.ones([3, 2], dtype=float)
P(a, 'green')

# Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.
# Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens.
X = np.array([[1, 2], [3, 4]])
a = np.ones_like(X)
b = np.zeros_like(X)
c = np.full_like(X, 7)
c = np.full(X.shape, 7)
c = a * 7
P(a, 'green')
P(b, 'green')

# Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere.
a = np.eye(3)
a = np.identity(3)
P(a, 'green')

# Create a numpy array, filled with 3 random integer values between 1 and 10.
a = np.random.randint(1, 11, size=3)
P(a, 'green')

# Create a 3*3*3 numpy matrix, filled with random float values.
a = np.random.rand(3, 3, 3)
P(a, 'green')

# Given the X python list convert it to an Y numpy array
X = [1, 2, 3, 4, 5]
Y = np.array(X)
P(Y, 'green')
P(type(Y), 'green')

# Create a 3*3 numpy matrix, filled with values ranging from 0 to 8
matrix = np.arange(9).reshape(3, 3)
P(matrix, 'green')

# Show the memory size of the given Z numpy matrix
Z = np.arange(10000)
P(Z.size * Z.itemsize, 'green')

# Given the X numpy array, show the elements in an odd position
X = np.array([1, 2, 3, 4, 5])
P(X[::2], 'green')

# Given the X numpy array, make a mask showing negative elements
X = np.array([-1, -2, 1, 2, 3, -4])
mask = X < 0
P(mask, 'green')
P(X[mask], 'green')

# Given the X numpy array, return True if none of its elements is zero
X = np.array([-1, -2, 1, 2, 3, -4])
P(not any(X), 'green')

# # remember: axis=0 columns; axis=1 rows
X = np.array([[1, 2], [3, 4], [5, 6]])
P(X.sum(axis=0), 'green')
P(X.sum(axis=1), 'green')