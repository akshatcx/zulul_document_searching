import xapian
import os
import re
import nltk
import string
import pandas as pd
import csv

from nltk.tokenize import word_tokenize
from nltk.corpus import wordset
from nltk.corpus import stopwords
from nltk.corpus import words

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = stopwords.words('english')

fdf = pd.read_csv("fulltext.csv")
adf = pd.read_csv("summaries.csv")

no_full = fdf.shape[0]
no_abs = adf.shape[0]

def remove_brackets(st):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in st:
        if i == '[': skip1c +=1
        elif i == '{': skip2c +=1
        if i == ']' and skip1c > 0: skip1c -=1
        if i == '}' and skip2c > 0: skip2c -=1
        elif skip1c == 0 and skip2c == 0: ret += i
    return ret

def clean(t):
    text = remove_brackets(t)
    text = text.replace('>', ' greater than ')
    text = text.replace('<', ' less than ')
    text = text.replace('=', ' equal to ')
    text = text.replace('\n', ' ')
    text = text.replace('- ', '')
    tokens = word_tokenize(text)
    lowert = []
    for token in tokens:
        lowert.append(token.lower())
    for token in lowert:
        if token in stop_words:
            lowert.remove(token)
    lowert = list(filter(lambda a: a not in string.punctuation, lowert))
    #Synonym Code (maybe insert into lowert list)
    return " ".join(lowert)

#List of abstract strings and full strings
abstracts = []
fulls = []

def exists(w):
    return w.lower() in word.words()

for i in range(no_abs):
    text = remove_brackets(adf.loc[i, "abstract"])
    cleaned_text = clean(text)
    
    #Synonym Code (maybe insert into cleaned text)
    abstracts.append(cleaned_text)

for i in range(no_full):
    text = remove_brackets(fdf.loc[i, "paper_text"])
    cleaned_text = clean(text)
    fulls.append(cleaned_text)

#Answer Matrix
matrix = []

#Xapian Code

with open("./output_matrix.csv", "w+", newline = "") as f:
    writer = csv.writer(f)
    writer.writerows(martix)

