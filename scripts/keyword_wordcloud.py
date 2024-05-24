import re

# Remove the terms 'ServiceNow' and 'Experience' (case insensitive) from the text
it_text = re.sub(r'(?i)servicenow', '', it_text)
it_text = re.sub(r'(?i)experience', '', it_text)

# Generate the word cloud for IT industry job postings excluding 'ServiceNow' and 'Experience'
it_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(it_text)

# Plot the word cloud
plt.figure(facecolor='white', figsize=(10, 5))
plt.imshow(it_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of ServiceNow Skills Required in IT Industry (Excluding ServiceNow and Experience)')
plt.show()