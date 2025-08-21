# Word Cloud & Bag of Words from Word Document  
This project demonstrates how to **extract text from a Word document**, clean it, and then perform **text analysis** using Word Clouds representation.  
---

## 📌 Features  
- Reads text from a `.docx` file using **python-docx**.  
- Cleans the text by removing punctuation, converting to lowercase, and removing stopwords.  
- Generates a **Word Cloud visualization** for easy interpretation of frequent words.  
- Uses **Bag of Words (BoW)** with `CountVectorizer` from scikit-learn.  
- Displays the **Top 10 most frequent words** in the document.  

---

## 🛠️ Requirements  

Install the required Python libraries before running the script:  

```bash
pip install python-docx wordcloud matplotlib scikit-learn pandas
```
🚀 How to Run

Place your Word document (example: Simple_Sample_Document.docx) in a known directory.
- Update the file path inside the script:
- doc = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")
``` bash
python wordcloud_bow_docx.py
```
### 📊 Example Outputs

- Word Cloud Visualization
- A graphical representation of the most frequent words in the document.
- Top 10 Most Frequent Words (Bag of Words Output)
