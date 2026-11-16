
from sklearn.linear_model import LogisticRegression

income = [[20000], [30000], [40000], [50000], [60000]]
eligible = [0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(income, eligible)

applicant = [[45000]]
result = model.predict(applicant)[0]

print("Applicant Income:", applicant[0][0])
print("Prediction:", "Eligible" if result else "Not Eligible")
