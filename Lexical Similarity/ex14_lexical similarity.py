import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def jaccard_similarity(sent1, sent2):
    words1 = set(sent1.lower().split())
    words2 = set(sent2.lower().split())
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    return len(intersection) / len(union)

def cosine_sim(sent1, sent2):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([sent1, sent2])
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

s1 = "The dog chased the cat"
s2 = "The cat was chased by the dog"

print("Sentence 1:", s1)
print("Sentence 2:", s2)
print("\nJaccard Similarity:", jaccard_similarity(s1, s2))
print("Cosine Similarity:", cosine_sim(s1, s2))
