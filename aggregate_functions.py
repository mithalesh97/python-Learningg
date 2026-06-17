#aggregate functions = summarize data and typically return a single value

#basically doing statistics on the array

import numpy as np
a = np.array([[1,2,3,4],
             [2,3,4,5]])

print(np.sum(a))
print(np.mean(a))
print(np.std(a))  #standard deviation
print(np.var(a))  #variance
print(np.min(a))  #minimum
print(np.max(a))  #maximum

#position of the minimum value
print(np.argmin(a))
#position of the max value
print(np.argmax(a))

#to sum the column of an array
print(np.sum(a,axis=0))
#sum of the row of an array
print(np.sum(a,axis=1))
