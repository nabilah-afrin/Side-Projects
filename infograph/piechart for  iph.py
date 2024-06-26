import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Data
labels = ['Production', 'Transportation', 'Customer usage', 'Recycling']
values = [0.8, 0.02, 0.17, 0.01]
total = sum(values)
percentages = [f'{(v / total) * 100:.1f}%' for v in values]

colors = ['#f7ae7e','#8f5d46','#556b42','#5e91a4']

plt.figure(figsize=(10, 6))
the_grid = GridSpec(1, 2, width_ratios=[3.5, 0.5])

plt.subplot(the_grid[0], aspect=1)

# Explode the 1st slice (i.e. 'Production')
explode = (0.1, 0, 0, 0)
pie = plt.pie(values, explode=explode, labels=None, colors=colors, autopct=None, startangle=140)

# Draw center circle
# fae29c
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.text(0, 0, '79kg CO2e\n total greenhouse gas\n emission in full lifecycle\n',
         ha='center', va='center', fontsize=13, fontname='Bookman Old Style', color='#503D3F', wrap=True)


# Add a legend with a sidebar
plt.subplot(the_grid[1])
plt.axis('off')
legend_labels = [f'{label}: {percentage}' for label, percentage in zip(labels, percentages)]
legend = plt.legend(pie[0], legend_labels, loc='center left', fontsize=12)
for text in legend.get_texts():
    text.set_fontname('Bookman Old Style')
    text.set_color('#503D3F')

# Save the figure
plt.savefig('pie_chart_with_sidebar_percentages_closer.png', bbox_inches='tight')

plt.show()
# print('Pie chart with sidebar indicators moved closer to the circle and saved as pie_chart_with_sidebar_percentages_closer.png.')