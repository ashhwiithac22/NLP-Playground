from docx import Document
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
doc = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")
text = "\n".join([para.text for para in doc.paragraphs])
text = re.sub(r'[^A-Za-z\s]', '', text).lower()
stopwords = set(STOPWORDS)
cleaned_text = ' '.join(word for word in text.split() if word not in stopwords)
if not cleaned_text:
    print("Cleaned text is empty. Cannot generate Word Cloud.")
else:
    wordcloud = WordCloud(width=900, height=500, background_color='white').generate(cleaned_text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud Visualization")
    plt.show()
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform([cleaned_text])
    X.toarray()
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    print(df.T.sum(axis=1).sort_values(ascending=False).head(10))
