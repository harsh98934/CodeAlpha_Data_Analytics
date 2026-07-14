import pandas as pd


df = pd.read_csv("books.csv")

print(df.head())

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nData Types")
print(df.dtypes)

print("\nShape of Dataset")
print(df.shape)

print("\nColumn Names")
print(df.columns)


df["Price"] = df["Price"].str.extract(r"([\d.]+)")
df["Price"] = df["Price"].astype(float)

df["Availability"] = df["Availability"].str.strip()

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())


print("\nStatistical Summary")
print(df.describe())




print("\nAverage Price:")
print(df["Price"].mean())


print("\nMost Expensive Book:")
print(df.loc[df["Price"].idxmax()])


print("\nCheapest Book:")
print(df.loc[df["Price"].idxmin()])


print("\nBook Ratings Count:")
print(df["Rating"].value_counts())


print("\nAvailability Count:")
print(df["Availability"].value_counts())

print("\nFindings")
print("Dataset contains", len(df), "books.")
print("Average Book Price:", round(df["Price"].mean(), 2))
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Rows:", df.duplicated().sum())

