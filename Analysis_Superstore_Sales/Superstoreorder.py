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

df["profit"] = pd.to_numeric(df["profit"], errors="coerce")

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
month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
df["month"] = pd.Categorical(df["month"], categories=month_order, ordered=True)
monthly_sales = df.groupby(["year","month"])["sales"].sum().unstack()

# Sales by Category
sales_category = df.groupby("category")["sales"].sum()
category_year_sales = df.groupby(["category", "year"])["sales"].sum().unstack()

# Sales by Region
sales_region = df.groupby("region")["sales"].sum()
region_year_sales = df.groupby(["region", "year"])["sales"].sum().unstack()
# Total profit
total_profit = df["profit"].sum()

# Profit by Year
profit_year= df.groupby("year")["profit"].sum()
# Profit by Category
profit_catergory= df.groupby("category")["profit"].sum()
category_year_profit = df.groupby(["category", "year"])["profit"].sum().unstack()

# Profit by region
profit_region= df.groupby("region")["profit"].sum()
region_year_profit = df.groupby(["region", "year"])["profit"].sum().unstack()

# Top 10 Products
top_products = df.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10)

# Save summary
with pd.ExcelWriter("Analysis_Superstore_Sales/output/superstore_summary.xlsx") as writer:

    # Sales sheets
    sales_year.to_excel(writer, sheet_name="Sales by Year")
    monthly_sales.to_excel(writer, sheet_name="Monthly Sales")
    sales_category.to_excel(writer, sheet_name="Sales by Category")
    category_year_sales.to_excel(writer, sheet_name="Category Sales Year")
    sales_region.to_excel(writer, sheet_name="Sales by Region")
    region_year_sales.to_excel(writer, sheet_name="Region Sales Year")

    # Profit sheets
    profit_year.to_excel(writer, sheet_name="Profit by Year")
    category_year_profit.to_excel(writer, sheet_name="Profit by Category")
    region_year_profit.to_excel(writer, sheet_name="Profit by Region")

# Chart 1
sales_year.plot(kind="bar", title="Sales by Year")
plt.savefig("Analysis_Superstore_Sales/output/charts/year_sales.png")
plt.clf()

