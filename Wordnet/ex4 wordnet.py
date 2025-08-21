from docx import Document
from nltk.corpus import wordnet as wn
import matplotlib.pyplot as plt
import networkx as nx
import re
print("Loading document...")
doc = Document(r"E:/NLP LAB/NLP Laboratory/Simple_Sample_Document.docx")
text = "\n".join(para.text for para in doc.paragraphs)
print("Cleaning text...")
text = re.sub(r'[^A-Za-z\s]', '', text).lower()
words = text.split()
word_input = input("Enter a word to analyze: ").lower()
if word_input not in words:
    print(f"The word '{word_input}' is not found in the document.")
else:
    print(f"Word found: {word_input}")

    synsets = wn.synsets(word_input)
    if not synsets:
        print("No synsets found in WordNet for this word.")
    else:
        print(f"\nSynsets for '{word_input}':")
        for s in synsets[:3]:
            print(f"- {s.name()} : {s.definition()}")

            print("\nLemmas:")
            for lemma in s.lemmas():
                print(f"- {lemma.name()}")

            print("\nHypernyms:")
            for hyper in s.hypernyms():
                print(f"- {hyper.name()} : {hyper.definition()}")

            print("\nHyponyms:")
            for hypo in s.hyponyms():
                print(f"- {hypo.name()} : {hypo.definition()}")
            print("-" * 40)
        G = nx.DiGraph()
        level = 0
        node_pos = {}
        x = 0

        for syn in synsets[:3]:
            syn_name = syn.name()
            G.add_node(syn_name, color='red')
            G.add_edge(word_input, syn_name)
            
            for i, lemma in enumerate(syn.lemmas()[:3]):
                lemma_name = lemma.name()
                G.add_node(lemma_name, color='blue')
                G.add_edge(syn_name, lemma_name)

           
            for i, hyper in enumerate(syn.hypernyms()[:2]):
                hyper_name = hyper.name()
                G.add_node(hyper_name, color='green')
                G.add_edge(hyper_name, syn_name)  # from hypernym to synset

            
            for i, hypo in enumerate(syn.hyponyms()[:2]):
                hypo_name = hypo.name()
                G.add_node(hypo_name, color='orange')
                G.add_edge(syn_name, hypo_name)

        pos = {}
        levels = {'word': 0, 'synset': 1, 'lemma': 2, 'hypernym': 0, 'hyponym': 2}
        node_types = {}

        pos[word_input] = (0, 0)
        node_types[word_input] = 'word'
        y_offset = -1
        spacing = 3

        for i, syn in enumerate(synsets[:3]):
            syn_name = syn.name()
            pos[syn_name] = ((i - 1) * spacing, y_offset)
            node_types[syn_name] = 'synset'

            for j, lemma in enumerate(syn.lemmas()[:3]):
                lemma_name = lemma.name()
                pos[lemma_name] = ((i - 1) * spacing - 1 + j * 1, y_offset - 1)
                node_types[lemma_name] = 'lemma'

            for j, hyper in enumerate(syn.hypernyms()[:2]):
                hyper_name = hyper.name()
                pos[hyper_name] = ((i - 1) * spacing - 1 + j * 1, y_offset + 1)
                node_types[hyper_name] = 'hypernym'

            for j, hypo in enumerate(syn.hyponyms()[:2]):
                hypo_name = hypo.name()
                pos[hypo_name] = ((i - 1) * spacing - 1 + j * 1, y_offset - 2)
                node_types[hypo_name] = 'hyponym'

        colors = {'word': 'lightblue', 'synset': 'red', 'lemma': 'blue', 'hypernym': 'green', 'hyponym': 'orange'}
        node_colors = [colors.get(node_types.get(n, 'word'), 'gray') for n in G.nodes()]

        plt.figure(figsize=(14, 10))
        nx.draw(G, pos, with_labels=True, node_color=node_colors,
                node_size=1000, font_size=9, font_weight='bold',
                edge_color='gray', arrows=True)

        plt.title(f"WordNet Concept Graph for '{word_input}'", fontsize=14)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
