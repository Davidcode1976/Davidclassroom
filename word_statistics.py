# -*- coding:utf-8 -*-

import re

with open('words.txt','r',encoding='utf-8') as f:
    words=f.read()

word_list=re.findall(r'\b\w+\b',words)

word_num=len(word_list)

print('There are %s words in words.txt'% word_num)