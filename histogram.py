import matplotlib.pyplot as plt
frequency=[7,8,9,10,12,12,12,13,14,15,16,16,17,18,19,21,22,24,25,25,26,28,30,32,35,36,38,40,40,40,42,44,46,48,50]
plt.hist(frequency,bins=10,color="green")
plt.title("histogram")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()
