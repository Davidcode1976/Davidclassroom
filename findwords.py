# -*- coding:utf-8 -*-
import re

with open('from.txt','r',encoding='utf-8')as f:
    text=f.read()
words=re.findall(r'\b[a-zA-Z]+[a-zA-Z]+\b',text)
words.sort()

#print(words)
with open('to.txt','w',encoding='utf-8')as f:
    for i in words:
        f.writelines(i+'\n')