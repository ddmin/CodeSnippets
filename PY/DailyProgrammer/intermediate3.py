# [Intermediate] Challenge 3

import string


def clean(string):
    i = 1
    while i < len(string):
        if string[-i] in string[:-i]:
            if i == 1:
                string = string[:-i]
            else:
                string = string[:-i] + string[-i + 1:]
        else:
            i += 1
    return string


def convert(letter, key):
    if not letter.isalpha():
        return letter

    if letter.isupper():
        return convert(letter.lower(), key).upper()

    return key[ord(letter) - 97]

def revert(letter, key):
    if not letter.isalpha():
        return letter

    if letter.isupper():
        return revert(letter.lower(), key).upper()

    return chr(key.index(letter) + 97)

def encrypt(msg, word):
    new = ''
    key = clean(word + string.ascii_lowercase)
    for letter in msg:
        new += convert(letter, key)

    return new

def decrypt(msg, word):
    new = ''
    key = clean(word + string.ascii_lowercase)
    for letter in msg:
        new += revert(letter, key)

    return new

def main():
    print(encrypt('Flee at once, we are discovered!', 'zebras'))
    print(decrypt('Siaa zq lkba, va zoa rfpbluaoar!', 'zebras'))


if __name__ == '__main__':
    main()
