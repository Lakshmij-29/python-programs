
import pandas as pd

data = pd.read_csv("sales.csv")

print("Total Records:", len(data))
print("Total Revenue:", data["revenue"].sum())
print("Average Revenue:", data["revenue"].mean())

top_product = data.groupby("product")["revenue"].sum().idxmax()
print("Best Selling Product:", top_product)

data["revenue"] = data["quantity"] * data["price"]
data.to_csv("analyzed_sales.csv", index=False)
