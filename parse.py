import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
stemmer = PorterStemmer()
stop_words = stopwords.words('english')

f = open("test_set/abstarct_clean1.txt", "r+")
inp = f.read()
f.close()

tokens = word_tokenize(inp)
clean_tokens = tokens = tokens[:]

for token in tokens:
    if token in stop_words: clean_tokens.remove(token)


table = str.maketrans('', '', string.punctuation)
clean_tokens = [word.translate(table) for word in tokens]
print(' '.join(clean_tokens))

all_synonyms = []

for word in clean_tokens:
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            all_synonyms.append(lemma.name())

stemmed = []
for word in all_synonyms:
    stemmed.append(stemmer.stem(word))

all_synonyms = list(set(all_synonyms))
# print(all_synonyms)
