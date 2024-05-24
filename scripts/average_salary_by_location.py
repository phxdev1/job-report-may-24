# Adjust the scale of the plot to better visualize the salary ranges
plt.figure(facecolor='white', figsize=(12, 6))
salary_by_location['mean'].sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Average Salary by Location (Without Outliers)')
plt.xlabel('Location')
plt.ylabel('Average Salary')
plt.xticks(rotation=90)
plt.ylim(50000, 250000)  # Adjust the y-axis limits to better visualize the data
plt.show()