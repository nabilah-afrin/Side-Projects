import matplotlib.pyplot as plt

# Data
countries = ['Norway', 'Germany', 'USA', 'UK', 'France', 'Italy', 'Canada', 'Japan', 'Australia', 'South Korea']
recycling_rates = [97, 98, 29.3, 57.6, 58.2, 45, 9, 77, 31.8, 54.4]

# Create a bar graph
plt.figure(figsize=(3,3), facecolor='#edd9d3')  # Set background color
plt.bar(countries, recycling_rates, color='#d18164', width=0.25)  # Set bar width


plt.title('Plastic Bottle Recycling Rates by Country', color='#4d4d4d')  # Set title color
plt.xlabel('Country', color='#1b5c2d')  # Set x-axis label color
plt.ylabel('Recycling Rate (%)', color='#1b5c2d')  # Set y-axis label color
plt.ylim(0, 100)  # Set the y-axis limit from 0 to 100 for percentage values
plt.xticks(rotation=45, ha='right', color='#1b5c2d')  # Rotate x-axis labels and set color for better readability
plt.yticks(color='#1b5c2d')  # Set color for y-axis labels

# Display the values on top of each bar
for i, rate in enumerate(recycling_rates):
    plt.text(i, rate + 1, f'{rate}%', ha='center', va='bottom', fontsize=10, color='#1b5c2d')

# Remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)


# Show the plot
plt.tight_layout()
plt.show()
