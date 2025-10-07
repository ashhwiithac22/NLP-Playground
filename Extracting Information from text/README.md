# 📝 Named Entity Recognition, Chunking & Relation Extraction

This project demonstrates **information extraction** from text using **spaCy**.  
It covers **Named Entity Recognition (NER)**, **Chunking**, and **Relation Extraction** to identify entities, meaningful phrases, and relationships in sentences.

---

## ⚙️ Features  
- **Named Entity Recognition (NER)**: Classifies entities such as **persons, organizations, locations, dates, and more**.  
- **Chunking**: Divides sentences into **meaningful phrases** or "chunks" (e.g., noun phrases).  
- **Relation Extraction**: Identifies **subject-verb-object (SVO)** relations in text.

---

## 🧠 How It Works
1. Load the **spaCy English model (`en_core_web_sm`)**.  
2. Process input text using `nlp(text)`.  
3. Extract **named entities** using `doc.ents`.  
4. Extract **noun chunks** using `doc.noun_chunks`.  
5. Identify **relations** by finding the **ROOT verb** and its **subject and object** dependencies.

---

## 🛠️ Tech Stack
- Python 3  
- [spaCy](https://spacy.io/) – NLP library for text processing and NER  

---

## 📂 Sample Code
```python
import spacy
nlp = spacy.load("en_core_web_sm")

text = "Virat Kohli plays cricket for India in 2025."
doc = nlp(text)

# Named Entities
for ent in doc.ents:
    print(ent.text, "->", ent.label_)

# Chunking
for chunk in doc.noun_chunks:
    print(chunk.text)

# Relation Extraction
for token in doc:
    if token.dep_ == "ROOT":
        subject = [w.text for w in token.lefts if w.dep_ == "nsubj"]
        obj = [w.text for w in token.rights if w.dep_ in ("dobj", "pobj")]
        if subject and obj:
            print(subject[0], token.text, obj[0])
```
---
## Sample Output
🔹 Named Entities
```
Virat Kohli -> ORG
India -> GPE
2025 -> DATE
```
🔹 Chunking
```
Virat Kohli
cricket
India
```
🔹 Relations
```
Kohli plays cricket
```
---
## How to Run
1.Install spaCy:
```
pip install spacy
python -m spacy download en_core_web_sm
```
2.Run the script:
```
python main.py
```
---
