import nltk
import requests
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist, Text
from wordcloud import WordCloud
import matplotlib.pyplot as plt
url = "https://en.wikipedia.org/wiki/Natural_language_processing"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text()
text = re.sub(r'https\S+|www\S+', '', text)
try:
    import contractions
    text = contractions.fix(text)
except:
    pass 
text = re.sub(r'[^A-Za-z\s]', '', text)
tokens = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token not in stop_words]
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
freq_dist = FreqDist(lemmatized_tokens)
print("\nTop 10 Frequent Words:\n")
for word, freq in freq_dist.most_common(10):
    print(f"{word} : {freq}")
print("\nConcordance for 'language':\n")
text_obj = Text(lemmatized_tokens)
text_obj.concordance("language", width=80, lines=10)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(lemmatized_tokens))
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Web Text")
plt.show()

