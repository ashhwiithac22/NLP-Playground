# 🧠 Parsing Sentences using Context-Free Grammar (CFG) – NLP Project

This project demonstrates **syntactic parsing** in Natural Language Processing (NLP) using **Context-Free Grammar (CFG)** and **NLTK’s Chart Parser**.  
It performs **Part-of-Speech (POS) tagging** and generates **Parse Trees** that show the grammatical structure of a sentence.

---

## 📘 Description

- **POS Tagging** identifies the grammatical roles of each word (noun, verb, preposition, etc.).
- **CFG (Context-Free Grammar)** defines language production rules (e.g., how a sentence (S) is made up of NP + VP).
- **Parsing** produces **tree structures** that represent how words combine to form phrases and sentences.

---

## 🧩 Key Concepts

### 🔹 Part-of-Speech Tagging (POS)
Assigns grammatical labels to words, e.g.:

[('the', 'DT'), ('dog', 'NN'), ('chased', 'VBD'), ('the', 'DT'), ('cat', 'NN'), ('in', 'IN'), ('the', 'DT'), ('garden', 'NN')]
---

### 🔹 Context-Free Grammar (CFG)
A set of recursive rules to define valid sentence structures, e.g.:

S -> NP VP

NP -> Det N | Det N PP | Name

VP -> V NP | V NP PP | V

PP -> P NP

---

### 🔹 Parse Trees
Visualize sentence structure hierarchically, for example:
```
         S
  _______|______
 NP             VP
```

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install nltk
   ```
2.Run the script:
   ```bash
    python ex11_parsing_using_cfg.py
  ```
---

## 🎯 Insights

POS tagging identifies each word’s grammatical role.

CFG parsing shows how words combine to form meaningful structures.

Useful in NLP applications like chatbots, grammar checkers, and question-answering systems.