# Chart 2
monthly_sales.T.plot(marker="o", figsize=(8,5), title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(title="Year")
plt.savefig("Analysis_Superstore_Sales/output/charts/monthly_sales.png")
plt.clf()

# Chart 3
# sales_category.plot(kind="bar", title="Sales by category")
# plt.xlabel("category")
# plt.ylabel("Sales")
# plt.savefig("Analysis_Superstore_Sales/output/charts/catergory_sales.png")
# plt.clf()

# plotting a vertical multiseries bar chart 
# category_year_sales.plot(kind="bar", title="Sales by Category (Year-wise)")
# plt.xlabel("Category")
# plt.ylabel("Sales")
# plt.savefig("Analysis_Superstore_Sales/output/charts/catergory_sales.png")
# plt.clf()
#plotting a stack bar chat for sales 
# category_year_sales.plot(
#     kind="bar",
#     stacked=True,
#     title="Sales by Category (Year-wise Stacked)"
# )

# plt.xlabel("Category")
# plt.ylabel("Sales")
# plt.legend(title="Year")

# plt.savefig("Analysis_Superstore_Sales/output/charts/catergory_sales.png")
# plt.clf()

# Create figure with 2 charts
fig, ax = plt.subplots(1, 2, figsize=(12,5))

# Chart 1: Vertical bar chart
category_year_sales.plot(kind="bar", ax=ax[0], title="Category Sales (Year-wise)")
ax[0].set_xlabel("Category")
ax[0].set_ylabel("Sales")

# Chart 2: Stacked bar chart
category_year_sales.plot(kind="bar", stacked=True, ax=ax[1], title="Category Sales (Stacked)")
ax[1].set_xlabel("Category")
ax[1].set_ylabel("Sales")

# Adjust layout
plt.tight_layout()

# Save both charts in one image
plt.savefig("Analysis_Superstore_Sales/output/charts/catergory_sales.png")
plt.clf()

# Chart 4
# sales_region.plot(kind="bar", title="Sales by Region")
# plt.xlabel("region")
# plt.ylabel("Sales")
# plt.savefig("Analysis_Superstore_Sales/output/charts/region_sales.png")
# plt.clf()
# Create figure with 2 charts
fig, ax = plt.subplots(1, 2, figsize=(20,8))

# Chart 1: Vertical bar chart
region_year_sales.plot(kind="bar", ax=ax[0], title="Region Sales (Year-wise)")
ax[0].set_xlabel("region")
ax[0].set_ylabel("Sales")

# Chart 2: Stacked bar chart
region_year_sales.plot(kind="bar", stacked=True, ax=ax[1], title="Region Sales (Stacked)")
ax[1].set_xlabel("region")
ax[1].set_ylabel("Sales")

# Adjust layout
plt.tight_layout()

# Save both charts in one image
plt.savefig("Analysis_Superstore_Sales/output/charts/region_sales.png")
plt.clf()
print("Total sales:", total_sales)
print("Superstore analysis completed!")

# Chart 5
profit_year.plot(kind="bar", title="Profit by Year")
plt.savefig("Analysis_Superstore_Sales/output/charts/year_profit.png")
plt.clf()

# Chart 6
# profit_catergory.plot(kind="bar", title="Profit by catergory")
# plt.xlabel("Category")
# plt.ylabel("profit")
# plt.savefig("Analysis_Superstore_Sales/output/charts/profit_by_catergory.png")
# plt.clf()

# category_year_profit.plot(kind="bar", stacked=True, title="Profit by Category (Year-wise Stacked)")

# plt.xlabel("Category")
# plt.ylabel("profit")
# plt.legend(title="Year")

# plt.savefig("Analysis_Superstore_Sales/output/charts/catergory_profit_stack.png")
# plt.clf()
# category_year_profit.plot(kind="bar", title="profit by Category (Year-wise)")
# plt.xlabel("Category")
# plt.ylabel("profit")
# plt.savefig("Analysis_Superstore_Sales/output/charts/catergory_profit_vertical.png")
# plt.clf()
# Create figure with 2 charts
fig, ax = plt.subplots(1, 2, figsize=(20,8))

# Chart 1: Vertical bar chart
category_year_profit.plot(kind="bar", ax=ax[0], title="Catergory profit (Year-wise)")
ax[0].set_xlabel("Category")
ax[0].set_ylabel("profit")

# Chart 2: Stacked bar chart
category_year_profit.plot(kind="bar", stacked=True, ax=ax[1], title="Catergory profit (Stacked)")
ax[1].set_xlabel("Category")
ax[1].set_ylabel("profit")

# Adjust layout
plt.tight_layout()

# Save both charts in one image
plt.savefig("Analysis_Superstore_Sales/output/charts/Category_profit_stack&vertical.png")
plt.clf()

#Chart 7
# Create figure with 2 charts
fig, ax = plt.subplots(1, 2, figsize=(20,8))

# Chart 1: Vertical bar chart
region_year_profit.plot(kind="bar", ax=ax[0], title="Region profit (Year-wise)")
ax[0].set_xlabel("region")
ax[0].set_ylabel("profit")

# Chart 2: Stacked bar chart
region_year_profit.plot(kind="bar", stacked=True, ax=ax[1], title="Region profit (Stacked)")
ax[1].set_xlabel("region")
ax[1].set_ylabel("profit")

# Adjust layout
plt.tight_layout()

# Save both charts in one image
plt.savefig("Analysis_Superstore_Sales/output/charts/region_profit_stack&vertical.png")
plt.clf()

#chart 8
top_products.plot(kind="barh", title="Top 10 Products by Sales")
plt.xlabel("Sales")
plt.savefig("Analysis_Superstore_Sales/output/charts/top_products.png")
plt.clf()