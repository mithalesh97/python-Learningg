import pandas as pd

#to read csv file
df = pd.read_csv("currency.csv")

print(df.to_string()) #to_string() to print all data in csv and json

#to read json file
df1 = pd.read_json("currency.json")
print(df1.to_string())