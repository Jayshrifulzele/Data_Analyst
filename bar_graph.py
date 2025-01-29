import matplotlib.pyplot as plt
fruits = ["apple", "banana", "orange", "grapes", "mango"]
quantity =[10,20,15,25,30]

plt.bar(fruits,quantity, color='pink', edgecolor='black', linewidth=1.3,)
plt.title("Fruits VS Quantity", fontsize=19, fontweight='bold', fontfamily='monospace', color='darkblue') 
plt.xlabel("Fruits", fontsize=15, fontfamily='cursive', color='brown')
plt.ylabel("Quantity", fontsize=15, fontfamily='cursive', color='brown')


plt.show()