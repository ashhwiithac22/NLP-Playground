# 📝 NLP Preprocessing & Analysis from Web Text

This project demonstrates how to **scrape text from the web (Wikipedia)** and perform a series of **Natural Language Processing (NLP) tasks** including tokenization, lemmatization, frequency analysis, concordance search, and word cloud visualization.  

---

## ⚙️ Steps Performed in the Project

1. **Web Scraping**  
   - Used `requests` to fetch text from the Wikipedia page on **Natural Language Processing**.  
   - Used `BeautifulSoup` to remove HTML tags and extract clean text.  

2. **Text Cleaning**  
   - Removed URLs.  
   - Expanded contractions (e.g., `"don't"` → `"do not"`).  
   - Removed special characters and punctuation.  

3. **Tokenization & Stopword Removal**  
   - Split text into lowercase tokens using NLTK.  
   - Removed common English stopwords (`the`, `is`, `and`, etc.).  

4. **Lemmatization**  
   - Converted words to their base form using `WordNetLemmatizer`.  
   - Example: `"running"` → `"run"`.  

5. **Frequency Distribution**  
   - Found the **Top 10 most frequent words** in the cleaned text.  

6. **Concordance (Keyword-in-Context Search)**  
   - Showed words surrounding the keyword **“language”** in context.  
   - This is useful to see how a word is used in different sentences.  
   - Example output for `"language"` might look like:
     ```
     ... natural language processing interdisciplinary ...
     ... human language technology deals with ...
     ... programming language also considered ...
     ```

7. **Word Cloud**  
   - Generated a visual representation of the most frequent words.  
   - Larger words in the cloud appear more frequently in the text.  

---

## 📊 Example Outputs


### 🔹 Word Cloud
- The script generates a word cloud highlighting the most frequent words visually.  

---

## 📂 Files

- `webtext_nlp.py` → Python script with preprocessing, analysis, and visualization.  
- Generated plots:  
  - **Word Cloud of Web Text**  

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/ashhwiithac22/NLP---Playground.git
cd NLP---Playground

# Install dependencies
pip install requests beautifulsoup4 nltk wordcloud matplotlib
```
Run the script:
```bash
python webtext_nlp.py
```

### 📌 Key Takeaways

- Concordance helps understand how a word is used in context (semantic usage).
- Word Cloud provides a quick visual summary of frequent terms.
- This pipeline can be extended to other websites or text datasets for NLP tasks.
