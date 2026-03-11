import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders
os.makedirs("Analysis_Superstore_Sales/output/charts", exist_ok=True)

# Read CSV
df = pd.read_csv("Analysis_Superstore_Sales/SuperStoreOrders.csv")

# Drop missing values
df = df.dropna()

# Convert sales to numeric
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Convert date (handles mixed formats)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce", dayfirst=True)

# Create year column
df["year"] = df["order_date"].dt.year

# Total sales
total_sales = df["sales"].sum()

# Sales by year
sales_year = df.groupby("year")["sales"].sum()

# Monthly trend

df["month"] = df["order_date"].dt.strftime("%b")
df["year"] = df["order_date"].dt.year
month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
df["month"] = pd.Categorical(df["month"], categories=month_order, ordered=True)
monthly_sales = df.groupby(["year","month"])["sales"].sum().unstack()
# Save summary
with pd.ExcelWriter("Analysis_Superstore_Sales/output/superstore_summary.xlsx") as writer:
    sales_year.to_excel(writer, sheet_name="Sales by Year")
    monthly_sales.to_excel(writer, sheet_name="Monthly Sales")

# Chart 1
sales_year.plot(kind="bar", title="Sales by Year")
plt.savefig("Analysis_Superstore_Sales/output/charts/year_sales.png")
plt.clf()

# Chart 2
monthly_sales.T.plot(marker="o", title="Monthly Sales Trend (All Years)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("Analysis_Superstore_Sales/output/charts/monthly_sales.png")
plt.clf()

print("Total sales:", total_sales)
print("Superstore analysis completed!")