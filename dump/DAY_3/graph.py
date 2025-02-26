import matplotlib.pyplot as plt

# Data
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
quantity = [10, 20, 15, 25, 30]

# Create bar chart
plt.bar(fruits, quantity, color='pink', edgecolor='black', linewidth=1.2, )

# Customize title and labels with font family
plt.title("Fruits VS Quantity", fontsize=16, fontweight='bold', fontfamily='monospace', color='darkblue')
plt.xlabel("Fruits", fontsize=14, fontfamily='cursive', color='brown')
plt.ylabel("Quantity", fontsize=14, fontfamily='cursive', color='brown')

# Show the plot
plt.show()
