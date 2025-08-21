from docx import Document
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re
import pandas as pd
from collections import Counter
doc = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")
text = "\n".join([para.text for para in doc.paragraphs])
text = re.sub(r'[^A-Za-z\s]', '', text).lower()
stopwords = set(STOPWORDS)
words = [word for word in text.split() if word not in stopwords]
if not words:
    print("Cleaned text is empty. Cannot generate Word Cloud.")
else:
    wordcloud = WordCloud(width=900, height=500, background_color='white').generate(' '.join(words))
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud Visualization")
    plt.show()
    word_lengths = [len(word) for word in words]
    length_counts = Counter(word_lengths)
    print("Frequency of Words Based on Lengths:")
    for length, count in sorted(length_counts.items()):
        print(f"Length {length}: {count} words")
