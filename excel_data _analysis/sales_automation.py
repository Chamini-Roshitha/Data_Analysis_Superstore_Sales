import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel("sales_data.xlsx")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Clean data
df = df.dropna()

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Total revenue
total_revenue = df["Revenue"].sum()

# Revenue by product
revenue_by_product = df.groupby("Product")["Revenue"].sum()

# Revenue by region
revenue_by_region = df.groupby("Region")["Revenue"].sum()

# Monthly sales trend
monthly_sales = df.groupby(df["Date"].dt.month)["Revenue"].sum()

# Top product
top_product = revenue_by_product.idxmax()

# Save analysis to Excel
with pd.ExcelWriter("sales_summary.xlsx") as writer:
    revenue_by_product.to_excel(writer, sheet_name="Revenue by Product")
    revenue_by_region.to_excel(writer, sheet_name="Revenue by Region")
    monthly_sales.to_excel(writer, sheet_name="Monthly Sales")

# Create chart
monthly_sales.plot(kind="bar", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("sales_chart.png")

print("Total Revenue:", total_revenue)
print("Top Product:", top_product)
print("Report and chart generated!")