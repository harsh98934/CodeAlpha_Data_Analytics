import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("books.csv")

# Clean Data
df["Price"] = df["Price"].str.extract(r"([\d.]+)").astype(float)
df["Availability"] = df["Availability"].str.strip()

# Create Dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("Books Dataset Dashboard", fontsize=18, fontweight="bold")

# Chart 1 - Price Distribution
sns.histplot(df["Price"], bins=15, kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Price Distribution")
axes[0, 0].set_xlabel("Price (£)")
axes[0, 0].set_ylabel("Number of Books")

# Chart 2 - Rating Distribution
sns.countplot(data=df, x="Rating", order=df["Rating"].value_counts().index, ax=axes[0, 1])
axes[0, 1].set_title("Books by Rating")
axes[0, 1].set_xlabel("Rating")
axes[0, 1].set_ylabel("Count")

# Chart 3 - Price Boxplot
sns.boxplot(y=df["Price"], ax=axes[1, 0])
axes[1, 0].set_title("Book Price Outliers")
axes[1, 0].set_ylabel("Price (£)")

# Chart 4 - Average Price by Rating
average_price = df.groupby("Rating")["Price"].mean().sort_index()

average_price.plot(
    kind="bar",
    ax=axes[1, 1],
    color="skyblue",
    edgecolor="black"
)

axes[1, 1].set_title("Average Price by Rating")
axes[1, 1].set_xlabel("Rating")
axes[1, 1].set_ylabel("Average Price (£)")

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig("books_dashboard.png", dpi=300)

plt.show()

# Individual Charts

# Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=15, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# Ratings
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Rating", order=df["Rating"].value_counts().index)
plt.title("Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("ratings.png")
plt.show()

# Availability
plt.figure(figsize=(8,5))
df["Availability"].value_counts().plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)
plt.title("Book Availability")
plt.xlabel("Availability")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("availability.png")
plt.show()

# Price Boxplot
plt.figure(figsize=(6,5))
sns.boxplot(y=df["Price"])
plt.title("Price Outliers")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig("price_boxplot.png")
plt.show()

# Average Price by Rating
plt.figure(figsize=(8,5))
average_price.plot(
    kind="bar",
    color="green",
    edgecolor="black"
)
plt.title("Average Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.tight_layout()
plt.savefig("average_price_rating.png")
plt.show()

print("\nVisualization Task Completed Successfully!")

print("\nGenerated Files:")
print("1. books_dashboard.png")
print("2. price_distribution.png")
print("3. ratings.png")
print("4. availability.png")
print("5. price_boxplot.png")
print("6. average_price_rating.png")