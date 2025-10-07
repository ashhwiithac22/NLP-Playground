'''
chunking refers to the process of dividing a sentence into meaningful phrases, called "chunks,"
named entity recognition information extraction that classify named entities mentioned in unstructured text into predefined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.
relation extraction is the task of identifying and classifying relationships between entities in text.
'''

import spacy
nlp = spacy.load("en_core_web_sm") # Load the small English model
text = "Virat Kohli plays cricket for India in 2025."
doc = nlp(text) # Process the text with spaCy NLP 
print("\nNamed Entities:")
for ent in doc.ents: #doc is the processed text
    print(ent.text, "->", ent.label_) #PERSON, GPE, DATE, ORG, etc.
print("\nChunking:")
for chunk in doc.noun_chunks: 
    print(chunk.text)
print("\nRelations:")
for token in doc: #token is each word in the doc
    if token.dep_ == "ROOT":  #dep is dependency label, ROOT is the main verb(find the main action verb in the sentence)
        subject = [w.text for w in token.lefts if w.dep_ == "nsubj"] #nsubj is nominal subject , the one who is doing the action
        #Look at all the words on the left side of the main action (ROOT).Pick the one(s) whose role is subject (nsubj).
        obj = [w.text for w in token.rights if w.dep_ in ("dobj", "pobj")] #dobj is direct object, pobj is object of a preposition
        #Look at all the words on the right side of the main action (ROOT).Pick the one(s) whose role is direct object (dobj) or object of a preposition (pobj).
        #preposition object comes after a preposition like in,for,on,at,withs
        if subject and obj:
            print(subject[0], token.text, obj[0]) #print subject, verb, object
