# News Text Classification with WordCloud

This project demonstrates a **basic keyword-based text classification system** along with a **WordCloud visualization**.  
It classifies news headlines into three categories: **Sports**, **Technology**, and **World News**.

---

## 📌 Features
- Generates a **WordCloud** of news headlines.  
- Implements a **rule-based classifier** using keyword matching.  
- Categorizes news into:
  - 🏏 **Sports**  
  - 💻 **Technology**  
  - 🌍 **World News**  

---

## 🛠️ Tech Stack
- **Python 3**
- [Matplotlib](https://matplotlib.org/) – Visualization  
- [WordCloud](https://amueller.github.io/word_cloud/) – Generating word clouds  

---

## 📂 Workflow
1. Collect a set of **sample news texts** with labels.  
2. Combine all texts and generate a **WordCloud**.  
3. Define **keyword dictionaries** for each category (Sports, Technology, World News).  
4. Classify new sample sentences by checking for keyword matches.  
5. Print out **predicted categories**.  

---

## 🚀 How to Run
1. Clone this repository:
```bash
git clone https://github.com/ashhwiithac22/NLP-Playground/new/main/Text%20classification
cd your-repo-name
```
2.Install dependencies:
   ```bash
pip install matplotlib wordcloud
   ````
3. Run the script:
```
python main.py
```
4.The WordCloud will be displayed, and predictions for sample texts will be printed in the console.
