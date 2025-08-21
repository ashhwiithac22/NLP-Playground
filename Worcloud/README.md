# Word Cloud & Text Analysis with Python  

This project demonstrates how to generate **Word Clouds** and perform **basic text preprocessing** in Python. It includes two parts:  

1. **Word Cloud from a given text (Artificial Intelligence article)**  
2. **Word Cloud from a live news article (scraped using BeautifulSoup)**  

---

## 📌 Features  
- Cleans and preprocesses text (removes punctuation, converts to lowercase, removes stopwords).  
- Generates **Word Cloud visualization** for better understanding of word frequency.  
- Demonstrates web scraping with `requests` and `BeautifulSoup` to fetch live article content.  
- Uses **Matplotlib** to display the word clouds.  

---

## 🛠️ Requirements  

Install the required Python libraries before running the scripts:  

```bash
pip install wordcloud matplotlib requests beautifulsoup4
```
### 🚀 How to Run
1. Word Cloud from Artificial Intelligence Article
- The script takes a predefined text about AI.
- Cleans the text using Regex & Stopwords.
- Generates a Word Cloud with Viridis color map.
  ```bash
  python wordcloud_ai.py
  ```
2.Word Cloud from News Article (Web Scraping)

- Fetches news article text using requests + BeautifulSoup.
- Cleans the text with regex.
- Generates and displays the Word Cloud.
```
python wordcloud_news.py
```

### 📊 Example Outputs
- AI Article Word Clou
- Shows frequently used terms such as artificial, intelligence, learning, generative, neural, models.
- News Article Word Cloud
- Highlights keywords from the Times of India article fetched live.
