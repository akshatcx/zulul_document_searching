import os
import re
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import wordnet, stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = stopwords.words('english')

def brackets(test_str): 
    ret = '' 
    skip1c = 0 
    skip2c = 0 
    for i in test_str: 
        if i == '[': 
            skip1c += 1 
        elif i == '{': 
            skip2c += 1 
        elif i == ']' and skip1c > 0: 
            skip1c -= 1 
        elif i == '}'and skip2c > 0: 
            skip2c -= 1 
        elif skip1c == 0 and skip2c == 0: 
            ret += i 
    return ret
<<<<<<< HEAD
file = input("+++")
text = open("abstarct"+file+".txt","r+").read()
text = brackets(text)
text = text.replace('>', ' greater than ')
text = text.replace('<', ' less than ')
text = text.replace('\n', ' ')
text = text.replace('-','')
text=re.sub(r'[\W]', ' ', text)
with open("abstarct_clean"+file+".txt","w+") as f:
    f.write(text)
    
=======
   
def clean(t):
    text = brackets(t)
    text = brackets(text)
    text = text.replace('>', ' greater than ')
    text = text.replace('<', ' less than ')
    text = text.replace('\n',' ')
    text = text.replace("- ",'')
    print(text)
    tokens = word_tokenize(text)
    l = []
    for token in tokens:
        l.append(token.lower())
    for token in l:
        if token in stop_words:
            l.remove(token)
    l = list(filter(lambda a: a not in string.punctuation, l))
    k = " ".join(l)
    return k

for i in range(5):
    te = open("./abstarct" + str(i+1) + ".txt", "r+").read()
    te = clean(te)
    with open("./clean_abstract" + str(i+1) + ".txt", "w+") as f:
        f.write(te)

>>>>>>> 617675e4f5563a0f8e4902ba6f5e7961ebfa2159
