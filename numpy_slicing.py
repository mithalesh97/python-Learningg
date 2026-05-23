import numpy as np
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#slicing syntax: array[row_start:row_end, column_start:column_end]
print(array[0:4, 0:4]) #prints the whole array
print(array[0:2, 0:2]) #prints the top left 2x2 subarray
print(array[2:4, 2:4]) #prints the bottom right 2x2 subarray
print(array[1:3, 1:3]) #prints the middle 2x2 subarray
print(array[0:4, 1:3]) #prints the middle two columns of the whole array

print("this is the same as the previous line")
#slicing with step
print(array[0:4:2, 0:4:2]) #prints every other row and column, resulting in a 2x2 subarray
print(array[0:4:2, 1:4:2]) #prints every other row and every other column starting from the second column, resulting in a 2x2 subarray
print(array[1:4:2, 0:4:2]) #prints every other row starting from the second row and every other column, resulting in a 2x2 subarray
