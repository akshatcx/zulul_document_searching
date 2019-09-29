import nltk
from nltk.corpus import wordnet

max_synonym=5
for j in range(1):
    synonyms = dict()
    text = open("clean_abstract"+str(j+1)+".txt").read().split(" ")
    for word in text:
        l = []
        counter = 1
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if counter>max_synonym:
                    break
                l.append(lemma.name())
                counter+=1
        synonyms[word]=l
    print(synonyms)
