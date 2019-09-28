import os
import re

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
file = input("+++")
text = open("file"+file+".txt","r+").read()
text = brackets(text)
text = text.replace('>', ' greater than ')
text = text.replace('<', ' less than ')
text = text.replace('\n', ' ')
text = text.replace('-','')
text=re.sub(r'[\W]', ' ', text)
with open("clean"+file+".txt","w+") as f:
    f.write(text)
    