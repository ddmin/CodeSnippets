##Bunch of Words Definer##

from PyDictionary import PyDictionary 

dic = PyDictionary()
with open('words.txt', 'r') as f:
    words = f.read().split('\n')

dic.meaning('void')

for word in words:
    print(word+':\n')
    for meaning in dic.meaning(word)['Adjective'][:3]:
        print(meaning)
    print('-------------------------------------------------------------------------------')
