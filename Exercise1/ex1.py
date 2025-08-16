from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re
text = """
Artificial Intelligence (AI) is revolutionizing the way businesses operate. 
AI tools help automate tasks, improve efficiency, and provide better customer experiences. 
Machine Learning (ML), a subset of AI, enables systems to learn from data and make predictions. 
Digital marketing also benefits from AI by enhancing SEO, content creation, and customer engagement.
Artificial intelligence is the ability of a computer or computer-controlled robot to perform tasks that are commonly associated with the intellectual processes characteristic of humans, such as the ability to reason. Although there are as yet no AIs that match full human flexibility over wider domains or in tasks requiring much everyday knowledge, some AIs perform specific tasks as well as humans. Learn more.
Are artificial intelligence and machine learning the same?
No, artificial intelligence and machine learning are not the same, but they are closely related. Machine learning is the method to train a computer to learn from its inputs but without explicit programming for every circumstance. Machine learning helps a computer to achieve artificial intelligence.
artificial intelligence (AI), the ability of a digital computer or computer-controlled robot to perform tasks commonly associated with intelligent beings.
Deep learning is a subset of machine learning that uses multilayered neural networks, called deep neural networks, that more closely simulate the complex decision-making power of the human brain.
Deep neural networks include an input layer, at least three but usually hundreds of hidden layers, and an output layer, unlike neural networks used in classic machine learning models, which usually have only one or two hidden layers.
Generative AI, sometimes called "gen AI", refers to deep learning models that can create complex original content such as long-form text, high-quality images, realistic video or audio and more in response to a user’s prompt or request.
At a high level, generative models encode a simplified representation of their training data, and then draw from that representation to create new work that’s similar, but not identical, to the original data.
Generative models have been used for years in statistics to analyze numerical data. But over the last decade, they evolved to analyze and generate more complex data types. This evolution coincided with the emergence of three sophisticated deep learning model types.
"""
text = re.sub(r'[^A-Za-z\s]', '', text)
text = text.lower()
stopwords = set(STOPWORDS)
text = ' '.join(word for word in text.split() if word not in stopwords)
wordcloud = WordCloud(width=900, height=500, background_color='white', colormap='viridis').generate(text)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Artificial Intelligence Article", fontsize=16)
plt.show()


#2)
#bag of words , tfitf,count vectorizer
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
url = "https://timesofindia.indiatimes.com/world/middle-east/israel-iran-war-trump-weighs-us-strike-netanyahu-cites-personal-cost-10-key-points/articleshow/121964961.cms"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
text = ' '.join(p.get_text() for p in soup.find_all('p'))
text = re.sub(r'[^A-Za-z\s]', '', text)
text = text.lower()
wc = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud from NDTV Article")
plt.show()



