import requests #reads webpages from the internet
from bs4 import BeautifulSoup #helps to remove html tags
import re #regular expressions - helps us to clean unwanted things like special characters
import contractions #expands short words like I'll to I will
import nltk 
from nltk.corpus import stopwords #corpus - collections of text data
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize #breaks text into words
nltk.download('punkt') #used for splitting words
nltk.download('stopwords') #used to remove common english words

#Retrieving content from webpage
url = "https://en.wikipedia.org/wiki/Natural_language_processing"
response = requests.get(url)
html_content = response.text

#Removing HTML tags
soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text() #extracts readable text

#Removing URLs
text = re.sub(r'https\S+|www\S+', '', text) #removes words that starts with http,https,www
#Expand contractions
text = contractions.fix(text)
#Removing special characters
text = re.sub(r'[^A-Za-z\s]', '', text)
#Removing stop words
stop_words = set(stopwords.words('english'))
words = wordpunct_tokenize(text.lower())
filtered_words = [word for word in words if word not in stop_words]
cleaned_text = ' '.join(filtered_words)
print("Cleaned Text:\n")
print(cleaned_text[:1500])
