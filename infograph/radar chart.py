import matplotlib.pyplot as plt
import numpy as np

# Define colors
bg_color = '#ece4d5'
line_colors = ['#ada39d', 'lightcoral']
font_color = '#385459'

# Set the background color
plt.figure(figsize=(8, 8), facecolor=bg_color)

# Define the impact categories
categories = ['GWP (CO2 eq.)', 'Acidification (SO2 eq.)', 'Respiratory effects (DALY)', 'Human toxicity (1,4-DB eq.)']

# Original values for E-BIKE and Petrol car (stored as float)
e_bike_values = np.array([497101, 2070, 518, 1482], dtype=float)
petrol_car_values = np.array([61707544, 1482, 8391, 40763], dtype=float)

# Adjust only specific values for better visibility
e_bike_values_adjusted = np.copy(e_bike_values)
petrol_car_values_adjusted = np.copy(petrol_car_values)

# Choose the indices of values to adjust
indices_to_adjust = [0]  # Adjust only the first value (GWP)

# Apply adjustments
e_bike_values_adjusted[indices_to_adjust] /= 100000
petrol_car_values_adjusted[indices_to_adjust] /= 1000000

# Normalize the adjusted values (optional)
e_bike_values_normalized = (e_bike_values_adjusted - np.min(e_bike_values_adjusted)) / (np.max(e_bike_values_adjusted) - np.min(e_bike_values_adjusted))
petrol_car_values_normalized = (petrol_car_values_adjusted - np.min(petrol_car_values_adjusted)) / (np.max(petrol_car_values_adjusted) - np.min(petrol_car_values_adjusted))

# Create a radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), facecolor=bg_color)

# Calculate angle for each category
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()

# Plot the scattered points for E-BIKE with values
ax.plot(angles, e_bike_values_normalized, color=line_colors[0], marker='o', linestyle='-', label='E-BIKE')
for angle, value, label in zip(angles, e_bike_values_normalized, e_bike_values):
    ax.text(angle, value, f'{label:.0f}', color=font_color, fontsize=8, ha='center', va='center')

# Plot the scattered points for Petrol car with values
ax.plot(angles, petrol_car_values_normalized, color=line_colors[1], marker='o', linestyle='-', label='Petrol car')
for angle, value, label in zip(angles, petrol_car_values_normalized, petrol_car_values):
    ax.text(angle, value, f'{label:.0f}', color=font_color, fontsize=8, ha='center', va='center')

# Add labels
ax.set_thetagrids(np.array(angles) * 180/np.pi, categories, color=font_color)

# Set background color for the inside circle
ax.set_facecolor(bg_color)

# Display legend
ax.legend(loc='upper right')

plt.show()