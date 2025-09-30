# NLP POS Tagging and Visualization

This project demonstrates **Natural Language Processing (NLP)** techniques using **NLTK** and **spaCy** for Part-of-Speech (POS) tagging and dependency parsing visualization from a `.docx` document.

---

## 📌 Features
- Extracts text from a `.docx` file using **python-docx**.
- Tokenizes text into words with **NLTK**.
- Performs POS tagging with **NLTK**.
- Generates an **HTML table** showing words and their POS tags.
- Uses **spaCy**'s `displaCy` to visualize **dependency parsing** and saves it as an HTML file.

---

## 🛠️ Tech Stack
- **Python 3**
- [NLTK](https://www.nltk.org/) – Tokenization & POS tagging  
- [spaCy](https://spacy.io/) – Dependency parsing & visualization  
- [python-docx](https://python-docx.readthedocs.io/en/latest/) – Reading `.docx` files  

---

## 📂 Project Workflow
1. Load the `.docx` file.  
2. Extract first **3 paragraphs** and limit text to **50 words**.  
3. Perform **word tokenization** and **POS tagging** with NLTK.  
4. Save POS tagging results in `nltk_pos_visualization.html`.  
5. Perform **dependency parsing** using spaCy and save visualization in `spacy_displacy_visualization.html`.

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   https://github.com/ashhwiithac22/NLP-Playground/tree/main/Parts%20of%20Speech
   ```
2. Install dependencies:
   ```
   pip install nltk spacy python-docx
   python -m spacy download en_core_web_sm
   ```
3. Update the file path in the script:
   ```
   docx = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")
   ```
4. Run the script:
 ```
   python main.py
```
5. Open the generated HTML files:

- nltk_pos_visualization.html
- spacy_displacy_visualization.html

## Dependency Parsing (spaCy)
The displaCy HTML file shows a graphical representation of how words are connected grammatically.
