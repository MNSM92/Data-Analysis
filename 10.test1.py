import numpy as numpy as np

def mean_var_std(arr):

    # convert the array into 3*3 matrix
    arr = numpy.array(arr).reshape(3, 3)

    '''
    return
    {
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}

    '''

    mean = np.mean(arr, axis=1, keepdims=True)
    var = np.var(arr, axis=1, keepdims=True)
    std = np.std(arr, axis=1, keepdims=True)

    return mean, var, std

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))