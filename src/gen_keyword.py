# TBD
import jieba

f = open('dict\machinegen_keywords.txt', 'w', encoding='utf-8')
jieba.load_userdict('dict\manual_keywords.txt') 
raw_list = ['rawtext\google.txt', 'rawtext\gpt4o.txt']
text = ''

for raw in raw_list:
    f = open(raw, 'r', encoding='utf-8')
    for l in f.readlines():
        text += l

for i in list(set(jieba.cut(text))):
    w = str(i)
    if len(w) > 1:
        print(w)

f.close()
