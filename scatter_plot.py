import matplotlib.pyplot as plt
day=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
price=[140,120,190,185,345,80,130]
plt.scatter(day,price)
plt.title("scatter plot")
plt.xlabel("days of the week")
plt.ylabel("price")
plt.show()
