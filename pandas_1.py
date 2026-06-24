import pandas as pd

#series = A pandas is a 1 -Dimensional labeled array that can hold any data type
#Think of it like a single column in a spreadsheet (1-Dimensional)

data = [10,12,14,16]

series = pd.Series(data)

#all index can be set as you like
series1 = pd.Series(data, index = ['a','b','c','d'])
# print(series)
# print(series1)

# #to access the values'location by the label
# print(series1.loc['c'])

# #to changes the value of that label we use
# #also add the value by creating new label and value
# series1.loc['d']= 20
# print(series1)
# series.loc['4'] = 34
# print(series)

# # I can locate the values using integer  iloc
#print(series.iloc[3])

#find mean
#print(series1.mean())

# #this is to print output which is greater elements in the column
print(series1[series1 >= 15])