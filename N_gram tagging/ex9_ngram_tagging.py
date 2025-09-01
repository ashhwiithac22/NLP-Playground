'''
vocab is set of unique words
unigram : n = 1 (eg: "cat", "dog")
bigram  : n = 2 (eg: "cat dog", "tiger lion")
trigram : n = 3 (eg: "cat dog tiger")

these are used to predict the next word based on previous one, it is used in chatbots and also in sentiment analysis
'''

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter
from docx import Document
docx = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")
text = ' '.join([p.text.strip() for p in docx.paragraphs if p.text.strip()])

# Tokenizing into words (convert to lowercase for uniformity)
tokens = word_tokenize(text.lower())
# Total words in document
total_words = len(tokens)
# Vocabulary
vocab = set(tokens)
vocab_size = len(vocab)
# Unigrams
unigrams = list(ngrams(tokens, 1))
num_unigrams = len(unigrams)
# Bigram
bigrams = list(ngrams(tokens, 2))
num_bigrams = len(bigrams)
# Trigrams
trigrams = list(ngrams(tokens, 3))
num_trigrams = len(trigrams)
print("Total words in corpus:", total_words)
print("Number of vocabularies in the corpus:", vocab_size)
print("Number of unigrams appeared:", num_unigrams)
print("Number of bigrams appeared:", num_bigrams)
print("Number of trigrams appeared:", num_trigrams)
print("\nFirst 10 Unigrams:")
for gram in unigrams[:10]:
    print(gram[0])

print("\nFirst 10 Bigrams:")
for gram in bigrams[:10]:
    print(' '.join(gram))

print("\nFirst 10 Trigrams:")
for gram in trigrams[:10]:
    print(' '.join(gram))