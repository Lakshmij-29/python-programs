import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("customer_metrics.csv")
features = data[["Annual_Spending", "Purchase_Frequency"]].dropna()
scaler = StandardScaler()
scaled = scaler.fit_transform(features)
model = KMeans(n_clusters=4, random_state=42, n_init=10)
data.loc[features.index, "Customer_Segment"] = model.fit_predict(scaled)
data.to_csv("segmented_customers.csv", index=False)
print(data["Customer_Segment"].value_counts())
