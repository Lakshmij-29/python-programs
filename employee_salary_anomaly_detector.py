import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("employee_salaries.csv")
features = data[["Salary", "Experience"]].dropna()
model = IsolationForest(contamination=0.05, random_state=42)
data.loc[features.index, "Anomaly"] = model.fit_predict(features)
anomalies = data[data["Anomaly"] == -1]
print(anomalies[["Employee_ID", "Salary", "Experience"]])
anomalies.to_csv("salary_anomalies.csv", index=False)
