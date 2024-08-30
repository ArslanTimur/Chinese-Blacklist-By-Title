import os

paths = os.listdir('dict')

for path in paths:
    with open('dict' + '\\' + path,'r', encoding='utf-8') as f:    
        wordlist = f.read().splitlines()
    wordlist = list(set(wordlist))
    wordlist = list(filter(('').__ne__, wordlist)) 
    
    with open('rules' + '\\' + path,'w', encoding='utf-8') as f:
        f.writelines(['title *= "' + string + '"\n' for string in wordlist])
    
paths.append('manual_rules.txt')
open('rules\\all_in_one.txt', 'w', encoding='utf-8').close()
aio = open('rules\\all_in_one.txt', 'a', encoding='utf-8')

for path in paths:
    with open('rules' + '\\' + path,'r', encoding='utf-8') as f:
        aio.writelines([string for string in f.readlines()])

aio.close()