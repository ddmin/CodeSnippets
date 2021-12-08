# [Intermediate] Challenge 5

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def main():
    WORDS = '/home/ddmin/Code/Python/DailyProgrammer/Files/words.txt'

    with open(WORDS) as f:
        words = f.read().split()

    anagrams = {}
    for i in range(len(words)):
        for n in range(i+1, len(words)):
            if len(words[i]) == len(words[n]):
                if words[n] not in anagrams and is_anagram(words[i], words[n]):
                    anagrams[words[i]] = words[n]

                    print('Anagram Found!')
                    print(f'\t{words[i]} and {words[n]}')
                    print('Number of anagrams: ' + str(len(anagrams)))
                    print()

if __name__ == '__main__':
    main()
