import pandas as pd
from openpyxl import load_workbook

data = pd.read_excel("business_sales.xlsx")
summary = data.groupby("Region").agg(
    revenue=("Sales", "sum"),
    orders=("Order_ID", "nunique")
).reset_index()
summary["average_order_value"] = summary["revenue"] / summary["orders"]
summary.to_excel("regional_sales_dashboard.xlsx", index=False)
print(summary)
print("Dashboard data exported successfully")
