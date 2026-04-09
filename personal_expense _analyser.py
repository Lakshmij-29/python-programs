import matplotlib.pyplot as plt

categories = ['Food', 'Transport', 'Shopping', 'Bills']
amounts = [2500, 1200, 3000, 1800]

plt.pie(amounts, labels=categories, autopct='%1.1f%%')
plt.title("Monthly Expenses")
plt.show()
