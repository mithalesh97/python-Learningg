#this section covers the np.zeros() , np.empty(), np.arrange(), np.linspace()
import numpy as np

array = np.zeros(5)
print(array)

b = np.ones(10)
print(b)

c = np.empty(4)
print(c)

#create an array with a range of elements
#syntax: np.arrange(start , stop , step(spacing or gap))
d = np.arange(5,105,5)
print(d)

#syntax: np.linspace(start , stop , split value)

e = np.linspace(2,9,num = 4, endpoint = False)
print(e)

#default data type in the array is floating point, you have 
#explictly change it to the dtype keyword
x = np.ones(3, dtype = np.int64)
print(x)
