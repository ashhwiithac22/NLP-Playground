import nltk 
from nltk import CFG, ChartParser, word_tokenize, pos_tag #import necessary modules from nltk
nltk.download('averaged_perceptron_tagger') 
grammar = CFG.fromstring(""" 
S  -> NP VP
NP -> Det N | Det N PP | Name
VP -> V NP | V NP PP | V
PP -> P NP
Det -> 'the' | 'a'
N -> 'dog' | 'cat' | 'park' | 'mouse' | 'garden'
V -> 'chased' | 'saw' | 'played'
P -> 'in' | 'with'
Name -> 'John' | 'Mary'
""") #Define a simple context-free grammar (CFG)

parser = ChartParser(grammar) #Create a parser using the defined grammar
sentence = "the dog chased the cat in the garden" #Example sentence to parse
tokens = word_tokenize(sentence) #Tokenize the sentence into words
print("Tokens:", tokens) #Print the tokens
pos_tags = pos_tag(tokens) #Get part-of-speech tags for the tokens
print("POS Tags:", pos_tags) #Print the POS tags

print("\nParse Trees (from CFG):") 
trees = list(parser.parse(tokens)) #

if not trees:
    print("No parse found with this CFG. (Check grammar and tokens match.)")
else:
    for tree in trees:
        tree.pretty_print()
        print(tree)           

