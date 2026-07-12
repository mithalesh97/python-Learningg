import pandas as pd

age = {"milan" : 21,"prasiddhi" : 20 , "angad":24}

series = pd.Series(age)


#update the values
series.loc["angad"] -= 2
print(series)

