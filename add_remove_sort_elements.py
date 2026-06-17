#broadcasting allows numpy to perform operations on arrays
#with different shapes by virtually expanding dimensions
#so they match the larger array's shape.

#the dimensions have the same size
#OR
#One of the dimensions has a size of 1.

import numpy as np

a1 = np.array([[1,3,4,4],[3,4,5,6],[2,3,4,4],[7,8,9,0],[6,5,4,3]])
a2 = np.array([[1],[2],[3],[4],[5]])

print(a1.shape)
print(a2.shape)

print(a1*a2)