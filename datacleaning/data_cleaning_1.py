import pandas as pd

#data cleaning = the process of fixing/removing: incomplete, incorrect, or irrelevant data. ~75% of work done with pandas is data cleaning

df = pd.read_csv("data.csv")

#1. Drop irrelevant columns
#print(df.drop(columns=["Legendary"]))

#2. Handle missing data
#df = df.dropna(subset=["Type2"])

#or replace the not available na with other
# df = df.fillna({"Type2" : "None"})
# print(df.to_string())

#3 . Fix incosistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire": "FIRE",
#                                    "Water": "WATER"})

# print(df.to_string())

#4. Standardize text
# df["Name"] = df["Name"].str.lower()

# print(df.to_string())

# 5. Fix data types
# df["Legendary"]  = df["Legendary"].astype(bool)
# print(df.to_string())

#6. Remove duplicate values
df = df.drop_duplicates()
print(df)