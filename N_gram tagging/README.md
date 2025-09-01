# 📖 N-gram Language Model with NLTK

## 📌 Overview
This project demonstrates how to generate **unigrams, bigrams, and trigrams** from a given text document using **NLTK** in Python.  
N-grams are widely used in **chatbots, predictive text, and sentiment analysis** to predict the next word based on previous ones.

---

## 🧾 Concepts
- **Vocabulary (Vocab):** Set of unique words in the text.
- **Unigram (n=1):** Single words (e.g., `"dog"`).
- **Bigram (n=2):** Pair of consecutive words (e.g., `"dog barks"`).
- **Trigram (n=3):** Sequence of three consecutive words (e.g., `"the dog barks"`).

---

## ⚙️ How It Works
1. Load a `.docx` file using **python-docx**.
2. Extract all paragraph texts and combine them into one string.
3. Tokenize text into lowercase words using **NLTK word_tokenize**.
4. Generate:
   - **Unigrams** → sequences of 1 word  
   - **Bigrams** → sequences of 2 words  
   - **Trigrams** → sequences of 3 words
5. Display statistics:
   - Total number of words
   - Vocabulary size
   - Number of unigrams, bigrams, and trigrams
6. Print first 10 examples of each.

---

## 📊 Sample Output
- Total words in corpus: 1527
- Number of vocabularies in the corpus: 511
- Number of unigrams appeared: 1527
- Number of bigrams appeared: 1526
- Number of trigrams appeared: 1525


First 10 Unigrams:
- artificial
- intelligence
- is
- revolutionizing
- the
- way
- businesses
- operate
- ai
- tools


First 10 Bigrams:
- artificial intelligence
- intelligence is
- is revolutionizing
- revolutionizing the
- the way
- way businesses
- businesses operate
- operate ai
- ai tools
- tools help


First 10 Trigrams:
- artificial intelligence is
- intelligence is revolutionizing
- is revolutionizing the
- revolutionizing the way
- the way businesses
- businesses operate ai
- operate ai tools
- ai tools help
- tools help automate

  
---

## 🖥️ Requirements
Install the following Python libraries:
```bash
pip install nltk python-docx
```
▶️ How to Run

1. Place your .docx file (e.g., Simple_Sample_Document.docx) in the working directory.

2. Update the file path in the script:
```
docx = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")

```
3.Run the script:
```
python ngram_generator.py

```
4.View results in the terminal.

### 📚 Applications of N-grams

- Chatbots → Predict next word in a conversation.
- Sentiment Analysis → Capture context of word sequences.
- Autocomplete → Suggest next word while typing.
- Text Mining → Discover patterns in documents.
