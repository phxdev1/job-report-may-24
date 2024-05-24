import matplotlib.pyplot as plt

# Create a doughnut chart
fig, ax = plt.subplots(figsize=(10, 7), facecolor='white')

# Plot the doughnut chart
wedges, texts, autotexts = ax.pie(company_size_distribution['count'], labels=company_size_distribution['company_size'], autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))

# Add a circle at the center to make it a doughnut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')
plt.title('Company Size Distribution')
plt.show()
print('Doughnut chart created.')