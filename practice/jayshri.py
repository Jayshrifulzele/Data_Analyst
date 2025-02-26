import matplotlib.pyplot as plt
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
quantity = [12, 23, 14, 25, 32]

plt.bar(fruits, quantity)
plt.title("Stock of fruits")
plt.xlabel("fruits")
plt.ylabel("quantity")
plt.show()
