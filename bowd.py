##Bunch of Words Definer##

from PyDictionary import PyDictionary 

dic = PyDictionary()
with open('words.txt', 'r') as f:
    words = f.read().split('\n')

dic.meaning('void')

for word in words:
    print(word+':')
    try:
        for part_of_speech in dic.meaning(word).keys():
            print('\n'+part_of_speech+':\n')
            for meaning in dic.meaning(word)[part_of_speech]:
                print(meaning)
        print('-------------------------------------------------------------------------------')
    except:
        pass

