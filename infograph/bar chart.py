import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Precious Metals', 'Toxic Metals', 'Rare Earth Materials', 'Other Materials']
category_percentages = [1.21, 5.70, 4.50, 88.59]

# Metal percentages within each category
metal_percentages = [
    [25, 40, 15, 15, 0.55],  # Precious Metals
    [30, 40, 15, 7.50, 0.10],  # Toxic Metals
    [40, 25, 7.50, 0.10, 0.10],  # Rare Earth Materials
    [15, 7.50, 7.50, 5, 0]  # Other Materials
]

# Colors for each metal within a category
metal_colors = [
    ['#FFD700', '#C0C0C0', '#808080', '#A9A9A9', '#E5E4E2'],  # Precious Metals
    ['#A52A2A', '#8B4513', '#4682B4', '#8B4513', '#B22222'],  # Toxic Metals
    ['#8F4D2E', '#FFD700', '#6495ED', '#A52A2A', '#B22222'],  # Rare Earth Materials
    ['#CD5C5C', '#B0C4DE', '#708090', '#FFD700', '#A9A9A9']  # Other Materials
]

# Create stacked bar chart
fig, ax = plt.subplots()

# Loop through each category and plot the bars
for i, (metal_percent, metal_color) in enumerate(zip(metal_percentages, metal_colors)):
    ax.bar(categories, metal_percent, label=f'Metal {i + 1}', color=metal_color)

# Set labels and title
plt.xlabel('Categories')
plt.ylabel('Percentage of Metals')
plt.title('Metal Distribution in iPhone General')

# Add legend
plt.legend(title='Metals', loc='upper left')

# Show the plot
plt.show()
