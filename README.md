# 🧠 NLP Playground  

This repository is a collection of my **NLP (Natural Language Processing) exercises** where I explore various text processing and analysis techniques.  
Each folder contains Python scripts, outputs, and related resources for the respective exercise.  

---

## 📌 Exercises Included

### 1. Text Preprocessing  
- Cleaning raw text (removing punctuation, numbers, special symbols).  
- Converting text to lowercase.  
- Removing stopwords.  
- Tokenization.  
- **Lemmatization** (using WordNetLemmatizer).  

📁 Folder: `Text Preprocessing`

---

### 2. Word Cloud Visualization  
- Generates a **Word Cloud** from a `.docx` file.  
- Removes stopwords and visualizes the most frequent words.  
- Useful for quickly understanding the main topics in a document.  

📁 Folder: `WordCloud`

---

### 3. Data Vectorization  
- Text represented as **numerical vectors**.  
- Techniques included:  
  - Bag of Words (BoW)  
  - TF-IDF Vectorization  
- Demonstrates how text data can be prepared for ML models.  

📁 Folder: `Data Vectorization`

---

### 4. Frequency Analysis  
- Counts the **frequency of words** in text.  
- Analyzes **word frequency based on length**.  
- Visualizes results using **bar charts** and **word clouds**.  

📁 Folder: `Frequency of Words`

---

### 5. WordNet Exploration  
- Uses **NLTK WordNet** to explore word relationships:  
  - **Synonyms**  
  - **Antonyms**  
  - **Hypernyms** (broader terms)  
  - **Hyponyms** (narrower terms)  
- Helps in understanding semantic relationships.  

📁 Folder: `WordNet`

---

### 6. Pattern Matching (Regex)  
- Applies **regular expressions** for:  
  - Extracting email IDs  
  - Extracting phone numbers  
  - Pattern-based text cleaning  
- Useful for information extraction tasks.  

📁 Folder: `Pattern Matching`

---

### 7. Parts of Speech (POS) Tagging  
- Identifies grammatical roles of words in a sentence (noun, verb, adjective, etc.).  
- Uses **NLTK POS Tagger**.  
- Helps in understanding sentence structure.  

📁 Folder: `POS Tagging`

---

### 8. N-Gram Tagging  
- Generates **bi-grams** and **tri-grams** from text.  
- Helps in understanding word co-occurrence and context.  
- Useful for tasks like text prediction.  

📁 Folder: `N-Gram Tagging`

---

## 🛠️ Requirements
Install dependencies before running the scripts:
```bash
pip install nltk wordcloud matplotlib pandas python-docx
```
```bash
Make sure to also download NLTK datasets (run once):

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
```

### ✅ Key Learnings
- Text cleaning and preprocessing techniques.
- Different methods to represent text numerically.
- Visualization with word clouds and frequency plots.
- Exploring semantic relationships using WordNet.
- Regular expressions for pattern-based text extraction.
- POS tagging and n-gram modeling.

