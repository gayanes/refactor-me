import pandas as pd

# Read in a data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# List of strings of method names/summary statistics (mean, median, max, min,
# standard deviation) being calculated
agg_stats = ["mean", "median", "max", "min", "std"]

print("Summary statistics on Purchase Amount (USD), Age")
print(df.agg({"Purchase Amount (USD)": agg_stats, "Age": agg_stats}))

print("\nSummary statistics on Purchase Amount (USD) by Season")
print(df[["Season", "Purchase Amount (USD)"]].groupby("Season").agg({"Purchase Amount (USD)": agg_stats}))

# # keep all columns except for "Customer", & "Discount Applied"
# List of columns to be dropped
selected = ["Discount Applied"]
df = df.drop(columns=selected)

# Calculates frequency of Payment Method by Location
pay_by_state = df.groupby(["Location"])["Payment Method"].value_counts()
# Calculates most popular payment method in New York
ny_payments = pay_by_state["New York"]

print("\nPayment Methods in New York")
print(ny_payments)
print(pay_by_state)

# Write this updated data out to csv file
df.to_csv('data/processed/cleaned_data.csv', index=False)
