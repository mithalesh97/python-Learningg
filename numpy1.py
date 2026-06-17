import numpy as np

a = np.array([1,2,3])   #1d array
b = np.array([[1,2],[3,4]])   #2d array
c = np.array([[[0,1],[2,3]],
              [[4,5],[6,7]],
              [[8,9],[10,11]]])

print(c)
print(c.ndim)  #n dimension of arrays
print(c.shape)  # layers , row and colum of that arrays in the form of tuples
#print(c[2,0,0])  #multidimensional indexing

#creating my phone number using the indexing
num = str(c[2,0,1]) + str(c[1,1,1]) + str(c[0,0,0]) + str(c[0,1,0]) + str(c[1,0,1]) + str(c[1,0,1]) + str(c[0,0,0]) + str(c[2,0,0]) + str(c[1,1,1]) + str(c[2,0,1])
print(num)
