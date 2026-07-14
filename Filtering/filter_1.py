import pandas as pd

df = pd.read_csv("stock.csv")

# print(df.to_string())

# bull_stock = df[df["Diff %"] == 6.15]

df["Open"] = df["Open"].str.replace(",", "")
df["Open"] = pd.to_numeric(df["Open"])
check_open = df[df["Open"] <=400.00]

# print(bull_stock)

print(check_open.to_string())