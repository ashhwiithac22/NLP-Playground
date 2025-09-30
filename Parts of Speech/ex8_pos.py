import nltk
from nltk.tokenize import word_tokenize #breaks text into words
from nltk import pos_tag
from docx import Document
import spacy
from spacy import displacy
#loads small english model this model knows how to do pos tagging
nlp = spacy.load("en_core_web_sm")

# Load the document and read first few non-empty paragraphs
docx = Document(r"D:\NLP LAB\NLP Laboratory\Simple_Sample_Document.docx")

#strip removes leading and trailing white spaces
paragraphs = [p.text.strip() for p in docx.paragraphs if p.text.strip()]
limited_text = ' '.join(' '.join(paragraphs[:3]).split()[:50])  # First 3 paragraphs, 50 words maximum
words = word_tokenize(limited_text)
tagged_words = pos_tag(words)
print(f"{'Word':<15}{'POS Tag'}")
print("-" * 25)
for word, tag in tagged_words:
    print(f"{word:<15}{tag}")
html_lines = ['<html><body><h2>POS Tags</h2><table border="1" cellpadding="5">']
html_lines.append("<tr><th>Word</th><th>POS Tag</th></tr>") #tr table row, th table heading
for word, tag in tagged_words:
    html_lines.append(f"<tr><td>{word}</td><td>{tag}</td></tr>") #td table data
html_lines.append("</table></body></html>")
pos_output_path = r"D:\NLP LAB\NLP Laboratory\nltk_pos_visualization.html"
with open(pos_output_path, "w", encoding="utf-8") as f:
    f.write('\n'.join(html_lines))
print(f"\n POS tagging HTML saved at: {pos_output_path}")
doc = nlp(limited_text)
html = displacy.render(doc, style="dep", page=True) #dep shows how words in grammar are connected
displacy_output_path = r"D:\NLP LAB\NLP Laboratory\spacy_displacy_visualization.html"
with open(displacy_output_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"spaCy displaCy visualization saved at: {displacy_output_path}")
