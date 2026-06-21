import pandas as pd
import numpy as np

# 1. Load the messy data (Change 'cafe_sales.csv' to your raw file name if needed)
df = pd.read_csv("cafe_sales.csv")

# 2. Replace placeholder string errors with real NaN null values
df = df.replace(["UNKNOWN", "ERROR"], np.nan)

# 3. Fill missing categorical data with "Unknown"
df["Item"] = df["Item"].fillna("Unknown")
df["Payment Method"] = df["Payment Method"].fillna("Unknown")
df["Location"] = df["Location"].fillna("Unknown")

# 4. Convert numeric columns to proper numbers and fix corrupted data
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')

# 5. Fill missing numeric data with the median values
df[["Quantity", "Price Per Unit", "Total Spent"]] = df[["Quantity", "Price Per Unit", "Total Spent"]].fillna(
    df[["Quantity", "Price Per Unit", "Total Spent"]].median()
)

# 6. Drop rows where the Transaction Date is missing
df = df.dropna(subset=["Transaction Date"])

# 7. Convert Transaction Date to a proper datetime format
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

# 8. Save the perfectly cleaned data to a new CSV file
df.to_csv("cleaned_cafe_sales.csv", index=False)
