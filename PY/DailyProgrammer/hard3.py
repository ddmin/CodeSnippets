# [Hard] Challenge 3

def main():
    with open("./Files/scramble.txt") as f:
        words = f.read()

    word_lst = [word for word in words.split('\n')][:-1]
    scrambled = ['mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle', 'nalraoci', 'nsdeuto', 'amrhat', 'inknsy', 'iferkna']

    for scr in sorted(scrambled, key=len):
        match = [word for word in word_lst if sorted(word) == sorted(scr)]
        print(scr + " -> " + match[0])

if __name__ == '__main__':
    main()
