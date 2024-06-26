import matplotlib.pyplot as plt

# Data
categories = ['Precious Metals', 'Rare Earth Materials', 'Toxic Metals', 'Others']
percentages = [1.21, 4.50, 5.70, 88.59]

# Colors
colors = ['gold', 'lightblue', 'lightcoral', 'lightgray']

# Explode the 3 least categories
explode = (0.3, 0.2, 0, 0)

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages,  autopct='%1.2f%%', colors=colors, explode=explode, startangle=,font)
plt.title("Distribution of Metals ")
plt.show()
