import pandas as pd

#aggregate functions = Reduces a set of values into a
#                      single summary value used to summarize
#                      and analyze data often used with 
#                      the groupby() function

df = pd.read_csv("data.csv")

#for whole data frame
#print(df.mean(numeric_only = True))

# highest = df.loc[df["Diff %"].idxmax()]
# print(highest[["Symbol", "Diff %"]])

#print(df.sum(numeric_only = True))
# print(df.min(numeric_only = True))
# print(df.max(numeric_only = True))
# print(df.count())

#for single column like "Turnover"
# df["Turnover"] = pd.to_numeric(
#     df["Turnover"].str.replace(",", ""),
#     errors="coerce")
# print(df["Turnover"].mean())
# print(df["Turnover"].sum())
# print(df["Turnover"].min())
# print(df["Turnover"].max())
# print(df["Turnover"].count())

#for grouping
group = df.groupby("Type1")
# print(group["Height"].sum())
print(group["Height"].max())
print(group["Height"].count())