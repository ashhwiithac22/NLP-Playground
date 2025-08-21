# Word Cloud & Word Length Frequency from Word Document  

This project demonstrates how to **extract text from a Word document**, clean it, and perform **text analysis** by:  

1. Generating a **Word Cloud** to visualize the most frequent words.  
2. Analyzing the **frequency of words based on their lengths** using Python’s `Counter`.  

---

## 📌 Features  
- Reads text from a `.docx` file using **python-docx**.  
- Cleans the text (removes punctuation, converts to lowercase, removes stopwords).  
- Generates a **Word Cloud** visualization of frequent words.  
- Calculates and displays the **distribution of words by length** (e.g., how many 3-letter words, 5-letter words, etc.).  

---

## 🛠️ Requirements  

Install the required Python libraries before running the script:  

```bash
pip install python-docx wordcloud matplotlib pandas
```
### 🚀 How to Run

- Place your Word document (example: Simple_Sample_Document.docx) in a known directory.
- Update the file path in the script:
- doc = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")

Run the script:
``` bash
python wordcloud_wordlength_docx.py
```

### 📊 Example Outputs
1. Word Cloud Visualization
- Displays the most frequently occurring words in the document.

2. Word Length Frequency Analysis

### Notes

- If the document is empty or contains only stopwords, the script will display a warning and skip Word Cloud generation.
- Word length distribution helps analyze text characteristics (e.g., short vs. long words).
- You can extend this script to compute average word length, most common word lengths, or visualize with a bar chart.
