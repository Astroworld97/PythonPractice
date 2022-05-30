import matplotlib.pyplot as plt

X1 = [1, 2, 3, 4]
X2 = [4, 3, 2, 1]
y = [1, 4, 9, 17]

plt.plot(X1, y, marker="+", markerfacecolor="blue")
plt.plot(X2, y, marker="*", markerfacecolor="red")
plt.ylabel("some numbers")
plt.show()
