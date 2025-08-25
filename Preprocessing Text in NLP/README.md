# 📝 NLP Preprocessing Example

This project demonstrates how to **retrieve text from a webpage** and **preprocess it for Natural Language Processing (NLP)** tasks using Python.

---

## 🚀 Steps Performed in Preprocessing

1. **Retrieve content from a webpage**  
   - Uses the `requests` library to fetch the HTML content of a Wikipedia page.  

2. **Remove HTML tags**  
   - With `BeautifulSoup`, the raw HTML is converted into clean, readable text.  

3. **Remove URLs**  
   - Regular expressions (`re`) are used to remove links starting with `http`, `https`, or `www`.  

4. **Expand contractions**  
   - Example: `"I'll"` → `"I will"`, `"can't"` → `"cannot"`.  

5. **Remove special characters & punctuation**  
   - Only keeps alphabets (A–Z, a–z) and spaces.  

6. **Tokenization**  
   - Breaks down the text into smaller units (words).  
   - Example: `"Natural Language Processing"` → `["natural", "language", "processing"]`.  

7. **Convert to lowercase**  
   - Ensures consistency (avoids treating `"NLP"` and `"nlp"` as different words).  

8. **Remove stopwords**  
   - Common words like *"is"*, *"the"*, *"and"* are removed since they don’t add much meaning.  

9. **Join back into cleaned text**  
   - Final text is a string of meaningful words, ready for NLP tasks.  

---

## 📌 Example Output

### 
🔹 Original text (Wikipedia excerpt)

Natural language processing (NLP) is an interdisciplinary subfield of computer science and linguistics concerned with the interactions...

🔹 After preprocessing

natural language processing interdisciplinary subfield computer science linguistics concerned interactions.

---
### 📂 Files

- ex5_preprocessing.py → Python script performing preprocessing
- Text after cleaning.png → Screenshot of output after cleaning

--- 
### ▶️ How to Run

Copy & run the following in your terminal:

# Clone the repository
```
git clone https://github.com/ashhwiithac22/NLP---Playground.git
cd NLP---Playground
```
# Install dependencies
```
pip install requests beautifulsoup4 nltk contractions
```
# Run the script
```
python "Preprocessing Text in NLP/ex5_preprocessing.py"
```
✅ After running, you’ll see the cleaned text printed in your terminal.
