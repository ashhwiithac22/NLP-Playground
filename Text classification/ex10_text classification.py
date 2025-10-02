from wordcloud import WordCloud
import matplotlib.pyplot as plt
texts = [
    "India wins the cricket world cup",
    "Messi scores a hat-trick in football match",
    "Olympics 2024 to be held in Paris",
    "Apple launches new iPhone with AI features",
    "Google introduces latest Android version",
    "NASA reveals new space mission",
    "Heavy rains cause floods in India",
    "UN summit focuses on world peace",
    "Elections held in USA with record turnout"
]

labels = [
    "Sports", "Sports", "Sports",
    "Technology", "Technology", "Technology",
    "World News", "World News", "World News"
]
all_text = " ".join(texts)
wordcloud = WordCloud(stopwords="english", background_color="white").generate(all_text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of News Texts")
plt.show()
def classify_text(text):
    text = text.lower()

    sports_keywords = ["cricket", "football", "hockey", "tennis", "olympics", "goal", "match", "policy", "sports"]
    tech_keywords = ["technology", "apple", "google", "microsoft", "tesla", "ai", "software", "nasa", "space", "robot"]
    news_keywords = ["government", "flood", "earthquake", "summit", "elections", "peace", "war", "world", "india", "japan"]

    if any(word in text for word in sports_keywords):
        return "Sports"
    elif any(word in text for word in tech_keywords):
        return "Technology"
    elif any(word in text for word in news_keywords):
        return "World News"
    else:
        return "Unknown"
samples = [
    "Government announces new sports policy",
    "Tesla develops self-driving car",
    "Earthquake hits Japan",
    "NASA sends astronauts to space",
]
for s in samples:
    pred = classify_text(s)
    print(f"Text: {s}\nPredicted Category: {pred}\n")
