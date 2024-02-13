from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Your text data
text = "BASEBAND DMTS Leadership Skills Experience Expertise Hardware design SW Integration Levante Virtualization AI/ML Ponente Tulli Tulli Tulli Ecosystem Simulation Specification Maintenance"

# Generate word cloud
wordcloud = WordCloud(width = 800, height = 200, background_color ='white').generate(text)

# Display the generated Word Cloud
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
