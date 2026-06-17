import numpy as np

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

#shape of the array
print(a.shape) #prints (3,3) which means 3 rows and 3 columns
print(a.ndim)
print(len(a.shape))  # == ndim
print(a.size)
print(a.dtype)