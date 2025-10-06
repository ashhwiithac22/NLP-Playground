from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from wordcloud import WordCloud
import matplotlib.pyplot as plt

texts = [
    # Sports
    "India wins cricket world cup",
    "Ronaldo scores a hat trick in football match",
    "Olympics postponed due to weather",
    "Messi joins new football club",
    "Tennis championship begins next week",
    "Cricket fans celebrate big win",
    "Virat Kohli becomes top batsman",
    "Football World Cup will be hosted in Qatar",
    "India defeats Australia in test match",
    "Serena Williams retires from tennis",
    "Hockey team qualifies for finals",
    "Brazil wins Copa America",
    "Cricket match cancelled due to rain",
    "Fans cheer during football match",
    "Olympic flame lit in Tokyo",
    "Athlete sets new world record in running",
    "India hosts Asian Games",
    "Football team celebrates victory",
    "Cricket players sign new contracts",
    "Tennis star wins grand slam title",

    # Technology
    "Tesla develops self-driving car",
    "Microsoft launches new AI product",
    "Google introduces latest Android version",
    "Apple unveils new iPhone model",
    "Facebook updates privacy policy",
    "SpaceX successfully launches rocket",
    "NASA announces new space mission",
    "Scientists develop artificial intelligence tool",
    "Robots are replacing human jobs",
    "Amazon builds new data center",
    "AI beats humans in chess game",
    "New chip technology improves performance",
    "Virtual reality becomes popular",
    "Tesla improves battery technology",
    "Microsoft updates Windows OS",
    "Quantum computing is the future",
    "Researchers build humanoid robot",
    "Apple releases iOS update",
    "SpaceX sends astronauts to ISS",
    "Google invests in AI startups",

    # World News
    "Government announces new sports policy",
    "Heavy rains cause floods in India",
    "Prime Minister visits Japan",
    "Elections bring new government",
    "UN meeting discusses climate change",
    "Earthquake hits Japan",
    "Floods affect thousands in China",
    "President addresses the nation",
    "Terror attack shocks city",
    "International trade talks begin",
    "New law passed in parliament",
    "Protests continue in capital city",
    "Diplomatic relations improve between countries",
    "Wildfire spreads across California",
    "Refugees seek shelter after war",
    "Leaders meet to discuss peace",
    "Stock markets fall after crisis",
    "India signs deal with USA",
    "Global warming raises concerns",
    "Countries unite against terrorism"
]

labels = (
    ["Sports"] * 20 +
    ["Technology"] * 20 +
    ["World News"] * 20
)

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
samples = [
    "Government announces new sports policy",
    "Tesla develops self-driving car",
    "Earthquake hits Japan",
    "NASA sends astronauts to space",
    "India wins cricket series",
    "Apple launches new iPhone"]

for text in samples:
    pred = model.predict(vectorizer.transform([text]))[0]
    print(f"Text: {text}\nPredicted Category: {pred}\n")

all_text = " ".join(texts)
wc = WordCloud(width=800, height=500, background_color="white", colormap="plasma").generate(all_text)
plt.figure(figsize=(10,6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("WordCloud for Entire Dataset")
plt.show()
