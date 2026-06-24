#data frame = a tabular data structure with rows and columns. (2-dimensional) 
#similar to an excel spreadsheet

import pandas as pd

#dictionary
data = {"Name":["Milan","Prasiddhi","PK sharma"],
        "Age": [21,22,20]
        }

# df = pd.DataFrame(data)
# print(df)

#custom indexing
df1 = pd.DataFrame(data, index =['student 1', 'student 2', 'student 3'])

#to print output value by label using loc
# print(df1.loc["student 2"])  #by using integer properties use iloc
# print(df1.iloc[2])

#add a new column
df1["Language"] = ["Maithili" , "Newari" , "Nepali"]

#add new row  and also we can add multiple rows by just adding dictionary in new_row list
new_row = pd.DataFrame([{"Name":"Asmita", "Age": 23 ,"Language":"English" }],index = ['student 4'])

#now concatenate it
df1 = pd.concat([df1,new_row])
print(df1)