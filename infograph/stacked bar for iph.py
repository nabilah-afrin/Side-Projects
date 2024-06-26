import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import cm

# Your metal distribution data
categories = ['Precious Metals', 'Toxic Metals', 'Rare Earth Materials', 'Other Materials']
category_percentages = [1.21, 5.70, 4.50, 88.59]

# Metal percentages within each category
metal_data = {
    'Precious Metals': {'Copper': 25, 'Gold': 40, 'Palladium': 15, 'Silver': 15, 'Platinum': 0.55},
    'Toxic Metals': {'Lead': 30, 'Bromine': 40, 'Chromium': 15, 'Sb (Antimony)': 7.50, 'Beryllium': 0.10},
    'Rare Earth Materials': {'Cerium': 40, 'Lanthanum': 25, 'Europium': 7.50, 'Thorium': 0.10},
    'Other Materials': {'Iron': 15, 'Zinc': 7.50, 'Nickel': 7.50, 'Magnesium': 5}
}

# Prepare the data for DataFrame construction
prepared_data = []
for category, metals in metal_data.items():
    prepared_data.extend([(category, k, v) for k, v in metals.items()])

# Create a DataFrame from the metal distribution data
df = pd.DataFrame(prepared_data, columns=['Category', 'Metals', 'Percentage'])

# Fill the missing values by moving them to the previous rows since they seem to be merged cells in Excel
df['Category'] = df['Category'].replace('', None).ffill()

# Pivot the data to get the correct structure for a stacked bar chart
pivot_df = df.pivot_table(index='Category', columns='Metals', values='Percentage', aggfunc='sum', fill_value=0)

# Sort the columns in ascending order for each category
pivot_df = pivot_df.apply(lambda x: x.sort_values(ascending=True), axis=1)

# Define soft aesthetic colors
colors = cm.Pastel1.colors

# Plot the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Bottom parameter for the bar stacking
cumulative = np.zeros(len(pivot_df))

# Plot each metal type in ascending order
for idx, metal in enumerate(pivot_df.columns):
    values = pivot_df[metal]
    ax.bar(pivot_df.index, values, bottom=cumulative, color=colors[idx % len(colors)], edgecolor='white')
    cumulative += values

# Add metal names and percentages inside the bars
for category in pivot_df.index:
    cum_height = 0
    for metal in pivot_df.loc[category].sort_values(ascending=True).index:
        value = pivot_df.loc[category, metal]
        if value > 0:
            label = f'{metal}: {value:.2f}%'
            ax.text(category, cum_height + value/2, label, ha='center', va='center', fontsize=9, fontweight='bold', color='black')
            cum_height += value

# Add grid, labels, and title
ax.set_title('E-waste generated by Smartphones', fontsize=16, fontweight='bold')
ax.set_xlabel('Category', fontsize=14, fontweight='bold')
ax.set_ylabel('Percentage', fontsize=14, fontweight='bold')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(rotation=45, fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()