#Filtering = Refers to the process 
# of selecting elements
#from an array that match a given condition

import numpy as np
ages = np.array([[21,14,25,36,63,47],
                 [78,54,16,18,37,99]])

teenagers = ages[ages<20]
adults = ages[(ages>=18) & (ages<=65)]
seniors = ages[ages>=65]
evens = ages[ages%2==0]

#where function use np.where(condition,value_if_true,value_if_false)
#keep the original shape of the array
adul = np.where(ages>40,ages,0)
print(adul)