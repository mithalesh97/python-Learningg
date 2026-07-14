import pandas as pd

df = pd.read_csv("currency.csv", index_col="Name")

#Selection by column
#print(df["Name"].to_string())
# print(df["Symbol"].to_string())
# print(df["Code"].to_string())
# print(df[["Code","Symbol","Name"]].to_string())

#selection by Row/s
#print(df.loc[120]) #accessing by default index
#but we can't remember the integer to select 
#so we put name as an index
# print(df.loc["Nepalese rupee":"Tunisian dinar",["Code"]])

# print(df.iloc[0:11:2, 0:2])

#lets search currency
currencyy = input("Enter currency name: ")

try:
    print(df.loc[currencyy])

except KeyError:
    print(f"{currencyy } not found! ")