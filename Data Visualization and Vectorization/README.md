# 📚 Word Cloud & Text Analysis  

## 📌 Project Overview  
This project demonstrates text processing and visualization by generating a **Word Cloud** from a Word document (`.docx`). It also applies **CountVectorizer** to transform the text into numerical features for simple text analysis.  

---

## 🔑 Key Features  
- Extracts raw text from a `.docx` file.  
- Cleans text (removes punctuation, numbers, stopwords).  
- Generates a **Word Cloud** to highlight the most frequent words.  
- Creates a **Bag-of-Words model** using CountVectorizer.  
- Displays **Top 10 most frequent words** with counts.  

---

## 📂 Input  
- `Simple_Sample_Document.docx` – sample Word document with text.  

---

## 📊 Output  
1. **Word Cloud Visualization** – graphical representation of frequent words.  
2. **Word Frequency Table** – Top 10 words with their frequencies.  

---

## ⚙️ Tools & Libraries Used  
- **python-docx** → Extracts text from `.docx` files.  
- **WordCloud** → Creates the word cloud.  
- **Matplotlib** → Plots the visualization.  
- **Scikit-learn (CountVectorizer)** → Generates Bag-of-Words.  
- **Pandas** → Handles tabular word frequencies.  
- **Regex** → Cleans unwanted characters.  

---

## 🚀 Workflow  
1. **Extract Text** → Read the `.docx` file using `python-docx`.  
2. **Preprocess Text** → Remove stopwords, numbers, and special characters.  
3. **Generate Word Cloud** → Create a visualization of the top words.  
4. **Vectorize Text** → Convert cleaned text into a numerical matrix with CountVectorizer.  
5. **Analyze Word Frequency** → Display top 10 most frequent words in a table.  

---

## 📌 Applications  
- Quick visualization of text data.  
- Useful for **NLP preprocessing**.  
- Identifying common terms in research papers, notes, or reports.  
