# WordNet Concept Graph from Word Document  

This project demonstrates how to:  
1. Extract text from a **Word document** (`.docx`) using **python-docx**.  
2. Search for a **user-input word** in the document.  
3. Retrieve **WordNet synsets, lemmas, hypernyms, and hyponyms** for that word using **NLTK WordNet**.  
4. Build and visualize a **concept graph** using **NetworkX** and **Matplotlib**.  

---

## 📌 Features  
- Reads and preprocesses text from a Word document.  
- Checks whether the given word exists in the document.  
- Displays up to 3 synsets with their:  
  - Definitions  
  - Lemmas (synonyms)  
  - Hypernyms (more general concepts)  
  - Hyponyms (more specific concepts)  
- Constructs a **directed graph** with:  
  - Input word (light blue)  
  - Synsets (red)  
  - Lemmas (blue)  
  - Hypernyms (green)  
  - Hyponyms (orange)  
- Visualizes relationships using **NetworkX**.  

---

## 🛠️ Requirements  

Install the required libraries:  

```bash
pip install python-docx nltk matplotlib networkx
```
### 🚀 How to Run

- Place your Word document in a known directory (example: Simple_Sample_Document.docx).
- Update the file path in the script:
- doc = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")

``` bash
python wordnet_concept_graph.py
```
- Enter a word (present in the document) when prompted:
- Enter a word to analyze: machine

### 📊 Example Output
Console Output
- Word found: intelligence

Synsets for 'intelligence':
- intelligence.n.01 : the ability to comprehend; to understand and profit from experience

Lemmas:
- intelligence

Hypernyms:
- cognition.n.01 : the psychological result of perception and learning and reasoning

Hyponyms:
- acumen.n.01 : shrewdness shown by keen insight
----------------------------------------

Graph Output

- The graph displays:
- The input word connected to its synsets.
- Synsets linked to their lemmas, hypernyms, and hyponyms.
- Nodes are color-coded for clarity.
