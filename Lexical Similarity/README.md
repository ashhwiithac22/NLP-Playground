# 🧮 Sentence Similarity using Jaccard and Cosine Measures

This project demonstrates how to **compare the similarity between two sentences** using two popular NLP techniques — **Jaccard Similarity** and **Cosine Similarity (TF-IDF)**.  
It helps quantify how semantically and lexically close two text samples are.

---

## 📘 Description

- **Jaccard Similarity** → Measures word overlap between two sentences.  
- **Cosine Similarity** → Uses **TF-IDF vectorization** to compute the angle between sentence vectors in high-dimensional space.  
- Together, these methods help identify **semantic and lexical similarity** in text data.

---

## 🧩 Key Concepts

### 🔹 Jaccard Similarity
- Focuses on **common words** between two sentences.

### 🔹 Cosine Similarity
- Uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to represent text numerically.  
- Values range from **0 (no similarity)** to **1 (identical meaning)**.


## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install nltk scikit-learn
   ```
2. **Run the Script:**
   ```
   python ex14_sentence_similarity.py
   ```
3. **Sample Output:**
   ```
   Sentence 1: The dog chased the cat
   Sentence 2: The cat was chased by the dog

   Jaccard Similarity: 0.6666666666666666
   Cosine Similarity: 0.7995189954301454
   ```
 
## 🎯 Insights
- Jaccard Similarity considers word overlap, ignoring grammar or order.
- Cosine Similarity captures semantic closeness using vector representations.
- Both metrics indicate that the two sentences are highly similar in meaning.

  
## 🧠 Applications
- Text clustering
- Duplicate content detection
- Semantic search
- Plagiarism checking
- Chatbot intent matching
  
  
## 📚 Tech Stack

- Python 3
- NLTK – Text preprocessing
- Scikit-learn – TF-IDF and Cosine Similarity

  
