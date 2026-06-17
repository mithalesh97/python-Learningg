import numpy as np
# rng = np.random.default_rng()

# # Single integer between 0 and 9
# print(rng.integers(0, 10)) 

# # 1D array of 5 integers between 10 and 49
# print(rng.integers(10, 50, size=5)) 

# # 2D array (3x3 matrix) of integers between 1 and 6
# print(rng.integers(1, 7, size=(3, 3))) 

#for floating point numbers
#print(np.random.uniform(low = -10,high =10,size= (3,4)))

#shuffle the array
rng = np.random.default_rng()

fruits = np.array(["🍎","🍊","🍌","🥥","🍍"])
fruit = rng.choice(fruits,size = (4,2))
print(fruit)
# array = np.array([1,2,3,4,5])
# rng.shuffle(array)
# print(array)
