import matplotlib.pyplot as plt

# Data
storage_sizes = ['64GB', '128GB', '256GB']
carbon_footprint = [79, 87, 93]

# Plotting the line chart
fig, ax = plt.subplots()
ax.plot(storage_sizes, carbon_footprint, marker='o', color='#556b42', linestyle='-', linewidth=2, markersize=8)

# Set background color
ax.set_facecolor('#FAE29C')

ax.set_xticklabels(storage_sizes, fontsize=13, color='#56494C', fontname='Bookman Old Style')

# Set y-axis ticks and labels
ax.set_yticks(carbon_footprint)
ax.set_yticklabels(carbon_footprint, fontsize=13, color='#56494C', fontname='Bookman Old Style')

plt.xlabel('Storage Size', fontsize=13, color='#56494C', fontname='Bookman Old Style')
plt.ylabel('Carbon Footprint (kg CO2e)', fontsize=13, color='#56494C', fontname='Bookman Old Style')
plt.title('Carbon Footprint Generated During Distribution', fontsize=13, color='#56494C', fontname='Bookman Old Style')

# Display the values on the data points with adjusted vertical position
# for i, value in enumerate(carbon_footprint):
#     plt.text(storage_sizes[i], value, f'{value} kg', ha='center', va='center', fontsize=13, color='#56494C', fontname='Bookman Old Style', weight='bold')

# Show the plot
plt.grid(True)
plt.show()
