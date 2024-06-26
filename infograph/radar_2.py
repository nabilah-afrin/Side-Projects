import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from Excel file
data = {
    'Parameter': ['Carbon\n Footprint', 'Water Depletion', '\nMetalDeploy\n', 'Fossil Fuel Usage'],
    'Value': [258, 116, 9.3, 90],
    'Total': [1000, 158, 12.4, 133],
    'Unit': ['kg CO2e', 'm3', '\nkg', 'kg oil']
}

df = pd.DataFrame(data)

# Calculate percentage for each parameter
df['Percentage'] = df['Value'] / df['Total'] * 100

# Number of parameters
num_params = len(df)

# Calculate angles for radar chart
angles = np.linspace(0, 2 * np.pi, num_params, endpoint=False).tolist()

# Make the plot
fig, ax = plt.subplots(figsize=(2.5,2.5), subplot_kw=dict(polar=True), facecolor='#edd9d3')
ax.fill(angles, df['Percentage'], color='#d18164', alpha=0.8)
ax.set_yticklabels([])

# Plot data points and parameter labels
ax.plot(angles, df['Percentage'], 'o-', linewidth=0.5, color='#d18164')

# Set individual text properties for parameter labels with courier new font
for angle, label in zip(angles, df['Parameter']):
    va_position = 103 if label not in ['Water Depletion', 'Fossil Fuel Usage'] else 90
    ax.text(angle, va_position, label, ha='center', va='center', fontsize=13, fontfamily='Courier New', fontweight='bold',color='black')

# Remove angle lines
ax.set_xticks([])

# Add unit values with custom styling
for angle, label, unit in zip(angles, df['Percentage'], df['Unit']):
    ax.text(angle, label + 3, f'{label:.2f}%\n({unit})', ha='center', va='center', fontsize=13, fontfamily='Courier New', fontweight='bold',color='black')

# plt.title('Environmental Impact in Transportation and Distribution', fontsize=12, fontweight='bold', color='black')

plt.tight_layout()  
plt.show()# Adjust layout to prevent
