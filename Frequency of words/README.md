# Word Cloud and Word Length Frequency Analysis

This project demonstrates how to generate a **Word Cloud** from a Word document and analyze the **frequency of words based on their lengths** using Python.

---

## 📌 Project Overview
- Extracts text from a `.docx` file.
- Cleans the text by:
  - Removing punctuation and special characters.
  - Converting text to lowercase.
  - Removing stopwords.
- Generates a **Word Cloud Visualization** for the cleaned text.
- Calculates and prints the **frequency of words based on their lengths**.

---

## 📂 Input
- A `.docx` file containing text data.  
  Example: `Simple_Sample_Document.docx`

---

## 📊 Output
1. **Word Cloud Visualization** (displayed using matplotlib).  
2. **Word Length Frequency** printed in the console, e.g.:

      Length 2: 15 words

      Length 3: 20 words

      Length 4: 10 words

### 🚀 Usage

- Place your .docx file in the project folder.
- Update the file path in the script:
- doc = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")


### Run the script:

    python wordcloud_frequency.py

### 📌 Example Visualization
- Word Cloud of the input document.
- Printed frequency of words by their length.
