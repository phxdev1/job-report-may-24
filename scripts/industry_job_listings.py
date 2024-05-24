# Update the shortened names dictionary to include 'Computer Hardware Development'
shortened_names = {
    'Information Technology': 'IT',
    'Information Technology Support Services': 'IT',
    'Computer Hardware Development': 'Hardware Dev',
    'Healthcare': 'Healthcare',
    'Finance': 'Finance',
    'Engineering': 'Engineering',
    'Education': 'Education'
}

# Replace the industry names with the shortened names
industry_counts_filtered.index = industry_counts_filtered.index.map(lambda x: shortened_names.get(x, x))

# Plot the data with different colors for each industry in ascending order
colors = ['skyblue', 'lightgreen', 'salmon', 'gold', 'lightcoral']
plt.figure(facecolor='white')
industry_counts_filtered.sort_values(ascending=True).plot(kind='bar', color=colors)
plt.title('Top 5 Industries with Most Job Listings (Excluding Empty Tags)')
plt.xlabel('Industry')
plt.ylabel('Number of Listings')
plt.xticks(rotation=45)
plt.show()